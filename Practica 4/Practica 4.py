import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Bar
def bar(y,x,title, save):
    positions = range(len(y))
    plt.bar(positions, y)
    plt.xticks(positions, x)
    plt.title(title)    
    plt.savefig(save)
    plt.clf()
    
#Pie
def pie(value,label,title,save):
    colores=["#2d27a3","#eb4034"]
    plt.pie(value, labels=label, autopct="%0.1f %%", colors=colores)
    plt.title(title)
    plt.savefig(save)
    plt.clf()
    
#Scatter
def scatter(x,y,color,title,save):
    plt.scatter(x,y, c=color, edgecolors='black', linewidths=1, alpha=0.75)
    plt.title(title)
    plt.savefig(save)
    plt.clf()
    
#Boxplot
def boxplot(values,title, save):
    plt.boxplot(x=values, labels=["Win blue gold", "Lose blue gold", "Win red gold", "Lose red gold"])
    plt.title(title)
    plt.savefig(save)
    plt.clf()

#Win rate per objective
def winRateObj(df):
    #Num de victorias y Num de partidas totales
    winD, winH, winB, winTB = 0, 0, 0, 0
    totalD, totalH, totalB, totalT = 0, 0, 0, 0

    for data in df.values:
        #Si un equipo se hizo solo el dragon
        if(data[2]!='No one' and data[3]!=data[2]):
            if(data[0] == data[2]):
                winD += 1
            totalD += 1
        #Si un equipo se hizo solo el heraldo
        elif(data[2]!=data[3] and data[3]!='No one'):
            if(data[0] == data[3]):
                winH += 1
            totalH += 1
        #Si un equipo hizo ambos objetivos
        elif(data[2]!='No one' and data[2]==data[3]):
            if(data[0] == data[2]):
                winB += 1
            totalB += 1
        else:
            if(data[0]=='Blue'):
                winTB += 1
            totalT += 1

    winD = winD/totalD
    winH = winH/totalH
    winB = winB/totalB
    winTB = winTB/totalT
    winTR = 1 - winTB
    
    return [winD, winH, winB, winTB, winTR]

#Objective distribution
def objDist(df):
    bH, bD, rH, rD = 0, 0, 0, 0
    totalD, totalH = 0,0
    
    for data in df.values:
        if(data[2]=='Blue'):
            bD += 1
            totalD +=1
        elif(data[2]=='Red'):
            rD += 1
            totalD +=1

        if(data[3]=='Blue'):
            bH += 1
            totalH +=1
        elif(data[3]=='Red'):
            rH += 1
            totalH +=1
            
    bH = bH/totalH
    bD = bD/totalD
    rH = rH/totalH
    rD = rD/totalD
    return [[bD, rD],[bH, rH]]
#Gold Exp distribution
def goldExpDist(df):
    gB = []
    gR = []
    eB = []
    eR = []
    
    for data in df.values:
        gB.append(data[9])
        eB.append(data[10])
        gR.append(data[18])
        eR.append(data[19])
        
    return [gB, eB, gR, eR]

#Gold comparison
def goldComp(df):
    wbg = []
    lbg = []
    wrg = []
    lrg = []
    for data in df.values:
        if(data[0]=='Blue'):
            wbg.append(data[9])
            lrg.append(data[18])
        else:
            lbg.append(data[9])
            wrg.append(data[18])
        
    return [wbg,lbg,wrg,lrg]
#Frist Blood distribution
def firstB(df):
    fbB, fbR, fbW = 0, 0, 0
    n = len(df.index)
    for data in df.values:
        if(data[1]=='Blue'):
            if(data[0]==data[1]):
                fbW += 1
            fbB +=1
        else:
            fbR += 1
            if(data[0]==data[1]):
                fbW += 1
    fbB = fbB/n
    fbR = fbR/n
    fbW = fbW/n

    return [fbB, fbR, fbW]
#Read csv
df = pd.read_csv("../Practica 2/cleaned_rankedGames.csv")
#Grafica 1
wrObj = winRateObj(df)
bar(wrObj, ['Dragon','Heraldo','Ambos','Blue - Sin', 'Red - Sin'], "Win Rate por objetivos", "Bar_Objetivos.png")
#Grafica 2 y 3
oDist = objDist(df)
pie(oDist[0],["Blue","Red"], "Distribucion de Dragones", "Pie_Dragones.png")
pie(oDist[1], ["Blue","Red"], "Distribucion de Heraldo", "Pie_Heraldos.png")
#Grafica 4 y 5
geDist = goldExpDist(df)
scatter(geDist[0],geDist[1],"#2d27a3","Distribucion Oro - Exp", "Scatter_OroExpBlue.png")
scatter(geDist[2],geDist[3],"#eb4034","Distribucion Oro - Exp", "Scatter_OroExpRed.png")
#Grafica 6
gold = goldComp(df)
boxplot(gold, "Distribucion de Oro", "Boxplot_Oro.png")
#Grafica 7
fb = firstB(df)
bar(fb,["F.B. - Blue", "F.B. - Red","F.B. Win rate"], "First Blood", "Bar_FirstBlood.png")
