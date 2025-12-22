import pandas as pd
import numpy as np
import math
df = pd.read_csv('./sample_data.csv')

points = list(zip(df['x'],df['y']))
collection = []
for p1 in points:
    row = []
    for p2 in points:
        x1,y1 = p1
        x2,y2 = p2
        distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
        row.append(round(distance,3))
    collection.append(row)

indx = df['Unnamed: 0']
indx = list(indx)

df = df.drop('Unnamed: 0',axis = 1)
df.index = indx

df2 = pd.DataFrame(collection,columns=indx,index=indx)
df3 = pd.concat([df,df2],axis=1)

df3.to_csv('euclidian_distance.csv')