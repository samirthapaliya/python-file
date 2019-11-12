hello = input('write name')

name = ['john','sam','anna','ben','jeff']
maths = [88.0,77.0,67.0,87.0,90.0]
english = [86.0,67.0,65.0,78.0,80.0]
c = 0
for i in range(len(name)):
    if name[i] == hello:
        c = i
print(name[c])
print(maths[c])
print(english[c])
