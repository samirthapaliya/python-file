#declare a list with number, delete odd no from a list using loop
L=[1,2,3,4,5,6,7,8,9]
for i in L :
    if i % 2 == 1:
        L.remove(i)

print(L)
L.remove(8)   #this is to remove speccified number from the list....jun lekhyo tai delete garxa

print(L)

del(L[1])   #del the element from the position in index
print(L)

L.append(8)     #add the element from the backside of the list
print(L)

L.extend([90,90,80,78])  #add element from the last
print(L)

L.pop()  #pop delete the element from the last position where the element is not specified
print(L)
