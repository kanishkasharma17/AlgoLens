from analyzers.definition_resolver import resolve_definition

definitions = {

    "a":"b;",
    "b":"a;"
}

print(resolve_definition("a", definitions))

