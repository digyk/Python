numberstaken=[3,4,7,10,15,14,2]

print("Here are the numbers still available")

for n in range(0,20):
    if n in numberstaken:
        continue
    print(n)