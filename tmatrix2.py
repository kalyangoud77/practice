m = ([1, 2, 3, 4], [4, 1, 0, 1], [7, 2, 1, 3], [4, 5, 1, 0])

k = 1
sum = [0,0]

for i in range(0,len(m)-2):
    for j in range(i,len(m)-k):
        sum[i] = sum[i]+m[0][j]
        print(m[0][j])
    for j in range(i+1,len(m)-k):
        sum[i] = sum[i]+m[j][i+1]
        print(m[j][i+1])
    k-=1
print(sum)

