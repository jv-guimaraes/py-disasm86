| R/M | W = 0 | W = 1 | R/M | MOD = 00 | MOD = 01 | MOD = 10 |
|---|---|---|---|---|---|---|
| 000 | AL | AX | 000 | (BX) + (SI)    | (BX) + (SI) + D8 | (BX) + (SI) + D16 |
| 001 | CL | CX | 001 | (BX) + (DI)    | (BX) + (DI) + D8 | (BX) + (DI) + D16 |
| 010 | DL | DX | 010 | (BP) + (SI)    | (BP) + (SI) + D8 | (BP) + (SI) + D16 |
| 011 | BL | BX | 011 | (BP) + (DI)    | (BP) + (DI) + D8 | (BP) + (DI) + D16 |
| 100 | AH | SP | 100 | (SI)           | (SI) + D8        | (SI) + D16        |
| 101 | CH | BP | 101 | (DI)           | (DI) + D8        | (DI) + D16        |
| 110 | DH | SI | 110 | DIRECT ADDRESS | (BP) + D8        | (BP) + D16        |
| 111 | BH | DI | 111 | (BX)           | (BX) + D8        | (BX) + D16        |