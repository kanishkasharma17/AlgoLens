from analyzers.recursion_analyzer import (
    classify_recursion,
    looks_like_divide_and_conquer
)

from complexity_builder import analyze_node


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

    recursion_type = classify_recursion(
        function_node,
        function_name
    )

    if recursion_type != "BINARY":
        return None

    if not looks_like_divide_and_conquer(
        function_node,
        function_name
    ):
        return None

    work = analyze_node(function_node)

    recurrence = make_recurrence(
        a=2,
        b=2,
        work=work
    )

    return recurrence


from analyzers.recursion_analyzer import (
    classify_recursion,
    looks_like_divide_and_conquer
)

from complexity_builder import analyze_node


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

    recursion_type = classify_recursion(
        function_node,
        function_name
    )

    if recursion_type not in (
    "LINEAR",
    "BINARY"
):
        return None

    if not looks_like_divide_and_conquer(
        function_node,
        function_name
    ):
        return None

    work = analyze_node(function_node)

    calls = 1

    if recursion_type == "BINARY":
        calls = 2

    recurrence = make_recurrence(
    a=calls,
    b=2,
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