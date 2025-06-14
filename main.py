import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/insurance.csv')

print(df.head())

plt.figure(figsize=(10, 6))

sns.scatterplot(x=df['bmi'], y=df['charges'], hue=df['smoker'])

# sns.regplot(x=df['bmi'], y=df['charges'])

plt.show()