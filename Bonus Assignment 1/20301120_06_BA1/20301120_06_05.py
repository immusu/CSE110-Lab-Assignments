quan=int(input())
maxi=0
mini=0
summ=0
for i in range(0,quan):
    num = int(input())
    summ=summ+num
    avg=summ/num
    if i==0:
        maxi=num
        mini=num
    else:
        if num>maxi:
            maxi=num
        elif num<mini:
            mini=num
print("Maximum is:",maxi)
print("Minimum is :",mini)
print("Avarage",avg)