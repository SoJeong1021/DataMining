import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

# row_s : 군집화에 사용할 독립변수 모음

wcss = []

for k in range(2,11):
    kmeans = KMeans(n_clusters = k, random_state = 0).fit(row_s)
    wcss.append(kmeans.inertia_)
    
plt.plot(wcss)

# k = 2로 군집화
kmeans2 = KMeans(n_clusters = 2, random_state = 0).fit(row_s)

print(kmeans2.labels_)

# kmeans2.labels_ 값이 0 이면 class2(고학년) 1이면 class1(저학년) 
