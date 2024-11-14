# <p align = "center"><u>1.feladat</u> <br> 
## <p align = "center">Keresés, rendezés, mohó stratégia
### <p align = "center">Concert Tickets
#### <p align = "center"> [feladat link](https://cses.fi/problemset/task/1091)

### Feladat leírás
***

 Van <i>n</i> koncertjegy, mindegyiknek egy bizonyos ára van. Ezután érkeznek meg az <i>m</i> vásárlók egymás után. Minden vásárló bejelenti, hogy mennyi a maximális ár, amit hajlandó kifizetni egy jegyért, majd ezután kap egy jegyet a lehető legközelebbi áron, amely nem haladja meg a maximális árat.
 * #### Bemenet 
 ***
 Az első sorban egész számokat tartalmazó <i>n</i> és <i>m</i>, a jegyek és a vásárlók száma. A következő sorban <i>n</i> egész szám található: <i>h<sub>1</sub>, h<sub>2</sub>,...,h<sub>n</sub></i>: a jegyek árai. Az utolsó sorban <i>m</i> egész szám található: <i>t<sub>1</sub>, t<sub>2</sub>,...,t<sub>m</sub></i>: a vásárlókhoz tartozó maximális árak a sorrendjükben, ahogy érkeznek.
* #### Kimenet
***
Azt az árat kell kiírni minden vásárló számára, amit egy jegyért fog fizetni, és ezután a jegyet nem lehet újra megvásárolni. 
Ha egy vásárló nem tud jegyet vásárolni, akkor a -1 legyen kiíratva.

* #### Korlátok
***
1 <= <i>n, m </i><= 2 · 10 <sup>5</sup> <br>
1 <= <i>h<sub>i</sub>, t<sub>i</sub></i> <= 10<sup>9 </sup>

* #### Minta
***
Bemenet: <br> 5 3 <br>5 3 7 8 5 <br> 4 8 3 <br><br> Kimenet: <br> 3<br> 8 <br> -1


