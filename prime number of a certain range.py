prime = [] #empty list
n=int(input("enter the range"))
for n in range(2,n):

    ans = True
    for i in range(2,n):
        if n % i == 0:
            ans = False
            break
    if ans == True:
        prime.append(n) #add to list if prime
print(prime)
