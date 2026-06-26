from parser import parse_cpp
from function_analyzer import collect_functions

from analyzers.recurrence_analyzer import (
    extract_recurrence,
    recurrence_to_string
)

code = """

void bs(int n)
{
    if(n<=1)
        return;

    bs(n/2);
}

"""

root = parse_cpp(code)

functions = collect_functions(root)

node = functions["bs"]

rec = extract_recurrence(
    node,
    "bs"
)

print(rec)

print()

print(
    recurrence_to_string(rec)
)