import csv
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
import time


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
    
NNstart = time.time()
clfMLP = MLPClassifier(random_state = 1, max_iter = 300).fit(row_s,row_n)
clfMLP.predict(row_s)
clfMLP.predict_proba(row_s)
print("Nueral Net 정확도 : ", clfMLP.score(row_s,row_n))
print("Neural Net time 훈련속도 :", time.time() - NNstart)

LOGstart = time.time()
clfLOG = LogisticRegression(random_state = 0).fit(row_s,row_n)
clfLOG.predict(row_s)
clfLOG.predict_proba(row_s)
print("LogisticRegression 정확도 : ", clfLOG.score(row_s,row_n))
print("LogisticRegression 훈련속도:", time.time() - LOGstart)
