import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import sys
def update_progress(progress):
    barLength = 25 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\r{:2.0f}% |{}| {}".format(progress*100,'\u2588'*block + " "*(barLength-block),status)
    sys.stdout.write(text)
    sys.stdout.flush()

# Wave Equation: d^2u/dt^2 = 1/c^2 d^2u/dx^2
m=1 # mass of each particle
k=1 # spring constant between each particle
c=10 # speed of wave
L=1 # length of string
time=10 # time of simulation
w=[]
def u(x, t): # disturbance through the medium
    return 1/2*(f(x-c*t)+f(x+c*t))
def f(x):
    return np.exp(-x**2)
for t in np.arange(0,time,0.1):
    w.append([])
    for x in np.arange(0,L,0.01):
        w[-1].append(u(x,t))
for i in range(len(w)):
    plt.plot(w[i])
    plt.pause(0.01)
    update_progress(i/len(w))
plt.show()
    