import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df["Price"] = boston.target
print(df.head())
x = df.drop("Price", axis=1)
lm = LinearRegression()
lm.fit(x, df.Price)
coeff = pd.Series(lm.coef_, index = boston.feature_names)
print('Coefficients: \n', coeff.sort_values())
print (df.corr())

#The infuence with the greatest effect on price of a house in Boston is LSTAT (% lower status of the population)
# The least effect on the price of a house in Boston
