from pathlib import Path

from parser import parse_cpp
from function_analyzer import collect_functions
from analyzers.recursion_analyzer import recursive_calls

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

code = cpp_file.read_text()

root = parse_cpp(code)

functions = collect_functions(root)

for name,node in functions.items():

    print(name)

    print(
        len(
            recursive_calls(
                node,
                name
            )
        )
    )