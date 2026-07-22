DP_NAMES = {
    "dp",
    "memo",
    "cache"
}


def uses_dp_table(function_node):

    def visit(node):

        if node.type == "identifier":

            name = node.text.decode("utf8")

            if name in DP_NAMES:
                return True

        for child in node.children:

            if visit(child):
                return True

        return False

    return visit(function_node)


def count_loops(function_node):

    count = 0

    def visit(node):

        nonlocal count

        if node.type in (
            "for_statement",
            "while_statement"
        ):
            count += 1

        for child in node.children:
            visit(child)

    visit(function_node)

    return count


def uses_tabulation(function_node):

    if not uses_dp_table(function_node):
        return False

    loops = count_loops(function_node)

    return loops > 0