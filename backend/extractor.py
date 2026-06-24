from parser import parse_cpp
from call_graph import(
    build_call_graph,
    recursive_functions
)
# STL MAP
STL_FUNCTIONS = {
    "sort": "sort_calls",
    "binary_search": "binary_search_calls",
    "lower_bound": "lower_bound_calls",
    "upper_bound": "upper_bound_calls"
}

LOOP_TYPES = {
    "for_statement",
    "while_statement",
    "do_statement"
}


def extract_features(code):

    root = parse_cpp(code)
    graph = build_call_graph(root)

    recursive_function_names = (
        recursive_functions(graph)
    )
    print("\nGRAPH =", graph)
    print("RECURSIVE FUNCTIONS =", recursive_function_names)

    features = {
        "for_loops": 0,
        "while_loops": 0,
        "do_loops": 0,
        "max_loop_depth": 0,
        "nested_loops": 0,
        "recursive_functions": 0,
        "recursive_calls": 0,
        "sort_calls": 0,
        "binary_search_calls": 0,
        "lower_bound_calls": 0,
        "upper_bound_calls": 0,
        "linear_bounds": 0,
        "constant_bounds": 0,
        "logarithmic_loops":0
    }

    

    def node_text(node):
        return code[
            node.start_byte:
            node.end_byte
        ]

    def find_identifier(node):

        if node.type == "identifier":
            return node

        for child in node.children:

            result = find_identifier(child)

            if result:
                return result

        return None

    def get_function_name(func_node):

        ident = find_identifier(func_node)

        if ident:
            return node_text(ident)

        return None

    def called_function_name(node):

        if node.type != "call_expression":
            return None

        ident = find_identifier(node)

        if ident:
            return node_text(ident)

        return None
    
    def get_loop_condition(node):
        for child in node.children:
            if child.type == "binary_expression":
                return child

        return None
    
    def get_update_expression(for_node):
        for child in for_node.children:
            if (
            child.type == "update_expression"
            or child.type == "assignment_expression"
        ):
                return child
        return None
    
    def visit(node, depth=0, current_function=None):

        if node.type == "function_definition":
            current_function = get_function_name(node)

        if node.type == "call_expression":

            called = called_function_name(node)
            
            # recursion detection
            

            # STL detection
            if called in STL_FUNCTIONS:
                features[
                    STL_FUNCTIONS[called]
                ] += 1

        if node.type == "for_statement":
            features["for_loops"] += 1
            #LOOP BOUND ANALYSIS
            condition = get_loop_condition(node)
            if condition:
                condition_text = node_text(condition)
                if "n" in condition_text:
                    features["linear_bounds"] += 1
                elif any(
        ch.isdigit()
        for ch in condition_text
    ):
                    features["constant_bounds"] += 1
# Logarithmic Loop Analysis 

            update_node = get_update_expression(node)
            if update_node:
                update_text = node_text(update_node)
                if (
                    "*=2" in update_text
                or "*= 2" in update_text
                or "/=2" in update_text
                or "/= 2" in update_text
                or "* 2" in update_text
                or "/ 2" in update_text
):
    
                    features["logarithmic_loops"] += 1

        if node.type == "while_statement":
            features["while_loops"] += 1

        if node.type == "do_statement":
            features["do_loops"] += 1

        if node.type in LOOP_TYPES:

            depth += 1

            features["max_loop_depth"] = max(
                features["max_loop_depth"],
                depth
            )

            if depth >= 2:
                features["nested_loops"] += 1

        for child in node.children:
            visit(
                child,
                depth,
                current_function
            )

    visit(root)

    features["recursive_functions"] = len(
        recursive_function_names
    )
    recursive_call_count = 0
    for func in recursive_function_names:

        recursive_call_count += len(
        graph[func]
    )

    features["recursive_calls"] = (
    recursive_call_count
)

    features["total_loops"] = (
        features["for_loops"]
        + features["while_loops"]
        + features["do_loops"]
    )

    return features