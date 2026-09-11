import time
import decay

n_atoms = 200000
decay_rate = 0.4
steps = 10

# Pure Python loop
t0 = time.perf_counter()
res_py = decay.simulate_loop(n_atoms, decay_rate, steps)
t_py = time.perf_counter() - t0

# NumPy vectorised
t0 = time.perf_counter()
res_np = decay.simulate(n_atoms, decay_rate, steps)
t_np = time.perf_counter() - t0

speedup = t_py / t_np if t_np > 0 else 0

print(f"Pure-Python loop time: {t_py:.4f} s")
print(f"NumPy vectorised time: {t_np:.4f} s")
print(f"NumPy is {speedup:.2f}x faster than pure-Python")
