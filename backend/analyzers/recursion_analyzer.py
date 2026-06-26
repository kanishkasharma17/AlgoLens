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
        return {
            "type": "EXPONENTIAL"
        }

    return {
        "n_power": 0,
        "log_power": 0
    }