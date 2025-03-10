word=input("enter the word : ")
char=input("enter the character : ")
for i in word:
    if i==char:
        print("it is present")
        break
else:
    print("it is not present")