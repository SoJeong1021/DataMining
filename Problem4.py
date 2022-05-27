#!/usr/bin/env python
# coding: utf-8

# In[84]:


import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

x_1 = open("C:/Users/user/Downloads/park.csv","r", encoding="cp949");
x1 = csv.reader(x_1)

row1 = []
row2 = []
row3 = []
row4 = []
for row in x1:
    row1.append(row[2])
    row2.append(row[3]) 
    row3.append(row[4])
    row4.append(row[1])
	
x_1.close()

row_s = []
row_n = []

for idx_r in range(1,len(row3)):
    row_n.append(row4[idx_r])
    row_s.append([float(row1[idx_r]), float(row2[idx_r]),float(row3[idx_r])])

neigh = KNeighborsClassifier(n_neighbors=4)
neigh.fit(row_s, row_n);

real1 = neigh.predict([[1500000, 20000, 500000]])
print(real1)


# In[ ]:




