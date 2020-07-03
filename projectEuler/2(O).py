a = [1,2]

while a[-1] <= 4000000:
    i = a[-1]+a[-2]
    a.append(i)
    print(i)
    
b = a[:-1]
print(b)

c = []
for N in b:
    if N % 2 == 0:
        c.append(N)


print(sum(c))





#k = a[-1]+a[-2]
#print(k)

#a.append(k)
#print(a)
#[a,b]
#a.append