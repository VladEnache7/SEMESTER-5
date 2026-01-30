import math
n=7051
binitial=1
b=[]
a=[]
x=[]
bsquare=[]
a.append(int(math.sqrt(n)))
b.append(a[0])
x.append(math.sqrt(n)-a[0])
bsquare.append((b[0]*b[0]) % n)
for i in range(1,8):
    a.append(int(1/x[i-1]) % n)
    x.append(1/x[i-1]-a[i] % n)
    if i==1:
        b.append((a[i]*b[i-1]+binitial) % n)
    else:
        b.append((a[i]*b[i-1]+b[i-2]) % n)
    bsquare.append((b[i]*b[i]) % n)
print("a ",a)
print("b ",b)
print("x ",x)
print("b^2 ",bsquare)