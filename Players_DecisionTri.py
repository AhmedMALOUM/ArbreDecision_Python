import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

data_players = pd.read_csv('players.csv', encoding='ISO-8859-1')


data_players.columns = data_players.columns.str.strip()  # Supprimer les espaces autour des noms de colonnes

print(data_players.columns)

print(data_players.head())

data_players = data_players.dropna(subset=['Market Value In Millions(£)', 'Age', 'Goals', 'Matches', 'Assists'])

data_players['HighValue'] = (data_players['Market Value In Millions(£)'] > 50).astype(int)


X = data_players[['Age', 'Goals', 'Matches', 'Assists']]
y = data_players['HighValue']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")


plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=['Low', 'High'], filled=True)
plt.show()
