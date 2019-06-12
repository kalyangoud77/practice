s = input("Enter anything here: ")
words= (''.join(reversed(s))).split()
text=""
i=0
j=4
k=0
for word in words:
    text=text+word
print(text)
for n in range(len(text)//3):
    print(text[i:j])
    if(j>len(text)-3 or j>len(text)-4):
        break
    i=j
    if k==0:
        j=j+3
        k=1
    else:
        j=j+4
        k=0
