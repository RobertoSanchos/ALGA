m, n = map(int, input().split(" "))
tomb1 = list(map(int, input().split()))
tomb2 = list(map(int, input().split(" ")))

tomb1.sort(reverse=True)

i = 0
j = 0

while i < n and j < m:
    if tomb2[i] - tomb1[j] >= 0 and tomb1[j] != 0:
        print(tomb1[j])
        tomb1[j] = 0
        i += 1
        j = 0
        continue
    j += 1

while i != len(tomb2):
    print(-1)
    i += 1