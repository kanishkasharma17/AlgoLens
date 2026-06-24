from pathlib import Path

from parser import parse_cpp
from function_analyzer import collect_functions

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

root = parse_cpp(code)

from function_analyzer import (
    collect_functions,
    build_function_table
)

functions = collect_functions(root)

print("FUNCTIONS FOUND:")
print(functions.keys())

print("\nFUNCTION TABLE:")

table = build_function_table(root)

for name, complexity in table.items():
    print(name, "->", complexity)