s = "Hi welcome to this world"
i=0
j=4
k=0
x = (''.join(reversed(s)))
text = x.replace(" ","")
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
