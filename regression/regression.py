# impport required modules
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# set the linear regression object
lm = LinearRegression()

# equation
# yhat = b0 + b1 * x

# get the data


# set predictor variable. Pridector variable is independent variable used to predict target variable.
x = df[['highway-mpg']] # this should be a dataframe and hence double brackets

# set target variable
y = df['price'] # this should be a series and hence single brackes

# fit the model to get parameters b0 (intercept) and b1 (slope)
lm.fit(x, y)

# make prediction
yhat = lm.predict(x)

# get intercept
b0 = lm.intercept_

# get slope
b1 = lm.coef_

