import pandas as pd
import scipy.stats as stats

#Get Winners/Losers Gold
def Gold(df):
    wbg, lrg, lbg, wrg = [], [], [], []
    for data in df.values:
        if(data[0]=='Blue'):
            wbg.append(data[9])
            lrg.append(data[18])
        else:
            lbg.append(data[9])
            wrg.append(data[18])
    return wbg, wrg, lbg, lrg

def Objectives(df, i):
    bObjs = []
    rObjs = []
    for data in df.values:
        bObj = 0
        rObj = 0
        if(data[i]=="Blue"):
            bObj+=1
        elif(data[i]=="Red"):
            rObj+=1
        bObjs.append(bObj)
        rObjs.append(rObj)
    return bObjs, rObjs

#Anova gold - scipy
def Anova(value1, value2, value3=None, value4=None):

    if(value3 != None and value4 != None):
        F, p = stats.f_oneway(value1, value2, value3, value4)
        if(p<0.05):
            return True, F, p
        else:
            return False, F, p
                    
    #Aplicar anova a los valores de ambos equipos cuando ganan
    F, p = stats.f_oneway(value1, value2)
    if(p<0.05):
        return True, F, p
    else:
        return False, F, p
    
#Read CSV
df = pd.read_csv("../Practica 2/cleaned_rankedGames.csv")
F, p = 0, 0
wbg, wrg, lbg, lrg = Gold(df)
bDrag, rDrag = Objectives(df, 2)
bHerald, rHerald = Objectives(df, 3)

#Excecute anova 1
winnerGold, F, p = Anova(wbg, wrg)
print("Valor F: ", F, ". Valor p: ", p)
Output = "Hay diferencia entre el oro de los equipos cuando ganan" if winnerGold else "No hay diferencia entre el oro de los equipos cuando ganan"
print(Output, "\n")

#Excecute anova 2
loserGold, F, p = Anova(lbg, lrg)
print("Valor F: ", F, ". Valor p: ", p)
Output = "Hay diferencia entre el oro de los equipos cuando pierden" if loserGold else "No hay diferencia entre el oro de los equipos cuando pierden"
print(Output, "\n")

#Excecute anova 3
bothGold, F, p = Anova(wbg, wrg, lbg, lrg)
print("Valor F: ", F, ". Valor p: ", p)
Output = "Hay diferencia entre el oro de los equipos sin importar si ganan o pierden" if bothGold else "No hay diferencias entre el oro dependiendo si se gana o pierde"
print(Output, "\n")

#Execute anova 4
ObjResult, F, p = Anova(bDrag, rDrag)
print("Valor F: ", F, ". Valor p: ", p)
Output = "Hay diferencia entre los dragones que hace cada equipo" if ObjResult else "No hay diferencia entre los dragones que hace cada equipo"
print(Output, "\n")

#Execute anova 5
ObjResult, F, p = Anova(bHerald, rHerald)
print("Valor F: ", F, ". Valor p: ", p)
Output = "Hay diferencia entre los heraldos que hace cada equipo" if ObjResult else "No hay diferencia entre los heraldos que hace cada equipo"
print(Output, "\n")

# Output Final: 
# Valor F:  2.268700868620551 . Valor p:  0.1320425003918586
# No hay diferencia entre el oro de los equipos cuando ganan 

# Valor F:  0.16022516904313752 . Valor p:  0.6889579506716696
# No hay diferencia entre el oro de los equipos cuando pierden

# Valor F:  1365.3936527337269 . Valor p:  0.0
# Hay diferencias entre el oro dependiendo si se gana o pierde

# Valor F:  54.52539769234392 . Valor p:  1.5954178883441173e-13
# Hay diferencia entre los dragones que hace cada equipo

# Valor F:  26.8584645512463 . Valor p:  2.2106709839263933e-07
# Hay diferencia entre los heraldos que hace cada equipo