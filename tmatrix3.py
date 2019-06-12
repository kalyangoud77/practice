l=[[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6]]
l1=[]
for i in range(len(l)-2):
    for j in range(len(l)-2):
        value = 0
        for k in range(i,i+3):
            for m in range(j,j+3):
                if i == k:
                    print(l[k][m],end=" ")
                    value +=l[k][m]
                elif i != k and j+1 == m:
                    print(" ",l[k][m],end=" ")
                    value +=l[k][m]
                #if j+1 == m:
                    #print(l[k][m],end=" ")
                #else:
                 #   print(l[k][m],end=" ")
            print()
        l1.append(value)
        print()
print(l1)
print(max(l1))
