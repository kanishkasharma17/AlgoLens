def collect_divide_variables(function_node):

    variables = {}

    def visit(node):

        if node.type == "declaration":

            text = node.text.decode("utf8")

            divisor = detect_divisor(text)

            if divisor:

                pieces = text.split()

                if len(pieces) >= 2:

                    name = pieces[1]

                    name = name.split("=")[0]

                    variables[name.strip()] = divisor

        for child in node.children:
            visit(child)

    visit(function_node)

    return variables

def detect_divisor(text):

    text = text.replace(" ", "")

    if "/" not in text:
        return None

    parts = text.split("/")

    if len(parts) < 2:
        return None

    divisor = ""

    for ch in parts[1]:

        if ch.isdigit():
            divisor += ch
        else:
            break

    if divisor:

        return int(divisor)

    return None

def get_call_divisor(
    call_node,
    symbols
):

    def visit(node):

        # Explicit n/2, n/3, n/4...
        if node.type == "binary_expression":

            text = node.text.decode("utf8")

            divisor = detect_divisor(text)

            if divisor:
                return divisor

        # Symbolic variable (mid, third...)
        if node.type == "identifier":

            name = node.text.decode("utf8")

            if name in symbols:
                return symbols[name]

        for child in node.children:

            result = visit(child)

            if result is not None:
                return result

        return None

    return visit(call_node)