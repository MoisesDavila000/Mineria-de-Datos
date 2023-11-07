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

def k_mean(points, k):
    DIM = len(points[0])
    N = len(points)
    clusters = k
    iterations = 15
    
    x = np.array(points)
    y = np.random.randint(0, clusters, N)
    
    mean = np.zeros((clusters, DIM))
    
    for i in range(iterations):
        for k in range(clusters):
            mean[k] = np.mean(x[y==k], axis=0)
        for j in range(N):
            dist = np.sum((mean-x[j])**2, axis=1)
            pred = np.argmin(dist)
            y[j] = pred
    
    for kl in range(clusters):
        xp = x[y==kl, 0]
        yp = x[y==kl, 1]
        plt.scatter(xp, yp)
    plt.savefig("Scatter_Kmean.png")
    plt.close()
    return mean
    
    
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
km = k_mean(points, 3)
print(km)
#Output:
# [[17058.58630952 18436.19345238]
#  [15692.65384615 17249.38888889]
#  [18732.36082474 19295.68556701]]