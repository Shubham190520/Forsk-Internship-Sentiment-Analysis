import pandas as pd

data = pd.read_csv('cricket_salary.csv')

data.isnull().any(axis=0)

features = data.iloc[:,0:3].values



from sklearn.impute import SimpleImputer

from numpy import nan
imputer = SimpleImputer(missing_values = nan strategy='mean')

features[:,1:2] = imputer.fit_transform(features[:,1:2])

###########################


df = pd.read_csv('balanced_reviews.csv')

df.columns.tolist()

df['overall'].value_counts()

df.isnull().any(axis=0)

df[df.isnull().any(axis=1)]

df.dropna(inplace=True)

df = df[df['overall']!=3]

df['overall'].value_counts()

import numpy as np

df['Positivity'] = np.where(df['overall'] > 3 ,1, 0)

df['Positivity'].value_counts()
.