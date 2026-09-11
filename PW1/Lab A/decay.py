import numpy as np

def simulate(n0, rate, steps=10):
    return [n0 * ((1 - rate) ** i) for i in range(steps)]
