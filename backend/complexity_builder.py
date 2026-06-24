from complexity_model import (
    make_complexity,
    multiply,
    add
)
from analyzers.recursion_analyzer import(
    classify_recursion
)
from ast_utils import (
    get_function_name,
    called_function_name
)

def get_update_expression(for_node):

    for child in for_node.children:

        if (
            child.type == "update_expression"
            or child.type == "assignment_expression"
        ):
            return child

    return None

def analyze_node(
    node,
    function_table=None
):
    if node.type == "function_definition":

        function_name = get_function_name(node)

        recursion_type = classify_recursion(
        node,
        function_name
        )

        if recursion_type == "LINEAR":

            return make_complexity(
            n_power=1,
            log_power=0
        )
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
        if (
    function_table
    and called in function_table
):
            return function_table[called]
        return make_complexity()
    # ------------------
    # Compound Statement
    # ------------------

    if node.type == "compound_statement":

        result = make_complexity()

        for child in node.children:

            child_cost = analyze_node(child,function_table)

            result = add(
                result,
                child_cost
            )

        return result

    # ------------------
    # For Loop
    # ------------------

    if node.type == "for_statement":
        update_node = get_update_expression(node)
        is_log_loop = False
        if update_node:
            update_text = update_node.text.decode("utf8")
            if (
        "/=2" in update_text
        or "/= 2" in update_text
        or "*=2" in update_text
        or "*= 2" in update_text
        or "/ 2" in update_text
        or "* 2" in update_text
    ):
                is_log_loop = True
        if is_log_loop:
                    loop_cost = make_complexity(
        n_power=0,
        log_power=1
    )
        else:
                    loop_cost = make_complexity(
            n_power=1,
            log_power=0
        )

        body_cost = make_complexity()

        for child in node.children:

            if child.type == "compound_statement":

                body_cost = analyze_node(child,function_table)

        return multiply(
            loop_cost,
            body_cost
        )

    # ------------------
    # Generic Traversal
    # ------------------

    result = make_complexity()

    for child in node.children:

        child_cost = analyze_node(child,function_table)

        result = add(
            result,
            child_cost
        )

    return result