def complexity_to_string(
    complexity_or_n,
    log_power=None,
    complexity_type=None
):
    if isinstance(complexity_or_n, dict):

        complexity = complexity_or_n

        if complexity["family"] == EXPONENTIAL:
            return "O(2ⁿ)"

        n_power = complexity["n_power"]
        log_power = complexity["log_power"]

    else:

        n_power = complexity_or_n

        if complexity_type == EXPONENTIAL:
            return "O(2ⁿ)"
    superscripts = {
        0: "⁰",
        1: "¹",
        2: "²",
        3: "³",
        4: "⁴",
        5: "⁵",
        6: "⁶",
        7: "⁷",
        8: "⁸",
        9: "⁹"
    }
    def to_superscript(num):
        return "".join(
            superscripts[int(d)]
            for d in str(num)
        )
    if complexity_type == EXPONENTIAL:
        return "O(2ⁿ)"
    
    if n_power == 0 and log_power == 0:
        return "O(1)"

    parts = []

    if n_power > 0:

        if isinstance(n_power, float):

            if n_power.is_integer():
                n_power = int(n_power)

        if n_power == 1:
            parts.append("n")

        elif isinstance(n_power, float):

            parts.append(f"n^{n_power:.2f}".rstrip("0").rstrip("."))

        else:

            parts.append(
            f"n{to_superscript(n_power)}"
        )

    if log_power > 0:

        if log_power == 1:
            parts.append("log n")
        else:
            parts.append(
                f"log{to_superscript(log_power)} n"
            )

    return "O(" + " ".join(parts) + ")"

CONSTANT = "CONSTANT"
LOG = "LOG"
LINEAR = "LINEAR"
N_LOG_N = "N_LOG_N"
POLYNOMIAL = "POLYNOMIAL"
EXPONENTIAL = "EXPONENTIAL"

def classify_complexity(
    n_power,
    log_power,
    recursion_type=None
):

    if recursion_type == "BINARY":
        return EXPONENTIAL

    if n_power == 0 and log_power == 0:
        return CONSTANT

    if n_power == 0 and log_power == 1:
        return LOG

    if n_power == 1 and log_power == 0:
        return LINEAR

    if n_power == 1 and log_power == 1:
        return N_LOG_N

    return POLYNOMIAL

def make_complexity(
    family="POLYNOMIAL",
    n_power=0,
    log_power=0,
    base=None
):
    return {
        "family": family,
        "n_power": n_power,
        "log_power": log_power,
        "base": base
    }