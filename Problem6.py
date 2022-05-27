import csv
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors

x1 = pd.read_csv("C:/Users/user/Downloads/subway.csv",encoding = 'euc-kr')

year= x1[['Year']]
line = x1[['Line 3']]


neigh = neighbors.KNeighborsClassifier(10)
neigh.fit(year, line)
pre2000 = neigh.predict([[2000]])
pre2001 = neigh.predict([[2001]])
pre2002 = neigh.predict([[2002]])

print("2000년도 예측값 :", pre2000)
print("2001년도 예측값 :", pre2001)
print("2002년도 예측값 :", pre2002)
