import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0
k = 2.0
b = 0.5

t = np.linspace(0, 20, 1000)
dt = t[1] - t[0]

x = np.zeros(len(t))
v = np.zeros(len(t))

x[0] = 1.0
v[0] = 0.0

for i in range(len(t)-1):
    a = -(b/m)*v[i] - (k/m)*x[i]
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i]*dt

plt.plot(t, x)
plt.title("Damped Harmonic Oscillator")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.grid()
plt.show()
