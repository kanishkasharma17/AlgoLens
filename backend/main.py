from pathlib import Path
from extractor import extract_features
from parser import parse_cpp
from complexity_builder import analyze_node
from complex_utils import complexity_to_string
from function_analyzer import(
    build_function_table,
    collect_functions
) 
from analyzers.master_theorem import (
    solve_master_theorem,
    master_report
)
from analyzers.recurrence_analyzer import extract_recurrence
from analyzers.master_theorem import (
    solve_complexity,
    determine_case
)
BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

features = extract_features(code)
root = parse_cpp(code)

table = build_function_table(root)

functions = collect_functions(root)

# Default result
result = analyze_node(root)
reason = "Whole Program Analysis"

# Choose a target function
if "solve" in functions:
    target_name = "solve"
elif functions:
    target_name = next(iter(functions))
else:
    target_name = None

if target_name:

    node = functions[target_name]

    rec = extract_recurrence(
        node,
        target_name
    )
    

    if rec:

        solve_master_theorem(rec)

        result = solve_complexity(rec)

        reason = (
            f"Master Theorem Case "
            f"{determine_case(rec)}"
        )

    else:

        result = table[target_name]

        reason = "Static Analysis"

DEBUG = False
print("=" * 40)
print("            ALGOLENS")
print("=" * 40)

print(f"\nFile: {cpp_file.name}")

if DEBUG:
    print("\nFeatures:")
    for key, value in features.items():
        print(f"  {key}: {value}")

print("\nPredicted Complexity:")
print(
    complexity_to_string(
    result["n_power"],
    result["log_power"]
    )
)

print("\nComplexity Object:")
print(result)





print("=" * 40)
print("\nFUNCTION TABLE:")

for name, comp in table.items():

    print(
        name,
        "->",
        complexity_to_string(
            comp["n_power"],
            comp["log_power"]
        )
    )

reason = "Static Analysis"

if rec:

    reason = (
        f"Master Theorem "
        f"Case {determine_case(rec)}"
    )

print("\nReason:")
print(reason)



