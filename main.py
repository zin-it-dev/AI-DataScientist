import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/flight_delays.csv', index_col="Month")

print(df.head())

plt.figure(figsize=(10, 6))

plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

sns.barplot(x=df.index, y=df['NK'])

sns.heatmap(data=df, annot=True)

plt.ylabel("Arrival delay (in minutes)")

plt.show()