a = [1,2,3]
b = [1,4,3,4]

for i in range(len(a)):
    for j in range(len(b)):
        if (a[i]==b[j]):
            print(a[i],b[j])