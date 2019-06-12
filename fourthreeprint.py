a=str((input('enter string :')))
y=len(a)-2
k=1
n=5
m=0
for i in a:
    m+=1
    print(i,end='')
    k+=1
    if k==n:
        k=1
        print('')
        if n==5:
            n=4
            if m!=len(a):
             if m+n-1>len(a):
                print('letters remain below 3')
                break;

        else:
            n=5
            if m != len(a):
             if m+n-1>len(a):
                print('letters remain below 4')
                break;
    '''if m>=len(a)-2:
        print('letters remain below 3')
        break'''