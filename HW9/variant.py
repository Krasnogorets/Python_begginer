import pandas as pd
df = pd.read_csv('california_housing_train.csv')
import seaborn as sns
df.head()
sns.scatterplot(data=df,x='households', y='population')