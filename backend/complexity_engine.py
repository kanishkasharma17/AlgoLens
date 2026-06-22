def predict_complexity(features):

    depth = features["max_loop_depth"]

    sort_calls = features.get(
        "sort_calls",
        0
    )

    recursive_calls = features.get(
        "recursive_calls",
        0
    )

    logarithmic_loops = features.get(
        "logarithmic_loops",
        0
    )

    if sort_calls > 0:
        return "O(n log n)"

    if logarithmic_loops > 0:
        return "O(log n)"

    if recursive_calls >= 2:
        return "Exponential"

    if depth == 0:
        return "O(1)"

    if depth == 1:
        return "O(n)"

    if depth == 2:
        return "O(n²)"

    if depth == 3:
        return "O(n³)"

    return "Unknown"
