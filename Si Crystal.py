import matplotlib.pyplot as plt

f=plt.figure()
ax=f.add_subplot(projection="3d")
a=1
points=[]
points.append([0,0,0])
points.append([0.5,0,0.5])
points.append([1,0,0])
points.append([0.25,0.25,0.75])
points.append([0.75,0.25,0.25])
points.append([0,0.5,0.5])
points.append([0.5,0.5,0])
points.append([0.5,1,0.5])
points.append([1,0.5,0.5])
points.append([0.25,0.75,0.25])
points.append([0.75,0.75,0.75])
points.append([0,1,0])
points.append([1,1,0])
points.append([0.5,1,0.5])

for i in range(len(points)):
    ax.scatter(points[i][0],points[i][1],points[i][2])
    ax.scatter(points[i][0]+1,points[i][1]+1,points[i][2])
    ax.scatter(points[i][0]+1,points[i][1],points[i][2]+1)
    ax.scatter(points[i][0],points[i][1]+1,points[i][2]+1)
    ax.scatter(points[i][0]+1,points[i][1],points[i][2])
    ax.scatter(points[i][0],points[i][1]+1,points[i][2])
    ax.scatter(points[i][0],points[i][1],points[i][2]+1)
    ax.scatter(points[i][0]+1,points[i][1]+1,points[i][2]+1)
plt.show()