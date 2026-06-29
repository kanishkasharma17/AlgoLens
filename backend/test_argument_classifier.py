from parser import parse_cpp
from function_analyzer import collect_functions

from analyzers.recursion_analyzer import recursive_calls
from analyzers.argument_classifier import classify_argument

code = """

void solve(int n)
{
    solve(n/3);
}

"""

root = parse_cpp(code)

functions = collect_functions(root)

node = functions["solve"]

calls = recursive_calls(node,"solve")

for call in calls:

    print(call.text.decode())

    print(
        classify_argument(call)
    )