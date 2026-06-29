from analyzers.recursion_analyzer import (
    classify_recursion,
    looks_like_divide_and_conquer,
    recursive_calls
)

from complexity_builder import analyze_node

from analyzers.symbolic_analyzer import (      collect_divide_variables,
    get_call_divisor
)
def make_recurrence(a, b, work):

    return {
        "a": a,
        "b": b,
        "work": work
    }


def extract_recurrence(
    function_node,
    function_name
):
    symbols=collect_divide_variables(function_node)
    
    recursion_type = classify_recursion(
        function_node,
        function_name
    )

    if recursion_type not in("LINEAR","BINARY"):
        return None
    
    if not looks_like_divide_and_conquer(
        function_node,
        function_name
    ):
        return None

    work = analyze_node(function_node)

    symbols = collect_divide_variables(
    function_node
)


    calls = recursive_calls(
    function_node,
    function_name
)


    call_count = len(calls)

    divisor = get_call_divisor(
    calls[0],
    symbols
)

    recurrence = make_recurrence(
        a=call_count,
        b=divisor,
        work=work
    )

    return recurrence



from complex_utils import (
    complexity_to_string
)


def recurrence_to_string(recurrence):

    if recurrence is None:
        return "No divide-and-conquer recurrence"

    work = recurrence["work"]

    if recurrence["a"] == 1:
        recursive_part = f"T(n/{recurrence['b']})"
    else:
        recursive_part = f"{recurrence['a']}T(n/{recurrence['b']})"

    return (
        f"T(n) = {recursive_part} + "
        f"{complexity_to_string(work['n_power'], work['log_power'])}"
    )