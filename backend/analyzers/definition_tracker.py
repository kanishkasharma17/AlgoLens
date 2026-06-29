def collect_variable_definitions(function_node):

    definitions = {}

    def visit(node):

        if node.type == "declaration":

            text = node.text.decode("utf8")

            if "=" in text:

                left, right = text.split("=", 1)

                name = left.split()[-1].strip()

                definitions[name] = right.strip()

        for child in node.children:
            visit(child)

    visit(function_node)

    return definitions