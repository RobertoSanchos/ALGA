# <p align = "center"><u>3.feladat</u> <br> 
## <p align = "center">Dinamikus programozás
### <p align = "center">Ada and Coins
#### <p align = "center"> [feladat link](https://www.spoj.com/problems/ADACOINS/)

## <p align = "center">Feladat leírás


Adának a katicabogárnak több érméje van a pénztárcájában. Arra kíváncsi, hogy hány különböző értéket ( az érme részhalmazának összegét ) képes elkészíteni ( egy adott tartományon belül ).

 * #### Bemenet 
 ***
Az első sor két egész számot tartalmaz: $1\le N \le 10^4, 1\le Q \le 5 \cdot 10^5$<br>
az érmék számát és a tesztesetek számát az adott tartományokra.

A következő sor **N** egész számot tartalmaz: $1\le A_i \le 10^5$ 

Ada tárcájában lévő érmék értékeit.

Ezt követően **Q** sorok következnek, amelyek mindegyike két egész számot tartalmaz: 

$1\le B \le E \le 10^5$ 

A tartomány eleje és vége, amelyekre Ada szeretné tudni a választ.
* #### Kimenet
***

Minden egyes adott tartományon belül számoljuk meg, hogy hány darab értéket tud kifizetni az adott érmékkel.

* #### Minta
***
Bemenet:
10 10
1 2 2 3 5 30 31 90 100 100
1 1
1 5
3 6
2 9
30 100
1 10000
30 32
5 12
9 29
190 220


Kimenet:
1
5
4
8
40
231
3
8
5
25

Levezetés:
[  1,    1]: 1 

[  1,    5]: 1 2 3 4 5 

[  3,    6]: 3 4 5 6 

[  2,    9]: 2 3 4 5 6 7 8 9 

[ 30,  100]: 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 61 62 63 64 65 66 67 68 69 70 71 72 73 74 90 91 92 93 94 95 96 97 98 99 100 

[  1,10000]: 1 2 3 4 5 6 7 8 9 10 11 12 13 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 61 62 63 64 65 66 67 68 69 70 71 72 73 74 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 290 291 292 293 294 295 296 297 298 299 300 301 302 303 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 351 352 353 354 355 356 357 358 359 360 361 362 363 364 

[ 30,   32]: 30 31 32 

[  5,   12]: 5 6 7 8 9 10 11 12 

[  9,   29]: 9 10 11 12 13 

[190,  220]: 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 220

