from pathlib import Path
from extractor import extract_features
from parser import parse_cpp
from complexity_builder import analyze_node
from complex_utils import complexity_to_string

from function_analyzer import (
    build_function_table,
    collect_functions
)
from analyzers.dp_report import detailed_dp_report

from analyzers.recurrence_analyzer import extract_recurrence

from analyzers.master_theorem import (
    solve_master_theorem,
    solve_complexity,
    determine_case,
    detailed_master_report
)

BASE_DIR = Path(__file__).parent
cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

features = extract_features(code)
root = parse_cpp(code)

# Required for static analysis and function table
table = build_function_table(root)

functions = collect_functions(root)

result = analyze_node(root)
reason = "Whole Program Analysis"
rec = None
def section(title):
    return f"{title}\n{'-' * len(title)}"
# ---------------------------------------
# Select target function
# ---------------------------------------

if "solve" in functions:
    target_name = "solve"
elif functions:
    target_name = next(iter(functions))
else:
    target_name = None

# ---------------------------------------
# Analyze recurrence if present
# ---------------------------------------


if target_name:

    node = functions[target_name]

    
    rec = extract_recurrence(
        node,
        target_name
    )
    

    if rec:

        if rec.get("type") == "MEMOIZATION":

            result = table[target_name]
            

            reason = "Dynamic Programming"

        else:

            solve_master_theorem(rec)

            result = solve_complexity(rec)

            reason = (
            f"Master Theorem Case "
            f"{determine_case(rec)}"
        )

    else:

        result = table[target_name]
        reason = "Static Analysis"

# ---------------------------------------
# Output
# ---------------------------------------

DEBUG = False

print("=" * 40)
print("            ALGOLENS")
print("=" * 40)

print(f"\nFile: {cpp_file.name}")

if DEBUG:

    print(section("\nFeatures:"))

    for key, value in features.items():
        print(f"  {key}: {value}")

print(section("\nPredicted Complexity"))

print(
    complexity_to_string(
        result["n_power"],
        result["log_power"]
    )
)



if rec:

    if rec.get("type") == "MEMOIZATION":

        print()

        print(
            detailed_dp_report(result)
        )

    else:

        print()

        print(
            detailed_master_report(
                rec,
                result
            )
        )

print("=" * 40)

print(section("\nFunction Summary"))

for name, comp in table.items():

    print(
        name,
        "→",
        complexity_to_string(
            comp["n_power"],
            comp["log_power"]
        )
    )