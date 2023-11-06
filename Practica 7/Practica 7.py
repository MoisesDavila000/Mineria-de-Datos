import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import mode
from collections import Counter

##Obtener puntos X (Oro), Y (Exp) y grupos, crear nuevo df
##Agrupacion de ORO-EXP dependiendo del desempeño en Micro (Kills, Farms) cuando gana un equipo - Se ignoran los objetivos (Torres, Monstruos de la Jungla)
def get_points(df, labels, x, y,team=None, obj=False):
    new_x = []
    new_y = []
    label = []
    for data in df.values:
        if(data[0]==team and data[2]=="No one" and data[3]=="No one" and data[11]<=210 and data[6]<=7 and data[8]==0):
            new_x.append(data[x])
            new_y.append(data[y])
            label.append(labels[0])
        elif(data[0]==team and data[2]=="No one" and data[3]=="No one" and data[11]>=210 and data[6]>=10 and data[8]==0):
            new_x.append(data[x])
            new_y.append(data[y])
            label.append(labels[2])
        elif(data[0]==team and data[2]=="No one" and data[3]=="No one"and data[8]==0):
            new_x.append(data[x])
            new_y.append(data[y])
            label.append(labels[1])
            
    data = {'Gold': new_x, 'Exp': new_y, 'Group': label}
    new_df = pd.DataFrame(data)
    return new_df

def scatter(path, df, xCol, yCol, labelCol):
    fig, ax = plt.subplots()
    labels = pd.unique(df[labelCol])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{labelCol} == '{label}'")
        ax.scatter(filter_df[xCol], filter_df[yCol], label = label, color=cmap(i), edgecolors='black', linewidths=1, alpha=0.75)
    ax.legend()
    plt.xlabel("Oro")
    plt.ylabel("Exp")
    plt.savefig(path)
    plt.close()

def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)

def euclidean_distance(p1:np.array, p2:np.array):
    return np.sqrt(np.sum((p2-p1)**2))

def k_nearest_neightbors(dfpoints, labels, new_points, k):
    input_dinstance = [
        [euclidean_distance(new_point, point) for point in dfpoints]
        for new_point in new_points
    ] 
    points_k_nearst = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_dinstance
    ]

    count=0
    for point_nearest in points_k_nearst:
        nearest_labels=[]
        for index in point_nearest:
            nearest_labels.append(labels[index])
        print("Los datos: ", new_points[count], " son del grupo: " + Counter(nearest_labels).most_common()[0][0])
        count+=1
    
    
def get_tuples(df):
    points = []
    labels = []
    for tuples in df.itertuples(index=False, name=None):
        points.append((tuples[0], tuples[1]))
        labels.append(tuples[2])
    return points, labels

##Leer CSV
df = pd.read_csv("../Practica 2/cleaned_rankedGames.csv")
new_df = get_points(df, ["Avg-", "Avg", "Avg+"], 9, 10, "Blue", True)
scatter("Scatter.png", new_df, "Gold", "Exp", "Group")
points, labels = get_tuples(new_df)
for tuples in new_df.itertuples(index=False, name=None):
    points.append((tuples[0], tuples[1]))
    labels.append(tuples[2])
k_nearest_neightbors(points,labels,[np.array([15000, 15000]),np.array([16000, 17500]),np.array([17500, 18300]), np.array([19300, 18300]), np.array([19000, 19000])],7)

#Output:
# Los datos:  [15000 15000]  son del grupo: Avg-
# Los datos:  [16000 17500]  son del grupo: Avg
# Los datos:  [17500 18300]  son del grupo: Avg
# Los datos:  [19300 18300]  son del grupo: Avg+
# Los datos:  [19000 19000]  son del grupo: Avg+