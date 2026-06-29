from complex_utils import make_complexity
from analyzers.symbolic_analyzer import (
    collect_divide_variables,
    get_call_divisor
)
def has_divide_argument(
    call_node,
    symbols
):

    def visit(node):

        # Explicit n/2 or x/2
        if node.type == "binary_expression":

            text = node.text.decode("utf8")

            if "/2" in text or "/ 2" in text:
                return True

        # Symbolic variable (e.g., mid)
        if node.type == "identifier":

            name = node.text.decode("utf8")

            if (
                name in symbols
                and symbols[name] == "HALF"
            ):
                return True

        for child in node.children:

            if visit(child):
                return True

        return False

    return visit(call_node)

def count_self_calls(function_node, function_name):

    count = 0

    def visit(node):
        nonlocal count

        if node.type == "call_expression":

            text = node.text.decode("utf8")

            if function_name in text:
                count += 1

        for child in node.children:
            visit(child)

    visit(function_node)

    return count


def classify_recursion(
    function_node,
    function_name
):

    calls = count_self_calls(
        function_node,
        function_name
    )

    if calls == 0:
        return "NONE"

    if calls == 1:
        return "LINEAR"

    if calls == 2:
        return "BINARY"

    return "MULTI_BRANCH"

def recursion_complexity(recursion_type):

    if recursion_type == "LINEAR":
        return {
            "n_power": 1,
            "log_power": 0
        }

    if recursion_type == "BINARY":
        return make_complexity(
            family="EXPONENTIAL",
            base=2
        )

    return {
        "n_power": 0,
        "log_power": 0
    }


def recursive_calls(function_node, function_name):

    calls = []

    def visit(node):

        if node.type == "call_expression":

            text = node.text.decode("utf8")

            if function_name in text:
                calls.append(node)

        for child in node.children:
            visit(child)

    visit(function_node)

    return calls

from analyzers.symbolic_analyzer import collect_divide_variables

def looks_like_divide_and_conquer(
    function_node,
    function_name
):

    symbols = collect_divide_variables(function_node)
    

    calls = recursive_calls(
        function_node,
        function_name
    )

    

    if len(calls) == 0:
        return False

    for call in calls:

        

        divisor = get_call_divisor(
            call,
            symbols
        )

        

        if divisor is None:
            return False

    return True
