# <p align = "center"><u>1.feladat</u> <br> 
## <p align = "center">Keresés, rendezés, mohó stratégia
### <p align = "center">Sum of Two Values
#### <p align = "center"> [feladat link](https://cses.fi/problemset/task/1640/)

### Feladat megoldásának menete
***
 * #### 1.lépés 
 ***
``` python
s, n = map(int, input().split(" "))
tomb = list(map(int, input().split(" ")))

m = 0
m += n

tomb2 = []
tomb2.extend(tomb)

megoldas = []

tomb.sort(reverse=True)
db = 0
```

Adatok beolvasása és értékadás:<br>
s = A tömb mérete<br>
n = A keresett összeg<br>
tomb = A tömb értékei<br>
m = A keresett összeg ( segédváltozóként a for ciklusban )<br>
tomb2 = A tömb értékei ismét ( index kereséshez )<br>
megoldas = A lista amibe kerülni fognak az indexek<br>
db = A megfelelő indexek számolásához<br><br>

A tomb elemeit csökkenő sorrendbe állítjuk, az optimális keresés miatt.


* #### 2.lépés 
***
``` python
for i in range(s):
    if n - tomb[i] >= 0 and tomb[i] != m:
        n = n - tomb[i]
        megoldas.append(tomb2.index(tomb[i])+1)
        tomb2[tomb2.index(tomb[i])] = 0
        db += 1
    if db == 2 and n == 0:
        break
```
For Ciklus:<br>
A ciklus a tömb hosszáig megy, és 2 db feltételt tartalmaz:<br>

1: A tömb elemeit vonjuk ki a keresett összegből, amíg nem kapunk 0-át, mert ezáltal megkaphatjuk azt, de közben megkeressük a tomb2 listában ( eredeti rendezetlen tömb ) az értékhez tartozó indexet, és belerakjuk a megoldasok listába, valamint az ehez tartozó értéket 0-ra állítjuk, hogy ne mindig ugyanazzal az indexxel térjen vissza több egyforma szám esetén. Ezután növelni kell a db értékét, hogy tudjuk hány elemből áll össze ( 2 db kell számunkra ).

2: Ellenőrizzük, hogy pontosan 2 db értékből jön ki a keresett összeg. Ha ez teljesül nem kell tovább keresnünk, kilépünk a ciklusból.

* #### 3.lépés 
***
``` python
if n != 0 or db != 2:
    print("IMPOSSIBLE")
else:
    for i in range(len(megoldas)):
        print(megoldas[i], end=" ")
```
Az utolsó lépésben ellenőrizzük, hogy sikerült-e megtalálni a 2 db indexet, ha nem akkor kiírjuk, hogy "IMPOSSIBLE", egyébként pedig kiíratjuk a lista elemeit ( az indexeket ).