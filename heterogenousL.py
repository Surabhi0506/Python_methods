a=[10, "Swara", 30, "Pooja", 10, 80, 90, "Jaanu", "Agrima"]
m = max(i for i in a
        if type(i) == int)
b = a[:a.index(m)]
c = a[a.index(m):]

print(b)
print(c)