def complexity_to_string(n_power, log_power):

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

    if n_power == 0 and log_power == 0:
        return "O(1)"

    parts = []

    if n_power > 0:

        if n_power == 1:
            parts.append("n")
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