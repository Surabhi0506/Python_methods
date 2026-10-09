name = input("Enter your name: ")
rev = ""
n = name
while len(n)>0:
    rev = rev + n[-1]
    n = n[:-1]

print(rev)
if name.lower() == rev.lower():
    print("Name is palindrome.")
else:
    print("Name is not palindrome.")