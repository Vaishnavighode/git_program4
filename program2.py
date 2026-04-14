txt=input("Enter a string to check palindrome   : ")
rev=" ".join(reversed(txt))
if txt==rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    