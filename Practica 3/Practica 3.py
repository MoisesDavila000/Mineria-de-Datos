import pandas as pd
    
def avarage(type, df):
    data = []
    n = len(df.index)
    if('all' in type):
        data.extend(df[type.replace('all', 'blue')].values)
        data.extend(df[type.replace('all', 'red')].values)
        n *= 2
    else:
        data = df[type].values
    avg = sum(data)/n    
    return avg
    
def min_val(type, df):
    if ('all' in type):
        min_list = []
        min_list.append(df[type.replace('all', 'blue')].min())
        print(min_list)
        min_list.append(df[type.replace('all', 'red')].min())
        print(min_list)
        return min(min_list)
    else:
        return df[type].min()

def max_val(type, df):
    if ('all' in type):
        max_list = []
        max_list.append(df[type.replace('all', 'blue')].max())
        max_list.append(df[type.replace('all', 'red')].max())
        print(max_list)
        return max(max_list)
    else:
        return df[type].max()
        
def statistics(type, df, winner=True):
    #Conteo
    if(type == 'Blue'):
        df = df.loc[df['Winner'].str.contains('Blue')]
    elif(type == 'Red'):
        df = df.loc[df['Winner'].str.contains('Red')]
        
    if not winner:
        if(type == 'Blue'):
            type = 'Red'
        else:
            type = 'Blue'
    count_data = len(df.index)
    
    header = ['WardsPlaced','WardsDestroyed','Kills','Assists','TotalGold','TotalExperience','TotalMinionsKilled','TotalJungleMinionsKilled']
    avg_data = []
    min_data = []
    max_data = []
    tipo_data = []
    
    for head in header:
        title = type.lower() + head
        #Promedio
        avg_data.append(avarage(title, df))
        #Min
        min_data.append(min_val(title, df))
        #Max
        max_data.append(max_val(title, df))
        #Tipo
        if(type == 'All'):
            tipo_data.append(title)
        else:
            if(winner):
                tipo_data.append('win'+title)
            else:
                tipo_data.append('lose'+title)
        

    d = {'Tipo':tipo_data, 'Conteo':count_data, 'Promedio':avg_data, 'Min':min_data, 'Max':max_data}
    stats_df = pd.DataFrame(data=d)
    return stats_df
    
    
df = pd.read_csv("../Practica 2/cleaned_rankedGames.csv")

#Create stats DataFrame
stats_df = pd.DataFrame(statistics('All', df))
stats_df = stats_df._append(statistics('Blue', df), ignore_index=True)
stats_df = stats_df._append(statistics('Red', df), ignore_index=True)
stats_df = stats_df._append(statistics('Blue', df, False), ignore_index=True)
stats_df = stats_df._append(statistics('Red', df, False), ignore_index=True)
#Save DataFrame
stats_df.to_csv('statistics_rankedGames.csv', index=False)
