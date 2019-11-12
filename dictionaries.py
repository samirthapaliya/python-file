dict = {'rollno':[1,2,3,4],'name':['subash','aakash','sushma']}
roll=dict['rollno']
name=dict['name']
data=int(input('enter your rollno'))

for i in range (len(roll)):
    if roll[i]==data:
        temp=0
        temp=i

print(name[temp])