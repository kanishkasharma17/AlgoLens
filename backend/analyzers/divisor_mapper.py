def divisor_from_argument(argument_type):

    mapping = {

        "HALF": 2,
        "MID": 2,

        "THIRD": 3,

        "LEFT": 2,
        "RIGHT": 2,

    }

    return mapping.get(argument_type)