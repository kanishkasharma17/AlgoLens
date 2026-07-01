from analyzers.recursion_analyzer import (
    classify_recursion,
    looks_like_divide_and_conquer,
    recursive_calls
)

from complexity_builder import analyze_node

from analyzers.symbolic_analyzer import (      collect_divide_variables,
    get_call_divisor
)
from analyzers.argument_classifier import classify_argument
from analyzers.divisor_mapper import divisor_from_argument
from analyzers.definition_resolver import resolve_definition
from analyzers.definition_tracker import collect_variable_definitions
from analyzers.argument_utils import get_argument_name
from analyzers.symbolic_analyzer import detect_divisor

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

    

    divide = looks_like_divide_and_conquer(
    function_node,
    function_name
)

    

    if recursion_type not in ("LINEAR", "BINARY"):
        return None

    if not divide:
        return None

    work = analyze_node(function_node)

    symbols = collect_divide_variables(
        function_node
    )

    definitions = collect_variable_definitions(
        function_node
    )

    calls = recursive_calls(
        function_node,
        function_name
    )

    call_count = len(calls)

    # -----------------------------
    # Step 1 : Argument Classifier
    # -----------------------------
    argument_type = classify_argument(
        calls[0]
    )

    divisor = divisor_from_argument(
        argument_type
    )

    # -----------------------------
    # Step 2 : Symbolic Analyzer
    # -----------------------------
    if divisor is None:

        divisor = get_call_divisor(
            calls[0],
            symbols
        )

    # -----------------------------
    # Step 3 : Definition Resolver
    # -----------------------------
    if divisor is None:

        variable = get_argument_name(
            calls[0]
        )

        if variable:

            expression = resolve_definition(
                variable,
                definitions
            )

            if expression:

                divisor = detect_divisor(
                    expression
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