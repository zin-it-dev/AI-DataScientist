import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/iris.csv', index_col='Id')

print(df.head())

plt.figure(figsize=(5, 4))

# sns.histplot(data=df, x='Petal Length (cm)', hue='Species')

# plt.title("Histogram of Petal Lengths, by Species")

# sns.kdeplot(data=df['Petal Length (cm)'], fill=True)

# sns.jointplot(x=df['Petal Length (cm)'], y=df['Sepal Width (cm)'], kind='kde')

sns.kdeplot(data=df, x='Petal Length (cm)', hue='Species', fill=True)

plt.title("Distribution of Petal Lengths, by Species")

plt.show()