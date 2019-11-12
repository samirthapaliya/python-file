dic1 = {"no1":10, "no2":20}
dic2 = {"no3":30,"no4":30}
dic = {}

for d  in (dic1,dic2):dic.update(d)
if "no1" in dic:
        print("key is present in the dictionary")
else:
        print("key is not present in dictionary")

