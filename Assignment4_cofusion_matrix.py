import pandas as pd

data = pd.read_csv('C:/Users/user/Downloads/random_number.csv', names = ['A','B'])

y_Actual = data['A']
y_Predicted = data['B']

confusion_matrix = pd.crosstab(y_Actual, y_Predicted, rownames = ['Actual'], colnames=['Predicted'])
confusion_matrix
