ermekszama, sorok = map(int, input().split(" "))
ermek = list(map(int, input().split(" ")))
tavolsagok = [list(map(int, input().split(" "))) for _ in range(sorok)]
megoldas = []
db = 0

def belerakhatoe(n):
    k = n
    for i in range(len(ermek)-1, -1, -1):
        n = k
        if n - ermek[i] == 0:
            return True
        elif n - ermek[i] > 0:
            for j in range(i, -1, -1):
                if n - ermek[j] >= 0:
                    n = n - ermek[j]
                if n == 0:
                    return True
    return False

for i in range(len(tavolsagok)):
    if tavolsagok[i][0] == 1 and tavolsagok[i][1] == 1:
        megoldas.append(1)
        continue
    for j in range(int(tavolsagok[i][0]), int(tavolsagok[i][1]) + 1, 1):
        if j > sum(ermek):
            break
        if belerakhatoe(j):
            db += 1
    if db > 0:
        megoldas.append(db)
        db = 0

for megold in megoldas:
    print(megold)
