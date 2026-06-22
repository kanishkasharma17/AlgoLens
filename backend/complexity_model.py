from complex_utils import complexity_to_string

def make_complexity(
    n_power=0,
    log_power=0
):
    return {
        "n_power": n_power,
        "log_power": log_power
    }
def multiply(a,b):

    return {
        "n_power":
            a["n_power"]
            + b["n_power"],

        "log_power":
            a["log_power"]
            + b["log_power"]
    }
def add(a,b):

    if a["n_power"] > b["n_power"]:
        return a

    if b["n_power"] > a["n_power"]:
        return b

    if a["log_power"] > b["log_power"]:
        return a

    return b

