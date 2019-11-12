dic1= {"no1":10, "no2":20}
dic2={"no3":30,"no4":30}
dic4 = {}
for d in (dic1, dic2):
dic4.update(d)
print(dic4)