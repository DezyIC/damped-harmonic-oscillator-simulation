import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0      # mass
k = 2.0      # spring constant
b = 0.5      # damping coefficient

# Time settings
t = np.linspace(0, 20, 1000)
dt = t[1] - t[0]

# Initial conditions
x = np.zeros(len(t))
v = np.zeros(len(t))

x[0] = 1.0   # initial displacement
v[0] = 0.0   # initial velocity

# Euler method
for i in range(len(t) - 1):
    a = -(b/m)*v[i] - (k/m)*x[i]
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i] * dt

# Plot result
plt.figure()
plt.plot(t, x)
plt.title("Damped Harmonic Oscillator")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.grid()

# Save image (for GitHub)
plt.savefig("output.png")

plt.show()
