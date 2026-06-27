from parser import parse_cpp
from function_analyzer import collect_functions
from analyzers.symbolic_analyzer import collect_half_variables

code = """

void mergeSort(int l,int r)
{
    int mid=(l+r)/2;

    mergeSort(l,mid);

    mergeSort(mid+1,r);
}

"""

root = parse_cpp(code)

functions = collect_functions(root)

node = functions["mergeSort"]

print(
    collect_half_variables(node)
)