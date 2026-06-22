def complexity_to_string(n_power, log_power):

    if n_power == 0 and log_power == 0:
        return "O(1)"

    parts = []

    if n_power > 0:

        if n_power == 1:
            parts.append("n")
        else:
            parts.append(f"n^{n_power}")

    if log_power > 0:

        if log_power == 1:
            parts.append("log n")
        else:
            parts.append(f"(log n)^{log_power}")

    return "O(" + " ".join(parts) + ")"
