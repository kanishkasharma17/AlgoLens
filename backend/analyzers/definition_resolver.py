def resolve_definition(variable, definitions):

    visited = set()

    current = variable

    while current in definitions:

        if current in visited:
            break

        visited.add(current)

        expression = definitions[current]

        expression = expression.replace(";", "").strip()

        # reached a real expression
        if "/" in expression:
            return expression

        # otherwise continue following aliases
        current = expression

    return None