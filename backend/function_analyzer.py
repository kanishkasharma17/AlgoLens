from parser import parse_cpp
from complexity_builder import analyze_node
from ast_utils import get_function_name
from analyzers.recurrence_analyzer import (
    extract_recurrence
)
from analyzers.master_theorem import (
    solve_master_theorem,
    solve_complexity
)
from complex_utils import make_complexity

def build_function_table(root):

    functions = collect_functions(root)

    function_complexities = {}

    # Initial values
    for name in functions:
        
        function_complexities[name] = make_complexity()

    # Fixed-point propagation
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

    # -----------------------------
    # Master Theorem Integration
    # -----------------------------

    # -----------------------------
# Master Theorem Integration
# -----------------------------

    for name, node in functions.items():

        rec = extract_recurrence(node, name)

        if rec:

            if "type" in rec:

                complexity = analyze_node(
            node,
            function_complexities,
            name
        )

            else:

                print("MASTER BRANCH")

                solve_master_theorem(rec)

                complexity = solve_complexity(rec)

        else:

            print("STATIC BRANCH")

            complexity = analyze_node(
        node,
        function_complexities,
        name
    )

        function_complexities[name] = complexity

    return function_complexities

def find_identifier(node):

    if node.type == "identifier":
        return node

    for child in node.children:

        result = find_identifier(child)

        if result:
            return result

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
