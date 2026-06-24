from function_analyzer import collect_functions
from complexity_builder import called_function_name


def build_call_graph(root):

    functions = collect_functions(root)

    graph = {}

    for name in functions:
        graph[name] = []

    def visit(node, current_function=None):

        if node.type == "function_definition":

            for fname, fnode in functions.items():

                if fnode == node:
                    current_function = fname
                    break

        if (
            node.type == "call_expression"
            and current_function
        ):

            called = called_function_name(node)

            if called in functions:

                graph[current_function].append(
                    called
                )

        for child in node.children:
            visit(child, current_function)

    visit(root)

    return graph
def has_cycle(graph):

    visited = set()

    recursion_stack = set()

    def dfs(node):

        visited.add(node)

        recursion_stack.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                if dfs(neighbor):
                    return True

            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)

        return False

    for node in graph:

        if node not in visited:

            if dfs(node):
                return True

    return False