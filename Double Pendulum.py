#! python3

# import tools (that makes it look like you have MATLAB)
import numpy as np # the power of vectors and matrices
import matplotlib.pyplot as plt # the power of graphs
from matplotlib.patches import Circle, Rectangle
import random # random number generators
import sys # for the progress bar

# define a progress bar
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


# Build a world
fig=plt.figure('A double pendulum experiment')
ax=fig.add_subplot(1,1,1)

ax.cla()
ax.set_aspect('equal')
L = 1.0 #size of box along x
V = L*1 # two-dimensional volume
ax.plot(np.array([0,L,L,0,0]), np.array([0,0,1,1,0]), 'k')

m1_dic={
    "loc":(0.55,0.75),
    "mass":1,
    "color":"blue"
}
m2_dic={
    "loc":(0.45,0.5),
    "mass":2,
    "color":"red"
}
def draw():
    m1=Circle(m1_dic["loc"],0.01*m1_dic["mass"],color=m1_dic["color"])
    ax.add_patch(m1)
    m2=Circle(m2_dic["loc"],0.01*m2_dic["mass"],color=m2_dic["color"])
    ax.add_patch(m2)
    ax.plot(np.array([0.5,m1_dic["loc"][0]]),np.array([1,m1_dic["loc"][1]]),color="green")
    ax.plot(np.array([m1_dic["loc"][0],m2_dic["loc"][0]]),np.array([m1_dic["loc"][1],m2_dic["loc"][1]]),color="green")
def move():
    # m_{2}l_{2}\ddot{\theta}_2+m_{2}l_{1}\ddot{\theta}_1\cos\left(\theta_{1}-\theta_{2}\right)
    # -m_{2}l_{1}\dot{\theta}_{1}^{2}\sin\left(\theta_{1}-\theta_{2}\right)+m_{2}g\sin\left(\theta_{2}\right)=0
    
    # \left(m_{1}+m_{2}\right)l_{1}^{2}\ddot{\theta}_{1}+m_{2}l_{2}^{2}\ddot{\theta}_{2}\cos\left(\theta_{1}-\theta_{2}\right)+
    # +m_{2}l_{1}l_{2}\dot{\theta}_{2}^{2}\sin\left(\theta_{1}-\theta_{2}\right)+
    # +\left(m_{1}+m_{2}\right)l_{1}g\sin\left(\theta_{1}\right)=0

    # Use SciPy to solve it
    t=np.linspace(0,100)
    

    pass
t=0
dt=1
end_time=10
while t<end_time:
    t+=dt
    move()
    draw()
plt.show()
