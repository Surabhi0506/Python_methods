#Strip spaces from both ends
text = "  Welcome to IMCC!  "
print("Remove Spaces:", text.strip())

#Capitalize first letter
text = "Welcome to IMCC !"
text= text.strip()
print("Capitalize First Letter:", text.capitalize())

#Title case(capitalize each word)
print(text.title())

#Count occurrencces of a substring
print(" Letter C occurs: ", text.count("C"), "times in text")

#Find position of a substring (-1 if not found)
print("Position of IMCC in text is", text.find("IMCC"))

#Replace a substring
print(text.replace("IMCC", "Python Magic"))

#Check if string starts or ends with certain substring
print(text.startswith(" We"))
print(text.endswith("! "))

#Split string into list by a delimeter
print("Simple split: ", text.split())

#Join a list of strings with a separator
word = ["Python", "is", "fun"]
print(" ".join(word))

