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

def extract_recurrence(function_node, function_name):

    recursion_type = classify_recursion(
        function_node,
        function_name
    )

    divide = looks_like_divide_and_conquer(
        function_node,
        function_name
    )

    if recursion_type not in ("LINEAR", "BINARY","MULTI_BRANCH"):
        return None

    if not divide:
        return None


    work = analyze_node(function_node)

    symbols = collect_divide_variables(function_node)

    definitions = collect_variable_definitions(function_node)

    calls = recursive_calls(
        function_node,
        function_name
    )


    divisors = []

    for call in calls:

        argument_type = classify_argument(call)

        divisor = divisor_from_argument(argument_type)

        if divisor is None:
            divisor = get_call_divisor(
            call,
            symbols
        )

        if divisor is None:

            variable = get_argument_name(call)

            if variable:

                expression = resolve_definition(
                variable,
                definitions
            )

                if expression:
                    divisor = detect_divisor(
                    expression
                )

        if divisor is None:
            return None

        divisors.append(divisor)

# All recursive calls must divide by the same value
    if len(set(divisors)) != 1:
        return None

    recurrence = make_recurrence(
    a=len(calls),
    b=divisors[0],
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