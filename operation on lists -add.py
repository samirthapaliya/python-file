l1=[1,"red",2,3]
l2=["apple", "orange", "grapse"]
l3=["php","python","java"]
"""
#concadinate l1 and l2
#or add l1 and l2
l1.extend(l2)
print(l1)
"""
#l3 add a programming language
#remove unwanted data from l1
l3.append('javascript')
print(l3)

#remove unwanted data from l1


for i in l1:
    if type(i)==str:
        l1.remove(i)
print(l1)
print(l2)
print(l3)

for fruit in l2:
    print(fruit)

for color in l1:
    if type(color)==str:
        print (color)