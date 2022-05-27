import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

x_1 = open("C:/Users/user/Downloads/student_health_2.csv","r", encoding="ISO-8859-1");
x1 = csv.reader(x_1)

row1 = []
row2 = []
row3 = []
for row in x1:
    row1.append(row[16])
    row2.append(row[15]) 
    row3.append(row[11])
	
x_1.close()

row_s = []
row_n = []

for idx_r in range(1,len(row3)):
    row_n.append(float(row3[idx_r]))
    row_s.append([float(row1[idx_r]), float(row2[idx_r])])

neigh = KNeighborsClassifier(n_neighbors=6)
neigh.fit(row_s, row_n);

real1 = neigh.predict([[150, 45]])
print(real1)
