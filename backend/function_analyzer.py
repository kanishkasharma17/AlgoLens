from parser import parse_cpp
from complexity_builder import analyze_node

def build_function_table(root):

    functions = collect_functions(root)

    function_complexities = {}

    for name in functions:

        function_complexities[name] = {
        "n_power": 0,
        "log_power": 0
        }
    changed = True

    while changed:

        changed = False

        for name, node in functions.items():

            new_complexity = analyze_node(
            node,
            function_complexities
        )

            if new_complexity != function_complexities[name]:

                function_complexities[name] = new_complexity

                changed = True

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
