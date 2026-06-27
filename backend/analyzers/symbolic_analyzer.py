def collect_half_variables(function_node):

    variables = {}

    def visit(node):

        if node.type == "declaration":

            text = node.text.decode("utf8")

            if "/2" in text or "/ 2" in text:

                pieces = text.split()

                if len(pieces) >= 2:

                    name = pieces[1]

                    name = name.split("=")[0]

                    variables[name.strip()] = "HALF"

        for child in node.children:
            visit(child)

    visit(function_node)

    return variables