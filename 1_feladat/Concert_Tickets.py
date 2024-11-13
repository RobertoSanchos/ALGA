mo = list(map(int, input().split(" ")))
tomb1 = list(map(int, input().split(" ")))
tomb2 = list(map(int, input().split(" ")))

tomb1.sort(reverse=True)

megoldas = []
i = 0
j = 0

while i < mo[1] and j < mo[0] and tomb1[j] != 0:
    if tomb2[i] - tomb1[j] >= 0 and tomb1[j] != 0:
        megoldas.append(tomb1[j])
        tomb1[j] = 0
        i += 1
        j = 0
        tomb1.sort(reverse=True)
        continue
    j += 1

megoldas.extend(((len(tomb2)-tomb1.count(0)) * [-1]))

for i in range(len(megoldas)):
    print(megoldas[i])