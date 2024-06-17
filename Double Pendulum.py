import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.81  # acceleration due to gravity, in m/s^2
l1 = 1.0  # length of the first pendulum rod (in meters)
l2 = 1.0  # length of the second pendulum rod (in meters)
m1 = 1.0  # mass of the first pendulum bob (in kg)
m2 = 1.0  # mass of the second pendulum bob (in kg)

# Initial conditions
a1 = np.pi / 2  # initial angle of the first pendulum (in radians)
a2 = np.pi / 2  # initial angle of the second pendulum (in radians)
a1_v = 0.0  # initial angular velocity of the first pendulum (in rad/s)
a2_v = 0.0  # initial angular velocity of the second pendulum (in rad/s)

# Time parameters
dt = 0.01  # time step (in seconds)
t_max = 20  # total time (in seconds)
t = np.arange(0, t_max, dt)

# Arrays to store the positions of the pendulum bobs
x1 = np.zeros_like(t)
y1 = np.zeros_like(t)
x2 = np.zeros_like(t)
y2 = np.zeros_like(t)

def update_pendulum(a1, a2, a1_v, a2_v, dt):
    num1 = -g * (2 * m1 + m2) * np.sin(a1)
    num2 = -m2 * g * np.sin(a1 - 2 * a2)
    num3 = -2 * np.sin(a1 - a2) * m2
    num4 = a2_v**2 * l2 + a1_v**2 * l1 * np.cos(a1 - a2)
    den = l1 * (2 * m1 + m2 - m2 * np.cos(2 * a1 - 2 * a2))
    a1_a = (num1 + num2 + num3 * num4) / den

    num1 = 2 * np.sin(a1 - a2)
    num2 = a1_v**2 * l1 * (m1 + m2)
    num3 = g * (m1 + m2) * np.cos(a1)
    num4 = a2_v**2 * l2 * m2 * np.cos(a1 - a2)
    den = l2 * (2 * m1 + m2 - m2 * np.cos(2 * a1 - 2 * a2))
    a2_a = (num1 * (num2 + num3 + num4)) / den

    a1_v += a1_a * dt
    a2_v += a2_a * dt
    a1 += a1_v * dt
    a2 += a2_v * dt

    return a1, a2, a1_v, a2_v

# Update positions of the pendulum bobs
for i in range(len(t)):
    x1[i] = l1 * np.sin(a1)
    y1[i] = -l1 * np.cos(a1)
    x2[i] = x1[i] + l2 * np.sin(a2)
    y2[i] = y1[i] - l2 * np.cos(a2)
    a1, a2, a1_v, a2_v = update_pendulum(a1, a2, a1_v, a2_v, dt)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-', lw=2)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True, init_func=init)

plt.show()
