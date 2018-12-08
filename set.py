a = {'A', 'B', "C"}
b = {'B', 'C', 'D'}

total = a.union(b)
common = a.intersection(b)
result = total.difference(common) 
print(result)
