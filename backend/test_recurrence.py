from parser import parse_cpp
from function_analyzer import collect_functions

from analyzers.recurrence_analyzer import (
    extract_recurrence,
    recurrence_to_string
)

code = """

void solve(int n){
    int mid=n/2;
    int x=mid;
    solve(x);
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