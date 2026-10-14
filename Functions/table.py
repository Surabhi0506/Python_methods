print("Table of odd numbers between 1 to 10 : ")
for i in range(1,10):
    if i%2 != 0:
        print("Table of", i)
        for j in range(1,11):
            print(i, "x", j, "=", i*j)

        print()