def find_identifier(node):

    if node.type == "identifier":
        return node

    for child in node.children:

        result = find_identifier(child)

        if result:
            return result

    return None

def called_function_name(node):

    if node.type != "call_expression":
        return None

    ident = find_identifier(node)

    if ident:
        return ident.text.decode("utf8")

    return None

def get_function_name(node):

    ident = find_identifier(node)

    if ident:
        return ident.text.decode("utf8")

    return None

