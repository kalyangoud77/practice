x = [20,45,19]
y = [1,4,5]
a = list(x)+list(y)

for i in a:
    j = a.index(i)
    while j>0:
        if a[j-1] > a[j]:
            a[j-1],a[j] = a[j],a[j-1]
        else:
            break
        j = j-1
print(a)





















































