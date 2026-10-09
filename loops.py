#for loop
print("Prints numbers using for loop")
for i in range(5): #value is excluded eg: 5 is excludedy
    print(i)

#continue: skips current iteration
print("Output of for loop")
for i in range(5):
    if i == 2:
        continue
    print(i)

#break: exits loop imediately
print("Output of for loop with break")
for i in range(5):
    if i == 3:
        break
    print(i)