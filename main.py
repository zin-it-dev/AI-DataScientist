import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './data/fifa.csv'

df = pd.read_csv(file_path, index_col="Date", parse_dates=True)

print(df.head())

plt.figure(figsize=(16, 6))

sns.lineplot(data=df)

plt.show()