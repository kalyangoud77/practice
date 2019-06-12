l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in l:
    if num > 0:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)