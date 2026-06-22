from parser import parse_cpp
from complexity_builder import analyze_node
from complex_utils import complexity_to_string

from pathlib import Path

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

root = parse_cpp(code)
def debug(node, depth=0):

    print(
        " " * depth,
        node.type
    )

    for child in node.children:
        debug(child, depth + 2)

debug(root)
result = analyze_node(root)


print(
    complexity_to_string(
        result["n_power"],
        result["log_power"]
    )
)
