import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

##Leer CSV
df = pd.read_csv('../high_diamond_ranked_10min.csv')


##Eliminar valores no necesarios
drop_list = ["gameId", "blueTotalGold", "blueTotalExperience", "blueCSPerMin", "blueGoldPerMin", 'redWardsPlaced', 'redWardsDestroyed',
             'redFirstBlood', 'redKills', 'redDeaths', 'redAssists', 'redEliteMonsters', 'redDragons', 'redHeralds', 'redTowersDestroyed',
             'redTotalGold', 'redAvgLevel', 'redTotalExperience', 'redTotalMinionsKilled', 'redTotalJungleMinionsKilled', 'redGoldDiff',
             'redExperienceDiff', 'redCSPerMin', 'redGoldPerMin','blueEliteMonsters']

df2 = df.drop(drop_list, axis = 1)
# df2.to_csv('prediction.csv', index=False)

#Ejecutar KNN y RandomForest
X = df2.drop('blueWins', axis = 1)
y = df2.blueWins

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=42)

clf = RandomForestClassifier()
kn = KNeighborsClassifier()

clf.fit(X_train, y_train)
kn.fit(X_train, y_train)

##Prediction
predictions = clf.predict(X_test)

#Random Forest
print("Random Forest:")
print("Precision score : ",precision_score(y_test, predictions))
print("Recall score : ",recall_score(y_test, predictions))
print("Accuracy score : ",accuracy_score(y_test, predictions))
print("F1 score : ",f1_score(y_test, predictions))

##Output:
# Random Forest:
# Precision score :  0.7120901639344263
# Recall score :  0.704868154158215
# Accuracy score :  0.7105263157894737
# F1 score :  0.7084607543323139

#Pruebas del modelo:

data = [[28, 2, 1, 9, 6, 11, 0, 0, 0, 6.6, 195, 36, 643, -8],[21, 3, 1, 6, 2, 12, 0, 0, 0, 7.2, 236, 62, 2900, 1228],
        [14, 4, 0, 3, 3, 7, 1, 0, 0, 7, 258, 60, -100, 78],[14, 3, 0, 4, 3, 5, 1, 1, 0, 7, 236, 55, -800, -358],
        [21, 4, 1, 1, 3, 2, 1, -1, 0, 7.2, 265, 60, -1000, 80]]

columns = ["blueWardsPlaced","blueWardsDestroyed","blueFirstBlood","blueKills","blueDeaths","blueAssists","blueDragons",
           "blueHeralds","blueTowersDestroyed","blueAvgLevel","blueTotalMinionsKilled","blueTotalJungleMinionsKilled",
           "blueGoldDiff","blueExperienceDiff"]

dfExamples = pd.DataFrame(data, columns=columns)

# 0 = Pierde, 1 = Gana || [Probabilidad de perder, Probabilidad de ganar]
print(clf.predict(dfExamples))
print(clf.predict_proba(dfExamples))

# ##Example - Equipo Azul perdio
# Valores: [28, 2, 1, 9, 6, 11, 0, 0, 0, 6.6, 195, 36, 643, -8]
##Output:
# # [[0.87 0.13]] 87% probabilidad de perder

# ##Example Worlds T1-JDG Game 1 - T1 Gano
# Valores: [21, 3, 1, 6, 2, 12, 0, 0, 0, 7.2, 236, 62, 2900, 1228]
##Output:
# # [[0.18 0.82]] 82% probabilidad de ganar


# ##Example Worlds T1-JDG Game 2 - T1 Perdio
# Valores: [14, 4, 0, 3, 3, 7, 1, 0, 0, 7, 258, 60, -100, 78]
##Output:
# # [[0.55 0.45]] 55% probabilidad de perder

# ##Example Worlds T1-JDG Game 3 - T1 Won
# Valores: [14, 3, 0, 4, 3, 5, 1, 1, 0, 7, 236, 55, -800, -358]
##Output:
# # [[0.48 0.52]] 52% probabilidad de ganar

# ##Example Worlds T1-JDG Game 4 - T1 Won
# Valores: [21, 4, 1, 1, 3, 2, 1, -1, 0, 7.2, 265, 60, -1000, 80]
##Output:
# [[0.46 0.54]] 54% probabilidad de ganar

#Prioridades del modelo
importance = clf.feature_importances_
importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title("Importance Random Forest")
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.savefig("Importance_RandomForest.png")
plt.close()