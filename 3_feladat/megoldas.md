# <p align = "center"><u>3.feladat</u> <br> 
## <p align = "center">Dinamikus programozás
### <p align = "center">Ada and Coins
#### <p align = "center"> [feladat link](https://www.spoj.com/problems/ADACOINS/)

## <p align = "center">Feladat megoldásának menete

 * #### 1.lépés 
 ***
``` python
ermekszama, sorok = map(int, input().split(" "))
ermek = list(map(int, input().split(" ")))
tavolsagok = [list(map(int, input().split(" "))) for _ in range(sorok)]
megoldas = []
db = 0
```

Adatok beolvasása és értékadás:<br>
**ermekszama** = Ada érméinek száma<br>
**sorok** = Hány darab tartományt teszteljünk<br>
**ermek** = Ada érméi<br>
**tavolsagok** = A tartományok<br>
**megoldas** = Ebbe a listába fognak kerülni a megadott tartományon belüli kifizethető értékek darabszámai<br>
**db** = Kifizethető értékek számolására



* #### 2.lépés 
***
``` python
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
```
Létrehozunk egy függvényt, amiben megállapítjuk, hogy a paraméterben átadott érték, ami a tartományon belül van, az kifizethető-e Ada érméivel, ha igen akkor true-val térünk vissza ( később hívjuk meg és használjuk ki a visszatérési értéket )


* #### 3.lépés 
***
``` python
for i in range(len(tavolsagok)):
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

```

A **tavolsagok** listában benne levő intervallumokon megyünk végig ( egyesével ), és ellenőrizzük a korábban megírt belerakhatoe() függvénnyel, hogy kifizethető-e az érték. Ha igen akkor növeljük a db értékét, amivel nyomon tudjuk követni, hogy eddig hány darabot tudtunk kifizetni. Ha az egyik tartománnyal végeztünk, akkor belerakjuk a megoldas listába a db-ben található értéket, és azután 0-zuk, valamint továbblépünk a következőre. 

A bejárások után kiíratjuk a **megoldas** listában szereplő értékeket, amik megadják sorban a kifizetések darabszámait.