a=[]
a.append(6)
print(type(a))
print(len("hello"))
a.insert(1,6)
a.insert(7,5)
a.insert(0,9)
print(a[2:])
print(a[-1])
b=[45,7,9]
a.extend(b)
print(a)
print(len(a))
print(list(range(10)))
print(range(10))
print(list(range(1,10)))
print(list(range(1,11,3)))
sq=[r*r for r in list(range(1,11))]
print(sq)
num=list(range(1,11))
sq=[]
for  x in num:
    sq.append(x*x)
print(sq)
s="himanshu gotra"
x=[ch for ch in s if ch in "aeiou"]
print(x)
print('g' in s)
l1=["eggs"]
l2=["juice"]
b=l1
l1.append("toast")
b.extend(l2)
print(b)
print(l1)