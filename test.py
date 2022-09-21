import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import pandas as pd

viewers_data = pd.read_excel('new_data.xlsx')

c_indices = {}
c_x = {}
c_y = {}
c_z = {}
colors = ['r', 'g', 'b', 'black']
for i in range(4):
    c_indices[i] = viewers_data.index[viewers_data['result']==i].tolist()
    c_x[i] = []
    c_y[i] = []
    c_z[i] = []
    for index in c_indices[i]:
        c_x[i].append(viewers_data['70'][index])
        c_y[i].append(viewers_data['90'][index])
        c_z[i].append(viewers_data['95'][index])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.text2D(0.05, 0.95, "Class " + str(i), transform=ax.transAxes)
    ax.set_xlabel('70%', fontsize=16, labelpad=15)
    ax.set_ylabel('90%', fontsize=16, labelpad=15)
    ax.set_zlabel('95%', fontsize=16, labelpad=15)
    color = random.choice(colors)
    colors.remove(color)
    ax.scatter(c_x[i], c_y[i], c_z[i], c=color)
    plt.show()

