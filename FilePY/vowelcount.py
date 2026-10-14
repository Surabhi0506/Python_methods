with open("file.txt", "r") as f:
    data = f.read()

    count = 0
    for ch in data:
        if ch.lower() in "aeiouAEIOU":
            count += 1
print("Total number of vowels: ", count)

