from pathlib import Path
from parser import parse_cpp
from function_analyzer import collect_functions

from analyzers.recursion_analyzer import (
    count_self_calls,
    classify_recursion
)

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

root = parse_cpp(code)

functions = collect_functions(root)

print("RECURSION ANALYSIS\n")

for name, node in functions.items():

    print(
        name,
        "->",
        count_self_calls(node, name),
        "self calls"
    )

    print(
        "Type:",
        classify_recursion(
            node,
            name
        )
    )

    print()