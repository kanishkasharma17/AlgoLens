from complex_utils import complexity_to_string


def section(title):

    return (
        title +
        "\n" +
        "-" * len(title)
    )


def detailed_tabulation_report(result):

    report = []

    report.append(section("Dynamic Programming Analysis"))
    report.append("")

    report.append(section("Dynamic Programming Strategy"))
    report.append("Bottom-up Dynamic Programming (Tabulation)")
    report.append("")

    report.append(section("Technique"))
    report.append("Dynamic Programming")
    report.append("")

    report.append(section("Master Theorem"))
    report.append("Not Applicable")
    report.append("")

    report.append(section("Reason"))
    report.append(
        "Subproblems are solved iteratively using a DP table.\n"
        "No recursive recurrence exists\n\n"
        "The Master Theorem is therefore not applicable.\n\n"
    )
    report.append("")

    report.append(section("Estimated Time Complexity"))
    report.append(
    complexity_to_string(
        result["n_power"],
        result["log_power"]
    )
)
    report.append("")

    report.append(section("Estimated Space Complexity"))
    report.append(
    complexity_to_string(
        result["n_power"],
        result["log_power"]
    )
)

    return "\n".join(report)