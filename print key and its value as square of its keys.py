d=dict()
for x in range (1,5):
    d[x]=x**2
print(d)

#merge dictinary

d1 = {'a':100, 'b':200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)