from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd 
import numpy as np 

# read data
data = np.asarray(pd.read_csv('data.csv', header=None))
X = data[:, 0:2]
y = data[:, 2]

# instantiate model
model = DecisionTreeClassifier()
# fit the model
model.fit(X,y)
# Predictions
preds = model.predict(X)
# check accuracy of model
acc = accuracy_score(y, preds)
print(f'accuracy is: {acc}')