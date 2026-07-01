import math

from complex_utils import (
    make_complexity,
    complexity_to_string
)


def solve_master_theorem(recurrence):

    if recurrence is None:
        return None

    a = recurrence["a"]
    b = recurrence["b"]

    work = recurrence["work"]

    log_value = math.log(a, b)

    recurrence["log_ab"] = log_value

    return recurrence

def determine_case(recurrence):

    if recurrence is None:
        return None

    work = recurrence["work"]

    log_ab = recurrence["log_ab"]

    work_power = work["n_power"]

    if work_power < log_ab:
        return 1

    if abs(work_power - log_ab) < 0.01:
        return 2

    return 3


def solve_complexity(recurrence):

    case = determine_case(
        recurrence
    )

    if case == 1:

        exponent = round(
            recurrence["log_ab"]
        )

        return make_complexity(
            n_power=exponent
        )

    if case == 2:

        exponent = round(
            recurrence["log_ab"]
        )

        return make_complexity(
            n_power=exponent,
            log_power=1
        )

    return recurrence["work"]


def master_report(recurrence):

    if recurrence is None:
        return "Not Applicable"

    case = determine_case(
        recurrence
    )

    result = solve_complexity(
        recurrence
    )

    return (
        f"Master Theorem Case {case}\n"
        f"{complexity_to_string(result['n_power'], result['log_power'])}"
    )


def subscript(text):

    table = str.maketrans(
        "0123456789",
        "₀₁₂₃₄₅₆₇₈₉"
    )

    return text.translate(table)

def pretty_number(x):

    if float(x).is_integer():
        return str(int(x))

    return str(round(x, 2))


from math import log

from complex_utils import complexity_to_string


def theta_string(n_power, log_power):

    if n_power == 0 and log_power == 0:
        return "Θ(1)"

    if n_power == 1 and log_power == 0:
        return "Θ(n)"

    if n_power == 1 and log_power == 1:
        return "Θ(n log n)"

    if n_power == 0 and log_power == 1:
        return "Θ(log n)"

    if log_power == 0:
        return f"Θ(n^{n_power})"

    return f"Θ(n^{n_power} log^{log_power} n)"

def section(title):
    return f"{title}\n{'-' * len(title)}"

def detailed_master_report(rec, result):

    a = rec["a"]
    b = rec["b"]
    work = rec["work"]

    exponent = log(a, b)

    exp_text = pretty_number(exponent)

    recurrence = (
        f"T(n) = "
        f"{'' if a == 1 else str(a)}"
        f"T(n/{b}) + "
        f"{theta_string(work['n_power'], work['log_power'])}"
    )

    report = []

    report.append(section("Master Theorem Analysis"))
    
    report.append("")

    report.append(section("General Form"))
    report.append("T(n) = aT(n/b) + f(n)")
    report.append("")

    report.append(section("Detected Recurrence"))
    
    report.append(recurrence)
    report.append("")

    report.append(section("Constants"))
    
    report.append(f"a = {a}")
    report.append(f"b = {b}")
    report.append(f"f(n) = {theta_string(work['n_power'], work['log_power'])}")
    report.append("")

    report.append(section("Comparison"))
    
    report.append(f"log{subscript(str(b))}(a) = log{subscript(str(b))}({a}) = {exp_text}")
    report.append("")
    if exponent == 0:
        theta = "Θ(1)"
    elif exponent == 1:
        theta = "Θ(n)"
    else:
        theta = f"Θ(n^{exp_text})"
    report.append(f"n^(log{subscript(str(b))}a) = {theta}")
    report.append("")


    report.append(section("Observation"))
    

    report.append(
    f"f(n) = {theta_string(work['n_power'], work['log_power'])}"
    )
    report.append("")

    report.append(
    f"n^(log{subscript(str(b))}a) = {theta}"
)
    report.append("")

    report.append(
    f"Since both growth rates are equal,\n"
    f"Master Theorem Case {determine_case(rec)} applies."
)
    report.append("")

    report.append(section("Solved Recurrence"))
    
    report.append(
        f"T(n) = {theta_string(result['n_power'], result['log_power'])}"
    )
    report.append("")

    report.append(section("Final Complexity"))
    
    report.append(
        complexity_to_string(
            result["n_power"],
            result["log_power"]
        )
    )

    return "\n".join(report)