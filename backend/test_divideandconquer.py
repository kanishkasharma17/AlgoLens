from pathlib import Path

from parser import parse_cpp
from function_analyzer import collect_functions
from analyzers.recursion_analyzer import (
    looks_like_divide_and_conquer
)

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

root = parse_cpp(code)

functions = collect_functions(root)

for name, node in functions.items():

    print(name)

    print(
        "Divide & Conquer:",
        looks_like_divide_and_conquer(
            node,
            name
        )
    )