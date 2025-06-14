import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './data/spotify.csv'

df = pd.read_csv(file_path, index_col="Date", parse_dates=True)

print(df.head())

print(df.tail())

print(list(df.columns))

plt.figure(figsize=(14,6))

plt.title("Daily Global Streams of Popular Songs in 2017-2018")

sns.lineplot(data=df['Shape of You'], label="Shape of You")
sns.lineplot(data=df['Despacito'], label="Despacito")

plt.xlabel("Date")

plt.show()
