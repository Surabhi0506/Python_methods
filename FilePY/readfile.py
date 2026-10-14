with open("file.txt", "r") as f:
    data = f.read()

words = data.split()
print("Total number of words: ", len(words))

unique_words = set(words)
print("Unique words: ", unique_words)