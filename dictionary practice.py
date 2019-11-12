#create a dict, add datas like, roll_no, name, marks, along with gender, now i want to print
#all the names and marks whose gender is male, how would you do that?
#for females all females NAME and marks no discriimination pls

dict1 = {'roll no':[1,2,3,4]}
dict2 = {'name':['anup','sita','sankhar','gita']}
dict3 = {'marks':[75,80,60,30]}
dict4 = {'gender':['male','female','male','female']}
dict = {}    #DICT VITRA  aba sabai lai halni
for i in (dict1,dict2,dict3,dict4):   #sabai lai jodhxa
    dict.update(i)
print(dict)

#aba sabi lai autai dict ma garni
dict = {'roll no':[1,2,3,4,5],'name':['anup','sita','sankhar','gita'],'marks':[75,80,60,30],'gender':['male','female','male','female']}

for key,value in dict.items():      #yesla chai key vanako roll no, name, marks and gender ...ani value vanako tesko number or name or marks or male or female
    print(key,value)

#aba chai name halda tesko information auna paryo

#mathiko dict1 2 3 ra 4 bata ko information tala print garna lako
name1 = input("Enter your  name")
z=0
for i in range(len(dict2['name'])):   #to find the length of name list
    if dict2['name'][i]==name1:         #dict2 ma name xa ra name1 ma chai lekhni thau xa so teslai melako
        z=i                                 #z la chai data store garxa ..tesko satta i use na garnu ko raran bhanako i ma chai value change hunxa
print(dict['roll no'][z])
print(dict['marks'][z])
print(dict['gender'][z])