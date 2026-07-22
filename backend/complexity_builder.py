from complexity_model import (
    make_complexity,
    multiply,
    add
)
from analyzers.recursion_analyzer import(
    classify_recursion,
    recursion_complexity
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
    function_table=None,
    current_function=None
):
    name_node=node.child_by_field_name("declarator")
    if name_node:
         text=name_node.text.decode("utf8")
         current_function=text.split("(")[0].split()[-1]
    if node.type == "function_definition":

        for child in node.children:

            if child.type == "compound_statement":

                return analyze_node(
                child,
                function_table,
                current_function
            )

        return make_complexity()
    
    # ------------------
    # STL Calls
    # ------------------
    
    if node.type == "call_expression":
        
        called = called_function_name(node)
        if(
             current_function is not  None and called==current_function):
             return make_complexity()
        
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

            child_cost = analyze_node(child,function_table,current_function)

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

        body = node.child_by_field_name("body")

        if body:
            body_cost = analyze_node(
        body,
        function_table,
        current_function
    )
        else:
            body_cost = make_complexity()

        return multiply(
            loop_cost,
            body_cost
        )

    # ------------------
    # Generic Traversal
    # ------------------

    result = make_complexity()

    for child in node.children:

        child_cost = analyze_node(child,function_table,current_function)

        result = add(
            result,
            child_cost
        )

    return result