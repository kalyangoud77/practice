l = [1,2,3,4,4,5,5,6,1]
i = 0
j = 1
for i in range(len(l)):
    for j in l:
        if (i==j):
            print(i,j)
            break
