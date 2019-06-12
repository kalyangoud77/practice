s1 = "kalfkvmkfvkfmvkfmvpkfmv;lkalyanfkvnjfnvojefnvoenvokalyankjfnvjfnvijfenvkalyanjvijfvbifevinnuvnevnenkalyaneffvhvuoevnevnejv"

s2 ="kalyan"

i = 0
j = 0
k = 0
count = 0

while(i<len(s1)):
    j=0
    k=0
    while(j<len(s2)):
        if(s1[i] == s2[j]):
            k+=1
            i+=1
            j+=1
        else:
            k-=1
            i+=1
            break
    if (k == len(s2)):
            count+=1
print("kalyan is",count,"times repeated")