# CSPC Project
## PW2 -- Lab A Report

### Results
- **Mean Acceleration:** -8.58 m/s²
- **Standard Deviation (Noise):** 28.72
- **Maximum Recovery Difference:** 0.7846 m

### Why is acceleration so noisy while position looks smooth?
Differentiation acts as a high-pass filter that magnifies high-frequency noise present in the original measurements. Taking the derivative twice amplifies this noise significantly, making acceleration look very rough, even though the original position data appears visually smooth.

### Integration Result
Integrating the noisy acceleration back suppresses the noise (integration cancels out random variations) and successfully recovers the original position within less than a metre of accuracy (0.78 m).