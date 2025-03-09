names = []
for name in range(10):
    names.append(input("Enter your name here: "))
for name in names:
    if len(name) > 5:
        print(name)
