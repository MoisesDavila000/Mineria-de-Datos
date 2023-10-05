import pandas as pd
import scipy.stats as stats

#Anova gold - scipy
def goldAnova(df):
    #Obtener los valores de oro de cada equipo cuando gana y pierde
    wbg, lrg, lbg, wrg = [], [], [], []
    for data in df.values:
        if(data[0]=='Blue'):
            wbg.append(data[9])
            lrg.append(data[18])
        else:
            lbg.append(data[9])
            wrg.append(data[18])
            
    #Aplicar anova a los valores de ambos equipos cuando ganan
    F, p = stats.f_oneway(wbg, wrg)
    print("Valor F: ", F, "Valor p: ",p)
    if(p<0.05):
        print("Hay diferencias entre el oro de los equipos cuando ganan\n")
    else:
        print("No hay diferencias entre el oro de los equipos cuando ganan\n")
    
    #Aplicar anova a los valores de ambos equipos cuando pierden
    F, p = stats.f_oneway(lbg, lrg)
    print("Valor F: ", F ,"Valor p: ", p)
    if(p<0.05):
        print("Hay diferencias entre el oro de los equipos cuando pierden\n")
    else:
        print("No hay diferencias entre el oro de los equipos cuando pierden\n")
    
    #Aplicar anova a todos los valores para determinar si estos varian o no sin importar la situacion del equipo
    F, p = stats.f_oneway(wbg, wrg, lbg, lrg)
    print("Valor F: ", F , "Valor p: ", p)
    if(p<0.05):
        print("Hay diferencias entre el oro dependiendo si se gana o pierde\n")
    else:
        print("A los 10 minutos nunca varia el oro\n")

#Read CSV
df = pd.read_csv("../Practica 2/cleaned_rankedGames.csv")

#Excecute anova
goldAnova(df)

# Output Final: 
# Valor F:  2.268700868620551 Valor p:  0.1320425003918586
# No hay diferencias entre el oro de los equipos cuando ganan

# Valor F:  0.16022516904313752 Valor p:  0.6889579506716696
# No hay diferencias entre el oro de los equipos cuando pierden

# Valor F:  1365.3936527337269 Valor p:  0.000000000000
# Hay diferencias entre el oro dependiendo si se gana o pierde