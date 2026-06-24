from function_analyzer import collect_functions
from ast_utils import (
    get_function_name,
    called_function_name
)


def build_call_graph(root):

    functions = collect_functions(root)

    graph = {}

    for name in functions:
        graph[name] = []

    def visit(node, current_function=None):

        if node.type == "function_definition":
            current_function = get_function_name(node)

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
def recursive_functions(graph):

    recursive_nodes = set()

    visited = set()
    recursion_stack = []

    def dfs(node):

        visited.add(node)
        recursion_stack.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                dfs(neighbor)

            elif neighbor in recursion_stack:

                cycle_start = recursion_stack.index(
                    neighbor
                )

                cycle_nodes = recursion_stack[
                    cycle_start:
                ]

                recursive_nodes.update(
                    cycle_nodes
                )

        recursion_stack.pop()

    for node in graph:

        if node not in visited:
            dfs(node)

    return recursive_nodes