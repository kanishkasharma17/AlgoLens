from pathlib import Path
from extractor import extract_features
from parser import parse_cpp
from complexity_builder import analyze_node
from complex_utils import complexity_to_string

BASE_DIR = Path(__file__).parent

cpp_file = BASE_DIR / "sample.cpp"

with open(cpp_file, "r") as f:
    code = f.read()

features = extract_features(code)
root = parse_cpp(code)

result = analyze_node(root)
DEBUG=True
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