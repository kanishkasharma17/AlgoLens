from parser import parse_cpp
from complexity_builder import analyze_node

def build_function_table(root):

    functions = collect_functions(root)

    function_complexities = {}

    # Pass 1
    for name, node in functions.items():

        function_complexities[name] = analyze_node(node)

    # Pass 2
    for name, node in functions.items():

        function_complexities[name] = analyze_node(
            node,
            function_complexities
        )

    return function_complexities

def find_identifier(node):

    if node.type == "identifier":
        return node

    for child in node.children:

        result = find_identifier(child)

        if result:
            return result

    return None
def get_function_name(node):

    ident = find_identifier(node)

    if ident:
        return ident.text.decode("utf8")

    return None
def collect_functions(root):

    functions = {}

    def visit(node):

        if node.type == "function_definition":

            name = get_function_name(node)

            functions[name] = node

        for child in node.children:
            visit(child)

    visit(root)

    return functions
