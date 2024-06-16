import numpy as np # the power of vectors and matrices
import matplotlib.pyplot as plt # the power of graphs
from matplotlib.patches import Rectangle

m=1
M=100
wall=Rectangle((0,0.02),0.02,1, color="brown")
ground=Rectangle((0,0),1,0.02,color="green")
big=Rectangle((0.7,0.02),0.1,0.1,color="blue")
little=Rectangle((0.3,0.02),0.1,0.1,color="red")
big.vx=-0.01
little.vx=0
collisions=0
tot_energy=0.5*m*little.vx**2+0.5*M*big.vx**2
tot_momentum=m*little.vx+M*big.vx
plt.gca().add_patch(wall)
plt.gca().add_patch(ground)
plt.gca().add_patch(big)
plt.gca().add_patch(little)
def end():
    return 0<little.vx<big.vx
def collide_masses():
    # print("energy before",0.5*m*little.vx**2+0.5*M*big.vx**2, tot_energy)
    # print("momentum before", m*little.vx+M*big.vx,tot_momentum)
    global collisions
    collisions+=1
    little.vx=(tot_momentum*m-np.sqrt(m*M*(2*tot_energy*m+2*tot_energy*M-tot_momentum**2)))/(m**2+m*M)
    big.vx=(tot_momentum*M+np.sqrt(m*M*(2*tot_energy*m+2*tot_energy*M-tot_momentum**2)))/(M**2+m*M)
    little.vx=np.round(little.vx,decimals=6)
    big.vx=np.round(big.vx,decimals=6)
    # print("momentum before", m*little.vx+M*big.vx,tot_momentum)
    # print("energy after",0.5*m*little.vx**2+0.5*M*big.vx**2, tot_energy)
def bounce_little():
    little.vx=-little.vx
    global tot_momentum, collisions
    tot_momentum=m*little.vx+M*big.vx
    collisions+=1
def update():
    big.set_x(big.get_x()+big.vx)
    little.set_x(little.get_x()+little.vx)
    left_big=big.get_center()[0]-0.5*big.get_width()
    right_little=little.get_center()[0]+0.5*little.get_width()
    left_little=little.get_center()[0]-0.5*little.get_width()
    if abs(left_big-right_little)<=max(little.vx,big.vx):
        print(right_little+little.vx,left_big+big.vx)
        collide_masses()
        print((little.vx,big.vx))
    elif (left_little+little.vx-0.02)<=0.0001:
        print(left_little)
        bounce_little()
        print((little.vx,big.vx))

def draw():
    plt.gca().add_patch(wall)
    plt.gca().add_patch(ground)
    plt.gca().add_patch(big)
    plt.gca().add_patch(little)
while(not end()):
    update()
    draw()
    plt.pause(0.01)
print(collisions)