name = input("Enter your name: ")
print(name)

#occurrence of a
print("Occurrence of A: ", name.count("a"))

#replace a with b
print(name.replace("a", "z"))

#split name in 2
mid = len(name) // 2
p1 = name[:mid]
p2 = name[mid:]
print(p1)
print(p2)

#sort string
sorted("Surabhi")
print(sorted)