from pathlib import Path

from parser import parse_cpp
from call_graph import (
    build_call_graph,
    has_cycle
)

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

root = parse_cpp(code)

graph = build_call_graph(root)

print("CALL GRAPH:")

for node, neighbors in graph.items():

    print(
        node,
        "->",
        neighbors
    )
print()
print(
    "RECURSION DETECTED:",
    has_cycle(graph)
)
