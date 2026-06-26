from pathlib import Path

from parser import parse_cpp
from function_analyzer import collect_functions
from analyzers.recursion_analyzer import (
    classify_recursion,
    recursion_complexity
)

BASE_DIR = Path(__file__).parent
cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

root = parse_cpp(code)

functions = collect_functions(root)

for name, node in functions.items():

    rtype = classify_recursion(node, name)

    print(name)
    print("Recursion Type:", rtype)
    print("Complexity:", recursion_complexity(rtype))
    print()