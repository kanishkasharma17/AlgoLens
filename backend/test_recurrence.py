from parser import parse_cpp
from function_analyzer import collect_functions

from analyzers.recurrence_analyzer import (
    extract_recurrence,
    recurrence_to_string
)

code = """

void solve(int n){
    if(n<=1) return;
    int third=n/3;
    solve(third);
}

"""

root = parse_cpp(code)

functions = collect_functions(root)

node = functions["solve"]

rec = extract_recurrence(
    node,
    "solve"
)

print(rec)

print()

print(
    recurrence_to_string(rec)
)