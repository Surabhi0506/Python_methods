with open("file.txt", "r") as f:
    l = f.readlines()

print("Total number of lines: ", len(l))
print("2nd line of the file: ", l[1])
print("4th line of the file: ", l[4])