import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


x_1 = open("C:/Users/user/Downloads/student_health_3.csv","r", encoding="cp949");
x1 = csv.reader(x_1)

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
for row in x1:
    row1.append(row[23])
    row2.append(row[24]) 
    row3.append(row[15])
    row4.append(row[16])
    row5.append(row[11])
	
x_1.close()

row_s = []
row_n = []

for idx_r in range(1,len(row3)):
    row_n.append(float(row5[idx_r]))
    row_s.append([float(row1[idx_r]), float(row2[idx_r]),float(row3[idx_r]),float(row4[idx_r])])

    
LinearClf = LinearDiscriminantAnalysis().fit(row_s, row_n)
QuadClf = QuadraticDiscriminantAnalysis().fit(row_s, row_n)

print(LinearClf.predict([[80, 60, 130.0, 28.5]]))
print(QuadClf.predict([[80, 60, 130.0, 28.5]]))
