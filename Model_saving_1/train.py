import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

#df = pd.read_csv(url, names=columns_names

df = pd.read_csv("dib.csv", names=columns_names)

data = df.values
X = data[:, :8]
y = data[:, 8]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

model = LogisticRegression()
model.fit(X_train, y_train)

# accuracy
result = model.score(X_test, y_test)

print(result)

#saving the model
joblib.dump(model, "joblib_model.pkl")