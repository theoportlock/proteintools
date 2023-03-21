#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')
df = pd.read_csv("coords.csv")

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#sampled = df.sample(n=1000)
sampled = df
ax.scatter(sampled['x'], sampled['y'], sampled['z'],s=0.1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_axis_off()

plt.show()
#plt.savefig("pointcloud.svg")
