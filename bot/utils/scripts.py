import bisect


def calculate_spin_multiplier(spins):
    variables = [0]
    idx = bisect.bisect_right(variables, spins) - 1

    return variables[idx] if idx >= 0 else 1
