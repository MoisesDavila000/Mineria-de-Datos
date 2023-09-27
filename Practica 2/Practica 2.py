import pandas as pd

# Read CSV
df = pd.read_csv("../high_diamond_ranked_10min.csv")

# Clean CSV as DataFrame
# Simplify info
winner = []
firstBlood = []
dragon = []
herald = []

for data in df.values:
    # winner
    if (data[1] == 1):
        winner.append("Blue")
    else:
        winner.append("Red")
    # FB
    if (data[4] == 1):
        firstBlood.append("Blue")
    else:
        firstBlood.append("Red")
    # Dragon
    if (data[9] == 1):
        dragon.append("Blue")
    elif (data[28]):
        dragon.append("Red")
    else:
        dragon.append("No one")
    # Herald
    if (data[10] == 1):
        herald.append("Blue")
    elif (data[29]):
        herald.append("Red")
    else:
        herald.append("No one")

df.insert(0, "Winner", winner, True)
df.insert(1, "FirstBlood", firstBlood, True)
df.insert(2, "Dragon", dragon, True)
df.insert(3, "Herald", herald, True)

# Delete useless info
useless_data = ["gameId", "blueDeaths", "redDeaths", "blueEliteMonsters", "redEliteMonsters", "blueAvgLevel",
                "redAvgLevel", "blueGoldDiff", "redGoldDiff", "blueCSPerMin", "redCSPerMin", "blueGoldPerMin", "redGoldPerMin", "blueWins", "blueFirstBlood", "redFirstBlood", "blueDragons", "redDragons", "blueHeralds", "redHeralds","blueExperienceDiff", "redExperienceDiff"]
df = df.drop(columns=useless_data)

# Create new CSV with cleaned DataFrame
df.to_csv('cleaned_rankedGames.csv', index=False)