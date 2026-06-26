from complex_utils import make_complexity

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

def looks_like_divide_and_conquer(
    function_node,
    function_name
):
    calls = recursive_calls(
        function_node,
        function_name
    )

    # Divide & Conquer should make exactly
    # two recursive calls
    if len(calls) != 2:
        return False

    # Look for "/2" or "/ 2" anywhere
    # in the function body
    text = function_node.text.decode("utf8")

    if "/2" in text or "/ 2" in text:
        return True

    return False
    