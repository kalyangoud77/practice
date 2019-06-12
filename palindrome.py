s = input("Enter a word : ")
k=s[::-1]
if k == s:
    print("it is a palindrome",s)
else:
    print("it is not a palindrome",s)
