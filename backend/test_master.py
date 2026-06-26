from analyzers.master_theorem import (
    solve_master_theorem,
    master_report
)

recurrence = {
    "a":4,
    "b":2,
    "work":{
        "n_power":1,
        "log_power":0
    }
}

solve_master_theorem(
    recurrence
)

print(
    master_report(
        recurrence
    )
)