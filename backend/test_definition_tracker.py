from parser import parse_cpp
from function_analyzer import collect_functions

from analyzers.definition_tracker import (
    collect_variable_definitions
)

code = """

void solve(int n)
{
    int mid=n/2;

    int third=n/3;

    int x=mid;

    solve(x);
}

"""

root = parse_cpp(code)

functions = collect_functions(root)

node = functions["solve"]

definitions = collect_variable_definitions(node)

print(definitions)