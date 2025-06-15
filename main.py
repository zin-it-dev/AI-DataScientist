import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("./data/melb_data.csv")

# print(df.describe())

# print(df.columns)

df = df.dropna(axis=0)

y = df.Price

features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = df[features]

# print(X.describe())
# print(y)

model = DecisionTreeRegressor(random_state=1)

model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(model.predict(X.head()))