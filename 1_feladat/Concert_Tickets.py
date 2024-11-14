mo = list(map(int, input().split(" ")))
tomb1 = sorted(list(map(int, input().split())), reverse=True)
tomb2 = list(map(int, input().split(" ")))


megoldas = []
i = 0
j = 0

while i < mo[1] and j < len(tomb1):
    if tomb2[i] - tomb1[j] >= 0:
        megoldas.append(tomb1[j])
        del tomb1[j]
        i += 1
        j = 0
        continue
    j += 1

megoldas.extend(((len(tomb2) - i) * [-1]))

for i in range(len(megoldas)):
    print(megoldas[i])