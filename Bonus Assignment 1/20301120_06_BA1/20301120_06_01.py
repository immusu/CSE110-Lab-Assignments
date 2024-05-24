i=int(input())
d=i//86400
dm=i%86400
h=dm//3600
hm=dm%3600
m=hm//60
s=hm%60
print(d,"day(s)",h,"hour(s)",m,"minute(s)",s,"second(s)")