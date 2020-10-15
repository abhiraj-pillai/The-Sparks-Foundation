# -*- coding: utf-8 -*-
"""Task2_SupervisedML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n0tqDC5-2tnDq06CL_1s-dRgWsqV0hAQ

### Predecting Grades using Linear Regression ML.

#### By: ABHIRAJ PILLAI
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns  
# %matplotlib inline

"""## Importing Data"""

url = "http://bit.ly/w-data"
data = pd.read_csv(url)

data.sample(10)

"""## Plotting the Data"""

sns.scatterplot(x  = 'Hours',y = 'Scores',data = data)
plt.title('Hours vs Scores ScatterPlot');

"""## Data Preprocessing"""

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

"""# Splitting data into Train and Test Subsets"""

from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test = train_test_split(X,y,train_size = 0.8,random_state=0)

"""## Creating and Training LinearRegression Model"""

from sklearn.linear_model import LinearRegression
predictor = LinearRegression()
predictor.fit(X_train, y_train) 
print("Beeeep Booop Baap ...Training complete....")

"""## Plotting the Fit Line"""

line = predictor.coef_*X+predictor.intercept_
plt.scatter(X, y)
plt.plot(X, line,'r-');

"""## Comparing ML model Predicted Scores to the Actual Scores"""

y_pred = predictor.predict(X_test)
compare = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
compare

"""## Predecting Scores"""

hour = float(input("Enter Number of Hours: "))
own_pred = predictor.predict([[hour]])
print("No of Hours = {}".format(hour))
print("Predicted Score = {}".format(own_pred[0]))

"""## Evaluating the Model"""

from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred)) 
print('Mean Gamma Deviance:', metrics.mean_gamma_deviance(y_test,y_pred))

