i=int(input())
d=i//86400
dm=i%86400
h=dm//3600
hm=dm%3600
m=hm//60
s=hm%60
if d==0:
    if h==0 and m==0:
        print(s,'second(s)')
    elif h==0 and s==0:
        print(m,'minute(s)')
    elif m==0 and s==0:
        print(h,'hour(s)')
    elif h==0:
        print(m,'minute(s)',s,'second(s)')
    elif m==0:
        print(h,'hour(s)',s,'second(s)')
    elif s==0:
        print(h,'hour(s)',m,'minute(s)')
    else:
        print(h,'hour(s)',m,'minute(s)',s,'second(s)')
elif h==0:
    if d==0 and m==0:
        print(s,'second(s)')
    elif d==0 and s==0:
        print(m,'minute(s)')
    elif m==0 and s==0:
        print(d,'day(s)')
    elif d==0:
        print(m,'minute(s)',s,'second(s)')
    elif m==0:
        print(d,'day(s)',s,'second(s)')
    elif s==0:
        print(d,'day(s)',m,'minute(s)')
    else:
        print(d,'day(s)',m,'minute(s)',s,'second(s)')
elif m==0:
    if h==0 and d==0:
        print(s,'second(s)')
    elif h==0 and s==0:
        print(d,'day')
    elif d==0 and s==0:
        print(h,'hour(s)')
    elif h==0:
        print(d,'day(s)',s,'second(s)')
    elif d==0:
        print(h,'hour(s)',s,'second(s)')
    elif s==0:
        print(h,'hour(s)',d,'day(s)')
    else:
        print(h,'hour(s)',d,'day(s)',s,'second(s)')
elif s==0:
    if h==0 and m==0:
        print(d,'day(s)')
    elif h==0 and d==0:
        print(m,'minute(s)')
    elif m==0 and d==0:
        print(h,'hour(s)')
    elif h==0:
        print(m,'minute(s)',d,'day(s)')
    elif m==0:
        print(h,'hour(s)',d,'day(s)')
    elif d==0:
        print(h,'hour(s)',m,'minute(s)')
    else:
        print(h,'hour(s)',m,'minute(s)',d,'day(s)')
else:
    print(d, "day(s)", h, "hour(s)", m, "minute(s)", s, "second(s)")