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



from math import log

from complex_utils import complexity_to_string
from analyzers.master_theorem import determine_case


SUBSCRIPT = str.maketrans(
    "0123456789",
    "₀₁₂₃₄₅₆₇₈₉"
)


def detailed_master_report(recurrence, result):

    a = recurrence["a"]
    b = recurrence["b"]
    work = recurrence["work"]

    work_string = complexity_to_string(
        work["n_power"],
        work["log_power"]
    )

    result_string = complexity_to_string(
        result["n_power"],
        result["log_power"]
    )

    case = determine_case(recurrence)

    base = str(b).translate(SUBSCRIPT)

    exponent = log(a, b)

    if abs(exponent) < 1e-9:
        exponent_text = "0"
    elif abs(exponent - round(exponent)) < 1e-9:
        exponent_text = str(int(round(exponent)))
    else:
        exponent_text = f"{exponent:.2f}"

    if a == 1:
        recurrence_string = (
            f"T(n) = T(n/{b}) + {work_string}"
        )
    else:
        recurrence_string = (
            f"T(n) = {a}T(n/{b}) + {work_string}"
        )

    lines = [

        "Master Theorem Analysis",
        "------------------------",

        f"Recurrence : {recurrence_string}",
        "",

        "Constants",
        f"  a = {a}",
        f"  b = {b}",
        f"  f(n) = {work_string}",
        "",

        "Comparison",
        f"  log{base}({a}) = {exponent_text}",
        f"  n^log{base}({a}) = O(n^{exponent_text})",
        "",

    ]

    if case == 1:

        lines.extend([
            "Observation",
            f"  {work_string} grows slower than O(n^{exponent_text}).",
            "",
            "Master Theorem Case 1",
        ])

    elif case == 2:

        lines.extend([
            "Observation",
            f"  {work_string} matches O(n^{exponent_text}).",
            "",
            "Master Theorem Case 2",
        ])

    else:

        lines.extend([
            "Observation",
            f"  {work_string} grows faster than O(n^{exponent_text}).",
            "",
            "Master Theorem Case 3",
        ])

    lines.extend([
        "",
        f"Final Complexity : {result_string}"
    ])

    return "\n".join(lines)

