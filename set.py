l = [1,2,3,2,1]
for i in l:
    if l.count(i)>1:
        l.remove(i)
        print(l)