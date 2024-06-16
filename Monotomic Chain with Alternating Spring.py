# This simulation shows the motion of a diatomic chain of atoms with the same 
# different spring constants between them. This plays an important role in
# condensed matter physics

# import tools (that makes it look like you have MATLAB)
import numpy as np # the power of vectors and matrices
import matplotlib.pyplot as plt # the power of graphs
from matplotlib.patches import Circle
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

plt.figure("Diatomic Chain")
plt.clf()
plt.gca().set_aspect('equal')

m1=1
m2=1    
a=0.25 # Distance between atoms at equilibrium
M0_eq=0
M1_eq=M0_eq+a
M2_eq=M1_eq+a
M3_eq=M2_eq+a
M4_eq=M3_eq+a
k1=0.5
k2=0.25
M1=Circle((M1_eq,0.5),0.05*m1,color="blue")
plt.gca().add_patch(M1)
M2=Circle((M2_eq+0.05,0.5),0.05*m2,color="red")
plt.gca().add_patch(M2)
M0=Circle((M0_eq,0.5),0.05*m2,color="red")
plt.gca().add_patch(M0)
M3=Circle((M3_eq-0.08,0.5),0.05*m1,color="blue")
plt.gca().add_patch(M3)
M4=Circle((M4_eq,0.5),0.05*m2,color="red")
plt.gca().add_patch(M4)
M0.v,M1.v,M2.v, M3.v,M4.v=0,0,0,0,0
x_locs_eq=[[],[],[]]
x_locs=[[],[],[]]
# M1.center=(0.25,0.25)
def update():
    # TODO: Correct the equations here:
    # f_M1=-(1/m1)*(k1*(M1.center[0]-M2.center[0]-a)-k2*(M0.center[0]-M1.center[0]-a))
    # f_M2=-(1/m2)*(k2*(M2.center[0]-M3.center[0]-a)-k1*(M1.center[0]-M2.center[0]-a))
    # f_M3=-(1/m1)*(k1*(M3.center[0]-M4.center[0]-a)-k2*(M2.center[0]-M3.center[0]-a))
    # M1.v+=f_M1*0.01
    # M2.v+=f_M2*0.01
    # M3.v+=f_M3*0.01
    # print(f_M1,f_M2,f_M3)
    # M1.center=(M1.center[0]+M1.v,M1.center[1])
    # M2.center=(M2.center[0]+M2.v,M2.center[1])
    # M3.center=(M3.center[0]+M3.v,M3.center[1])
    x_locs_eq[0].append(M1.center[0]-M1_eq)
    x_locs_eq[1].append(M2.center[0]-M2_eq)
    x_locs_eq[2].append(M3.center[0]-M3_eq)
    x_locs[0].append(M1.center[0])
    x_locs[1].append(M2.center[0])
    x_locs[2].append(M3.center[0])
t=0
max_time=1000
while(t<max_time):
    update()
    plt.pause(0.005)
    t+=1
    update_progress(t/max_time)
    # if t>1: break
plt.show()
plt.figure()
# print(x_locs[0])
plt.plot(x_locs_eq[0])
plt.plot(x_locs_eq[1])
plt.plot(x_locs_eq[2])
plt.legend(["M1", "M2", "M3"])
plt.title("Distance Away from Equilibrium Point")
plt.show()
plt.figure()
plt.plot(x_locs[0])
plt.plot(x_locs[1])
plt.plot(x_locs[2])
plt.legend(["M1", "M2", "M3"])
plt.title("Position as a function of time")
plt.show()