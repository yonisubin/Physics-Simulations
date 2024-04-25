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
plt.figure("Simple Harmonic oscillator simulation")
resting_point=(0.5,1-0.5)
origin=(0.5,1)
L=0.5
theta_0=np.pi/3
theta=theta_0
M=1
g=1
mass_point=[origin[0]+L*np.sin(theta),origin[1]-L*np.cos(theta)]
r=Rectangle(origin,width=0.001,height=-L,angle=theta*57.2958,color="red")
# s=[origin,point]
m=Circle(mass_point,0.01,color="blue")
# plt.gca().set_aspect("equal")
def plot_objects():
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.gca().add_patch(r)
    plt.gca().add_patch(m)
t=0
time=10
velosity=[]
position=[]
while t<time:
    t+=1/3
    theta=theta_0*np.cos(np.sqrt(L/g)*t)
    dtheta=-theta_0*np.sqrt(L/g)*np.sin(np.sqrt(L/g)*t)
    mass_point=[origin[0]+L*np.sin(theta),origin[1]-L*np.cos(theta)]
    m.center=mass_point
    r.set_angle(theta*57.2958)
    plot_objects()
    velosity.append(L*dtheta)
    position.append(origin[1]-m.center[1])
    plt.pause(0.001)
    update_progress(t/time)

plt.show()
plt.figure()
plt.plot(0.5*M*np.array(velosity)**2)
# plt.plot(M*g*np.array(position))
# plt.plot(0.5*M*np.array(velosity)**2+M*g*np.array(position),"k--")
plt.show()