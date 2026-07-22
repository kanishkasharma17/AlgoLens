from complex_utils import complexity_to_string


def section(title):

    return (
        title +
        "\n" +
        "-" * len(title)
    )


def detailed_dp_report(result):

    report = []

    report.append(section("Dynamic Programming Analysis"))
    report.append("")

    report.append(section("Recursive Pattern"))
    report.append("Top-down Dynamic Programming (Memoization)")
    report.append("")

    report.append(section("Technique"))
    report.append("Dynamic Programming")
    report.append("")

    report.append(section("Master Theorem"))
    report.append("Not Applicable")
    report.append("")

    report.append(section("Reason"))
    report.append(
        "The recursive function stores previously computed subproblems.\n"
        "Repeated states are evaluated only once.\n\n"
        "Since the recursion does not follow the form\n\n"
        "T(n) = aT(n/b) + f(n),\n\n"
        "the Master Theorem is not applicable."
    )
    report.append("")

    report.append(section("Estimated Complexity"))
    report.append(
        complexity_to_string(
            result["n_power"],
            result["log_power"]
        )
    )

    return "\n".join(report)