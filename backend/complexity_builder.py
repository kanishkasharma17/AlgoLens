from complexity_model import (
    make_complexity,
    multiply,
    add
)



def find_identifier(node):

    if node.type == "identifier":
        return node

    for child in node.children:

        result = find_identifier(child)

        if result:
            return result

    return None
def called_function_name(node):

    if node.type != "call_expression":
        return None

    ident = find_identifier(node)

    if ident:
        return ident.text.decode("utf8")

    return None

def analyze_node(node):

    # ------------------
    # STL Calls
    # ------------------
    
    if node.type == "call_expression":
        
        called = called_function_name(node)

        if called == "sort":
            return make_complexity(
                n_power=1,
                log_power=1
            )

        if called in (
            "binary_search",
            "lower_bound",
            "upper_bound"
        ):
            return make_complexity(
                n_power=0,
                log_power=1
            )

        return make_complexity()

    # ------------------
    # Compound Statement
    # ------------------

    if node.type == "compound_statement":

        result = make_complexity()

        for child in node.children:

            child_cost = analyze_node(child)

            result = add(
                result,
                child_cost
            )

        return result

    # ------------------
    # For Loop
    # ------------------

    if node.type == "for_statement":

        loop_cost = make_complexity(
            n_power=1,
            log_power=0
        )

        body_cost = make_complexity()

        for child in node.children:

            if child.type == "compound_statement":

                body_cost = analyze_node(child)

        return multiply(
            loop_cost,
            body_cost
        )

    # ------------------
    # Generic Traversal
    # ------------------

    result = make_complexity()

    for child in node.children:

        child_cost = analyze_node(child)

        result = add(
            result,
            child_cost
        )

    return result