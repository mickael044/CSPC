import numpy as np

def simulate(n0, rate, steps=10):
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    return [n0 * ((1 - rate) ** i) for i in range(steps)]

def simulate_loop(n0, rate, steps=10):
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    res = [n0]
    curr = n0
    for _ in range(1, steps):
        curr = curr * (1 - rate)
        res.append(curr)
    return res
