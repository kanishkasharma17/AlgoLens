from parser import parse_cpp
from function_analyzer import collect_functions
from analyzers.symbolic_analyzer import collect_divide_variables

code = """

void solve(int n)
{
    if(n<=1)
        return;

    int third = n/3;

    solve(third);
}

"""

root = parse_cpp(code)

functions = collect_functions(root)

node = functions["solve"]

print(
    collect_divide_variables(node)
)