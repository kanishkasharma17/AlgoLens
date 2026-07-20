def classify_argument(call_node):

    text = call_node.text.decode("utf8")

    text = text.replace(" ", "")

    if "/2" in text:
        return "HALF"

    if "/3" in text:
        return "THIRD"

    if "mid" in text:
        return "MID"

    if "left" in text:
        return "LEFT"

    if "right" in text:
        return "RIGHT"

    if "pivot" in text:
        return "PIVOT"

    if "n-" in text:
        return "COMPLEMENT"

    return "UNKNOWN"

def get_argument_name(call_node):

    def visit(node):

        if node.type == "identifier":
            return node.text.decode("utf8")

        for child in node.children:
            result = visit(child)
            if result:
                return result

        return None

    return visit(call_node)