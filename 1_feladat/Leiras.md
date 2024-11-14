# <p align = "center"><u>1.feladat</u> <br> 
## <p align = "center">Keresés, rendezés, mohó stratégia
### <p align = "center">Concert Tickets
#### <p align = "center"> [feladat](https://cses.fi/problemset/task/1091)

#### <u>Feladat leírás</u>

<p style = "font-size: 20px; font-family:Times New Roman"> Van <i>n</i> koncertjegy, mindegyiknek egy bizonyos ára van. Ezután érkeznek meg az <i>m</i> vásárlók egymás után. Minden vásárló bejelenti, hogy mennyi a maximális ár, amit hajlandó kifizetni egy jegyért, majd ezután kap egy jegyet a lehető legközelebbi áron, amely nem haladja meg a maximális árat. <br><u>Bemenet</u> <br> Az első sorban egész számokat tartalmazó <i>n</i> és <i>m</i>, a jegyek és a vásárlók száma. A következő sorban <i>n</i> egész szám található: <i>h<sub>1</sub>, h<sub>2</sub>,...,h<sub>n</sub></i>: a jegyek árai. Az utolsó sorban <i>m</i> egész szám található: <i>t<sub>1</sub>, t<sub>2</sub>,...,t<sub>m</sub></i>: a vásárlókhoz tartozó maximális árak a sorrendjükben, ahogy érkeznek.
<br><u>Kimenet</u> <br>
Azt az árat kell kiírni minden vásárló számára, amit egy jegyért fog fizetni, és ezután a jegyet nem lehet újra megvásárolni. 
Ha egy vásárló nem tud jegyet vásárolni, akkor a -1 legyen kiíratva.
<br><u>Korlátok</u> <br>

* $ 1 \le n, m \le 2 \cdot 10^5 $ 
* $ 1 \le h_i, t_i \le 10^9 $

<p style = "font-size: 20px; font-family:Times New Roman">  <u>Minta</u> <br>

> <p style = "font-size: 20px; font-family:Times New Roman"> Bemenet: <br> 5 3 <br>5 3 7 8 5 <br> 4 8 3 <br>Kimenet: <br> 3<br> 8 <br> -1


