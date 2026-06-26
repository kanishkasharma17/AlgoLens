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