import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
P0 = 200000  # Initial tank pressure, Pa
V = 0.003  # Tank volume, m^3
P_ambient = 101325  # Ambient pressure, Pa
R = 5000000  # Flow resistance, Pa.s/m^3 (chosen for illustrative purposes)


# ODE
def dPdt(P, t):
    return -(P - P_ambient) / (R * V)

# Time array for simulation
t = np.linspace(0, 2, 1000)  # From 0 to 2 seconds, 1000 points in time

# Solve ODE
P = odeint(dPdt, P0, t)

# Calculate flow rate Q
Q = (P - P_ambient) / R

# Plot results
plt.figure()

plt.subplot(211)
plt.plot(t, P / 1e5)  # Pressure in bar
plt.xlabel('Time [s]')
plt.ylabel('Pressure [bar]')

plt.subplot(212)
plt.plot(t, Q * 1e6)  # Flow rate in L/s
plt.xlabel('Time [s]')
plt.ylabel('Flow rate [L/s]')

plt.tight_layout()
plt.show()
