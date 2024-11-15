s, n = map(int, input().split(" "))
tomb = list(map(int, input().split(" ")))

m = 0
m += n

tomb2 = []
tomb2.extend(tomb)

megoldas = []

tomb.sort(reverse=True)
db = 0

for i in range(s):
    if n - tomb[i] >= 0 and tomb[i] != m:
        n = n - tomb[i]
        megoldas.append(tomb2.index(tomb[i])+1)
        tomb2[tomb2.index(tomb[i])] = 0
        db += 1
    if db == 2 and n == 0:
        break

if n != 0 or db != 2:
    print("IMPOSSIBLE")
else:
    for i in range(len(megoldas)):
        print(megoldas[i], end=" ")
