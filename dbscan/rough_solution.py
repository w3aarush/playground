import math

a = [[4.5,8],[5,7],[6,6.5],[7,5],[9,4],[7,3],[8,3.5],[9,5],[4,4],[3,7.5],[4,6],[5,5]]

n = len(a)
result = []

for i in range(n):
    row = []
    for j in range(n):
        x1, y1 = a[i]
        x2, y2 = a[j]
        dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        row.append(round(dist, 2))
    result.append(row)

print(len(result))
for r in result:
    print(r)
