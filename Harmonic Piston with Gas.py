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
plt.figure('A harmonic piston')
plt.clf()
plt.gca().set_aspect('equal')
L = 2.0 #size of box along x
V = L*1 # two-dimensional volume
plt.plot(np.array([0,L,L,0,0]), np.array([0,0,1,1,0]), 'k')

#add wall
width=0.1
wall=Rectangle((1,0),width,1,color="orange")
plt.gca().add_patch(wall)
u_init=0.0#1
wall.u=u_init
M=100
omega0=2*np.pi/100
dt=1

# add molecules of gas
r = 0.01 # radius of a molecule
N = 150 # number of gas molecules
m = 1 # mass of a single molecule
v = 0.01 # absolute value of velocity
gas = [] # a list of gas molecules
xlist=[]
vlist=[]
vx_list=[]
for n in range(N):
    # choose a random location of the particles (but leave a 2r
    # margin on each side
    xstart = 0.5+0*(random.random()*(1-4*r) + 2*r)
    ystart = 0.5+0*(random.random()*(1-4*r) + 2*r)
    c = Circle((xstart,ystart),r,color='blue')
    plt.gca().add_patch(c)
    # all particles have the same v but different directions
    theta = random.random() * 2 * np.pi
    c.vx = v*np.cos(theta)
    c.vy = v*np.sin(theta)
    gas.append(c)

# define a function that moves particles one step
def move(i):
    old_x,old_y=wall.xy
    x = old_x
    # move the molecules
    for n in range(N):
        c = gas[n]
        currentx, currenty = c.center
        if (currentx + c.vx > x) or (currentx + c.vx < 0):
            if (currentx + c.vx > x):
                # if we hit the right wall: add the momentum kick
                old_vx=c.vx
                old_u=wall.u
                new_vx=-old_vx*(1-(m/M))/(1+(m/M))+2*old_u*1/(1+m/M)
                new_u=old_u*(1-(m/M))/(1+(m/M))+2*old_vx*(m/M)/(1+m/M)
                wall.u=new_u
                c.vx=new_vx
                hits.append(2*m*c.vx)
            else:    
                c.vx = -c.vx
        if (currenty + c.vy > 1) or (currenty + c.vy < 0):
            c.vy = -c.vy
        c.center = currentx+c.vx, currenty+c.vy
    vx_list.append(np.mean([(0.5*m*c.vx**2) for c in gas]))
    # move the wall
    old_x,old_y=wall.xy
    old_u=wall.u
    new_x=old_x+dt*old_u
    new_u=old_u+dt*(-(omega0**2)*(new_x-1))
    wall.xy=new_x,old_y
    wall.u=new_u
    xlist.append(new_x)
    vlist.append((old_u+new_u)/2)
   
# now iterate
i = 0 # descrete time (start at t=0)
max_iterations = 500 # end of time
hits = [] #list of coliisions on the right wall
show = True
while (i<max_iterations):
    move(i)
    if show:
        plt.pause(0.001) # add a little pause to update monitor
                     # but if you want a faster simulation, comment 
                     # this out
    update_progress(i/max_iterations)
    i=i+1 # time moves forward

# Summarry plot
xlist=np.array(xlist)
vlist=np.array(vlist)
vx_list=np.array(vx_list)
plt.figure("Summary")
plt.subplot(3,1,1)
plt.xlabel("time")
plt.ylabel("X position")
plt.plot(xlist)
plt.subplot(3,1,2)
plt.plot(vlist)
plt.xlabel("time")
plt.ylabel("velocity")
plt.subplot(3,1,3)
plt.plot(0.5*M*vlist**2+0.5*M*omega0**2*(xlist-1)**2)
plt.plot(N*vx_list)
plt.plot(n*vx_list+0.5*M*vlist**2+0.5*M*omega0**2*(xlist-1)**2,"k--")
plt.ylim(0,0.02)
plt.xlabel("time")
plt.ylabel("Energy")
plt.show()