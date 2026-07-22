from complexity_model import make_complexity
def parameter_count(function_node):

    for child in function_node.children:

        if child.type == "function_declarator":

            for node in child.children:

                if node.type == "parameter_list":

                    count = 0

                    for p in node.children:

                        if p.type == "parameter_declaration":
                            count += 1

                    return count

    return 0

def memo_table_name(function_node):

    names = {
        "dp",
        "memo",
        "cache"
    }

    def visit(node):

        if node.type == "identifier":

            text = node.text.decode("utf8")

            if text in names:
                return text

        for child in node.children:

            result = visit(child)

            if result is not None:
                return result

        return None

    return visit(function_node)



from complexity_model import make_complexity


def estimate_dp_complexity(function_node):

    parameters = parameter_count(function_node)

    table = memo_table_name(function_node)

    if table is None:
        return None

    if parameters == 1:

        return make_complexity(
            n_power=1,
            log_power=0
        )

    if parameters == 2:

        return make_complexity(
            n_power=2,
            log_power=0
        )

    if parameters == 3:

        return make_complexity(
            n_power=3,
            log_power=0
        )

    return make_complexity(
        n_power=parameters,
        log_power=0
    )

def uses_memoization(function_node):

    return memo_table_name(function_node) is not None