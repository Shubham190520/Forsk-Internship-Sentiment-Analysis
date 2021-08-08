import pandas as pd
df = pd.read_csv("Salaries.csv")

df.shape

df.columns

df.head()

df.tail()

df['rank']

df['rank'].values

df['rank'].unique()

df['rank'].value_counts()

    #EDA (Initial investigation of data)
df['salary'].max()
df['salary'].min()
df['salary'].mean()

df['salary'] > 100000

df[df['salary'] > 100000]