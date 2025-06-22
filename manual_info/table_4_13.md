| 0x  | 0b       | BYTE 2      | BYTES 3,4,5,6                          | ASM-86 INSTRUCTION FORMAT        |
|:---|:----------|:------------|:---------------------------------------|:---------------------------------|
| 00 | 0000 0000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADD REG8/MEM8, REG8              |
| 01 | 0000 0001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADD REG16/MEM16, REG16           |
| 02 | 0000 0010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADD REG8, REG8/MEM8              |
| 03 | 0000 0011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADD REG16, REG16/MEM16           |
| 04 | 0000 0100 | DATA-8      |                                        | ADD AL, IMMED8                   |
| 05 | 0000 0101 | DATA-LO     | DATA-HI                                | ADD AX, IMMED16                  |
| 06 | 0000 0110 |             |                                        | PUSH ES                          |
| 07 | 0000 0111 |             |                                        | POP ES                           |
| 08 | 0000 1000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | OR REG8/MEM8, REG8               |
| 09 | 0000 1001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | OR REG16/MEM16, REG16            |
| 0A | 0000 1010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | OR REG8, REG8/MEM8               |
| 0B | 0000 1011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | OR REG16, REG16/MEM16            |
| 0C | 0000 1100 | DATA-8      |                                        | OR AL, IMMED8                    |
| 0D | 0000 1101 | DATA-LO     | DATA-HI                                | OR AX, IMMED16                   |
| 0E | 0000 1110 |             |                                        | PUSH CS                          |
| 0F | 0000 1111 |             |                                        | (not used)                       |
| 10 | 0001 0000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADC REG8/MEM8, REG8              |
| 11 | 0001 0001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADC REG16/MEM16, REG16           |
| 12 | 0001 0010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADC REG8, REG8/MEM8              |
| 13 | 0001 0011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | ADC REG16, REG16/MEM16           |
| 14 | 0001 0100 | DATA-8      |                                        | ADC AL, IMMED8                   |
| 15 | 0001 0101 | DATA-LO     | DATA-HI                                | ADC AX, IMMED16                  |
| 16 | 0001 0110 |             |                                        | PUSH SS                          |
| 17 | 0001 0111 |             |                                        | POP SS                           |
| 18 | 0001 1000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SBB REG8/MEM8, REG8              |
| 19 | 0001 1001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SBB REG16/MEM16, REG16           |
| 1A | 0001 1010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SBB REG8, REG8/MEM8              |
| 1B | 0001 1011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SBB REG16, REG16/MEM16           |
| 1C | 0001 1100 | DATA-8      |                                        | SBB AL, IMMED8                   |
| 1D | 0001 1101 | DATA-LO     | DATA-HI                                | SBB AX, IMMED16                  |
| 1E | 0001 1110 |             |                                        | PUSH DS                          |
| 1F | 0001 1111 |             |                                        | POP DS                           |
| 20 | 0010 0000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | AND REG8/MEM8, REG8              |
| 21 | 0010 0001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | AND REG16/MEM16, REG16           |
| 22 | 0010 0010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | AND REG8, REG8/MEM8              |
| 23 | 0010 0011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | AND REG16, REG16/MEM16           |
| 24 | 0010 0100 | DATA-8      |                                        | AND AL, IMMED8                   |
| 25 | 0010 0101 | DATA-LO     | DATA-HI                                | AND AX, IMMED16                  |
| 26 | 0010 0110 |             |                                        | ES: (segment override prefix)    |
| 27 | 0010 0111 |             |                                        | DAA                              |
| 28 | 0010 1000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SUB REG8/MEM8, REG8              |
| 29 | 0010 1001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SUB REG16/MEM16, REG16           |
| 2A | 0010 1010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SUB REG8, REG8/MEM8              |
| 2B | 0010 1011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | SUB REG16, REG16/MEM16           |
| 2C | 0010 1100 | DATA-8      |                                        | SUB AL, IMMED8                   |
| 2D | 0010 1101 | DATA-LO     | DATA-HI                                | SUB AX, IMMED16                  |
| 2E | 0010 1110 |             |                                        | CS: (segment override prefix)    |
| 2F | 0010 1111 |             |                                        | DAS                              |
| 30 | 0011 0000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | XOR REG8/MEM8, REG8              |
| 31 | 0011 0001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | XOR REG16/MEM16, REG16           |
| 32 | 0011 0010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | XOR REG8, REG8/MEM8              |
| 33 | 0011 0011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | XOR REG16, REG16/MEM16           |
| 34 | 0011 0100 | DATA-8      |                                        | XOR AL, IMMED8                   |
| 35 | 0011 0101 | DATA-LO     | DATA-HI                                | XOR AX, IMMED16                  |
| 36 | 0011 0110 |             |                                        | SS: (segment override prefix)    |
| 37 | 0011 0110 |             |                                        | AAA                              |
| 38 | 0011 1000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | CMP REG8/MEM8, REG8              |
| 39 | 0011 1001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | CMP REG16/MEM16, REG16           |
| 3A | 0011 1010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | CMP REG8, REG8/MEM8              |
| 3B | 0011 1011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | CMP REG16, REG16/MEM16           |
| 3C | 0011 1100 | DATA-8      |                                        | CMP AL, IMMED8                   |
| 3D | 0011 1101 | DATA-LO     | DATA-HI                                | CMP AX, IMMED16                  |
| 3E | 0011 1110 |             |                                        | DS: (segment override prefix)    |
| 3F | 0011 1111 |             |                                        | AAS                              |
| 40 | 0100 0000 |             |                                        | INC AX                           |
| 41 | 0100 0001 |             |                                        | INC CX                           |
| 42 | 0100 0010 |             |                                        | INC DX                           |
| 43 | 0100 0011 |             |                                        | INC BX                           |
| 44 | 0100 0100 |             |                                        | INC SP                           |
| 45 | 0100 0101 |             |                                        | INC BP                           |
| 46 | 0100 0110 |             |                                        | INC SI                           |
| 47 | 0100 0111 |             |                                        | INC DI                           |
| 48 | 0100 1000 |             |                                        | DEC AX                           |
| 49 | 0100 1001 |             |                                        | DEC CX                           |
| 4A | 0100 1010 |             |                                        | DEC DX                           |
| 4B | 0100 1011 |             |                                        | DEC BX                           |
| 4C | 0100 1100 |             |                                        | DEC SP                           |
| 4D | 0100 1101 |             |                                        | DEC BP                           |
| 4E | 0100 1110 |             |                                        | DEC SI                           |
| 4F | 0100 1111 |             |                                        | DEC DI                           |
| 50 | 0101 0000 |             |                                        | PUSH AX                          |
| 51 | 0101 0001 |             |                                        | PUSH CX                          |
| 52 | 0101 0010 |             |                                        | PUSH DX                          |
| 53 | 0101 0011 |             |                                        | PUSH BX                          |
| 54 | 0101 0100 |             |                                        | PUSH SP                          |
| 55 | 0101 0101 |             |                                        | PUSH BP                          |
| 56 | 0101 0110 |             |                                        | PUSH SI                          |
| 57 | 0101 0111 |             |                                        | PUSH DI                          |
| 58 | 0101 1000 |             |                                        | POP AX                           |
| 59 | 0101 1001 |             |                                        | POP CX                           |
| 5A | 0101 1010 |             |                                        | POP DX                           |
| 5B | 0101 1011 |             |                                        | POP BX                           |
| 5C | 0101 1100 |             |                                        | POP SP                           |
| 5D | 0101 1101 |             |                                        | POP BP                           |
| 5E | 0101 1110 |             |                                        | POP SI                           |
| 5F | 0101 1111 |             |                                        | POP DI                           |
| 61 | 0110 0001 |             |                                        | (not used)                       |
| 62 | 0110 0010 |             |                                        | (not used)                       |
| 63 | 0110 0011 |             |                                        | (not used)                       |
| 64 | 0110 0100 |             |                                        | (not used)                       |
| 65 | 0110 0101 |             |                                        | (not used)                       |
| 66 | 0110 0110 |             |                                        | (not used)                       |
| 67 | 0110 0111 |             |                                        | (not used)                       |
| 68 | 0110 1000 |             |                                        | (not used)                       |
| 69 | 0110 1001 |             |                                        | (not used)                       |
| 6A | 0110 1010 |             |                                        | (not used)                       |
| 6B | 0110 1011 |             |                                        | (not used)                       |
| 6C | 0110 1100 |             |                                        | (not used)                       |
| 6D | 0110 1101 |             |                                        | (not used)                       |
| 6E | 0110 1110 |             |                                        | (not used)                       |
| 6F | 0110 1111 |             |                                        | (not used)                       |
| 70 | 0111 0000 | IP-INC8     |                                        | JO SHORT-LABEL                   |
| 71 | 0111 0001 | IP-INC8     |                                        | JNO SHORT-LABEL                  |
| 72 | 0111 0010 | IP-INC8     |                                        | JB/JNAE/SHORT-LABEL JC           |
| 73 | 0111 0011 | IP-INC8     |                                        | JNB/JAE/SHORT-LABEL JNC          |
| 74 | 0111 0100 | IP-INC8     |                                        | JE/JZ SHORT-LABEL                |
| 75 | 0111 0101 | IP-INC8     |                                        | JNE/JNZ SHORT-LABEL              |
| 76 | 0111 0110 | IP-INC8     |                                        | JBE/JNA SHORT-LABEL              |
| 77 | 0111 0111 | IP-INC8     |                                        | JNBE/JA SHORT-LABEL              |
| 78 | 0111 1000 | IP-INC8     |                                        | JS SHORT-LABEL                   |
| 79 | 0111 1001 | IP-INC8     |                                        | JNS SHORT-LABEL                  |
| 7A | 0111 1010 | IP-INC8     |                                        | JP/JPE SHORT-LABEL               |
| 7B | 0111 1011 | IP-INC8     |                                        | JNP/JPO SHORT-LABEL              |
| 7C | 0111 1100 | IP-INC8     |                                        | JL/JNGE SHORT-LABEL              |
| 7D | 0111 1101 | IP-INC8     |                                        | JNL/JGE SHORT-LABEL              |
| 7E | 0111 1110 | IP-INC8     |                                        | JLE/JNG SHORT-LABEL              |
| 7F | 0111 1111 | IP-INC8     |                                        | JNLE/JG SHORT-LABEL              |
| 80 | 1000 0000 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-8           | ADD REG8/MEM8, IMMED8            |
| 80 | 1000 0000 | MOD 001 R/M | (DISP-LO), (DISP-HI), DATA-8           | OR REG8/MEM8, IMMED8             |
| 80 | 1000 0000 | MOD 010 R/M | (DISP-LO), (DISP-HI), DATA-8           | ADC REG8/MEM8, IMMED8            |
| 80 | 1000 0000 | MOD 011 R/M | (DISP-LO), (DISP-HI), DATA-8           | SBB REG8/MEM8, IMMED8            |
| 80 | 1000 0000 | MOD 100 R/M | (DISP-LO), (DISP-HI), DATA-8           | AND REG8/MEM8, IMMED8            |
| 80 | 1000 0000 | MOD 101 R/M | (DISP-LO), (DISP-HI), DATA-8           | SUB REG8/MEM8, IMMED8            |
| 80 | 1000 0000 | MOD 110 R/M | (DISP-LO), (DISP-HI), DATA-8           | XOR REG8/MEM8, IMMED8            |
| 80 | 1000 0000 | MOD 111 R/M | (DISP-LO), (DISP-HI), DATA-8           | CMP REG8/MEM8, IMMED8            |
| 81 | 1000 0001 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | ADD REG16/MEM16, IMMED16         |
| 81 | 1000 0001 | MOD 001 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | OR REG16/MEM16, IMMED16          |
| 81 | 1000 0001 | MOD 010 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | ADC REG16/MEM16, IMMED16         |
| 81 | 1000 0001 | MOD 011 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | SBB REG16/MEM16, IMMED16         |
| 81 | 1000 0001 | MOD 100 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | AND REG16/MEM16, IMMED16         |
| 81 | 1000 0001 | MOD 101 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | SUB REG16/MEM16, IMMED16         |
| 81 | 1000 0001 | MOD 110 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | XOR REG16/MEM16, IMMED16         |
| 81 | 1000 0001 | MOD 111 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | CMP REG16/MEM16, IMMED16         |
| 82 | 1000 0010 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-8           | ADD REG8/MEM8, IMMED8            |
| 82 | 1000 0010 | MOD 001 R/M |                                        | (not used)                       |
| 82 | 1000 0010 | MOD 010 R/M | (DISP-LO), (DISP-HI), DATA-8           | ADC REG8/MEM8, IMMED8            |
| 82 | 1000 0010 | MOD 011 R/M | (DISP-LO), (DISP-HI), DATA-8           | SBB REG8/MEM8, IMMED8            |
| 82 | 1000 0010 | MOD 100 R/M |                                        | (not used)                       |
| 82 | 1000 0010 | MOD 101 R/M | (DISP-LO), (DISP-HI), DATA-8           | SUB REG8/MEM8, IMMED8            |
| 82 | 1000 0010 | MOD 110 R/M |                                        | (not used)                       |
| 82 | 1000 0010 | MOD 111 R/M | (DISP-LO), (DISP-HI), DATA-8           | CMP REG8/MEM8, IMMED8            |
| 83 | 1000 0011 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-SX          | ADD REG16/MEM16, IMMED8          |
| 83 | 1000 0011 | MOD 001 R/M |                                        | (not used)                       |
| 83 | 1000 0011 | MOD 010 R/M | (DISP-LO), (DISP-HI), DATA-SX          | ADC REG16/MEM16, IMMED8          |
| 83 | 1000 0011 | MOD 011 R/M | (DISP-LO), (DISP-HI), DATA-SX          | SBB REG16/MEM16, IMMED8          |
| 83 | 1000 0011 | MOD 100 R/M |                                        | (not used)                       |
| 83 | 1000 0011 | MOD 101 R/M | (DISP-LO), (DISP-HI), DATA-SX          | SUB REG16/MEM16, IMMED8          |
| 83 | 1000 0011 | MOD 110 R/M |                                        | (not used)                       |
| 83 | 1000 0011 | MOD 111 R/M | (DISP-LO), (DISP-HI), DATA-SX          | CMP REG16/MEM16, IMMED8          |
| 84 | 1000 0100 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | TEST REG8/MEM8, REG8             |
| 85 | 1000 0101 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | TEST REG16/MEM16, REG16          |
| 86 | 1000 0110 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | XCHG REG8, REG8/MEM8             |
| 87 | 1000 0111 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | XCHG REG16, REG16/MEM16          |
| 88 | 1000 1000 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | MOV REG8/MEM8, REG8              |
| 89 | 1000 1001 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | MOV REG16/MEM16, REG16           |
| 8A | 1000 1010 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | MOV REG8, REG8/MEM8              |
| 8B | 1000 1011 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | MOV REG16, REG16/MEM16           |
| 8C | 1000 1100 | MOD 0SRR/M  | (DISP-LO), (DISP-HI)                   | MOV REG16/MEM16, SEGREG          |
| 8C | 1000 1100 | MOD 1--R/M  |                                        | (not used)                       |
| 8D | 1000 1101 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | LEA REG16, MEM16                 |
| 8E | 1000 1110 | MOD 0SRR/M  | (DISP-LO), (DISP-HI)                   | MOV SEGREG, REG16/MEM16          |
| 8E | 1000 1110 | MOD 1--R/M  |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | POP REG16/MEM16                  |
| 8F | 1000 1111 | MOD 001 R/M |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 010 R/M |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 011 R/M |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 100 R/M |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 101 R/M |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 110 R/M |                                        | (not used)                       |
| 8F | 1000 1111 | MOD 111 R/M |                                        | (not used)                       |
| 90 | 1001 0000 |             |                                        | NOP (exchange AX, AX)            |
| 91 | 1001 0001 |             |                                        | XCHG AX,CX                       |
| 92 | 1001 0010 |             |                                        | XCHG AX,DX                       |
| 93 | 1001 0011 |             |                                        | XCHG AX,BX                       |
| 94 | 1001 0100 |             |                                        | XCHG AX,SP                       |
| 95 | 1001 0101 |             |                                        | XCHG AX,BP                       |
| 96 | 1001 0110 |             |                                        | XCHG AX,SI                       |
| 97 | 1001 0111 |             |                                        | XCHG AX,DI                       |
| 98 | 1001 1000 |             |                                        | CBW                              |
| 99 | 1001 1001 |             |                                        | CWD                              |
| 9A | 1001 1010 | DISP-LO     | DISP-HI, SEG-LO, SEG-HI                | CALL FAR_PROC                    |
| 9B | 1001 1011 |             |                                        | WAIT                             |
| 9C | 1001 1100 |             |                                        | PUSHF                            |
| 9D | 1001 1101 |             |                                        | POPF                             |
| 9E | 1001 1110 |             |                                        | SAHF                             |
| 9F | 1001 1111 |             |                                        | LAHF                             |
| A0 | 1010 0000 | ADDR-LO     | ADDR-HI                                | MOV AL, MEM8                     |
| A1 | 1010 0001 | ADDR-LO     | ADDR-HI                                | MOV AX, MEM16                    |
| A2 | 1010 0010 | ADDR-LO     | ADDR-HI                                | MOV MEM8, AL                     |
| A3 | 1010 0011 | ADDR-LO     | ADDR-HI                                | MOV MEM16, AL                    |
| A4 | 1010 0100 |             |                                        | MOVS DEST-STR8,SRC-STR8          |
| A5 | 1010 0101 |             |                                        | MOVS DEST-STR16,SRC-STR16        |
| A6 | 1010 0110 |             |                                        | CMPS DEST-STR8,SRC-STR8          |
| A7 | 1010 0111 |             |                                        | CMPS DEST-STR16, SRC-STR16       |
| A8 | 1010 1000 | DATA-8      |                                        | TEST AL, IMMED8                  |
| A9 | 1010 1001 | DATA-LO     | DATA-HI                                | TEST AX, IMMED16                 |
| AA | 1010 1010 |             |                                        | STOS DEST-STR8                   |
| AB | 1010 1011 |             |                                        | STOS DEST-STR16                  |
| AC | 1010 1100 |             |                                        | LODS SRC-STR8                    |
| AD | 1010 1101 |             |                                        | LODS SRC-STR16                   |
| AE | 1010 1110 |             |                                        | SCAS DEST-STR8                   |
| AF | 1010 1111 |             |                                        | SCAS DEST-STR16                  |
| B0 | 1011 0000 | DATA-8      |                                        | MOV AL, IMMED8                   |
| B1 | 1011 0001 | DATA-8      |                                        | MOV CL, IMMED8                   |
| B2 | 1011 0010 | DATA-8      |                                        | MOV DL, IMMED8                   |
| B3 | 1011 1011 | DATA-8      |                                        | MOV BL, IMMED8                   |
| B4 | 1011 0100 | DATA-8      |                                        | MOV AH, IMMED8                   |
| B5 | 1011 0101 | DATA-8      |                                        | MOV CH, IMMED8                   |
| B6 | 1011 0110 | DATA-8      |                                        | MOV DH, IMMED8                   |
| B7 | 1011 0111 | DATA-8      |                                        | MOV BH, IMMED8                   |
| B8 | 1011 1000 | DATA-LO     | DATA-HI                                | MOV AX, IMMED16                  |
| B9 | 1011 1001 | DATA-LO     | DATA-HI                                | MOV CX, IMMED16                  |
| BA | 1011 1010 | DATA-LO     | DATA-HI                                | MOV DX, IMMED16                  |
| BB | 1011 1011 | DATA-LO     | DATA-HI                                | MOV BX, IMMED16                  |
| BC | 1011 1100 | DATA-LO     | DATA-HI                                | MOV SP, IMMED16                  |
| BD | 1011 1101 | DATA-LO     | DATA-HI                                | MOV BP, IMMED16                  |
| BE | 1011 1110 | DATA-LO     | DATA-HI                                | MOV SI, IMMED16                  |
| BF | 1011 1111 | DATA-LO     | DATA-HI                                | MOV DI, IMMED16                  |
| C0 | 1100 0000 |             |                                        | (not used)                       |
| C1 | 1100 0001 |             |                                        | (not used)                       |
| C2 | 1100 0010 | DATA-LO     | DATA-HI                                | RET IMMED16 (intraseg)           |
| C3 | 1100 0011 |             |                                        | RET (intrasegment)               |
| C4 | 1100 0100 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | LES REG16, MEM16                 |
| C5 | 1100 0101 | MOD REG R/M | (DISP-LO), (DISP-HI)                   | LDS REG16, MEM16                 |
| C6 | 1100 0110 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-8           | MOV MEM8, IMMED8                 |
| C6 | 1100 0110 | MOD 001 R/M |                                        | (not used)                       |
| C6 | 1100 0110 | MOD 010 R/M |                                        | (not used)                       |
| C6 | 1100 0110 | MOD 011 R/M |                                        | (not used)                       |
| C6 | 1100 0110 | MOD 100 R/M |                                        | (not used)                       |
| C6 | 1100 0110 | MOD 101 R/M |                                        | (not used)                       |
| C6 | 1100 0110 | MOD 110 R/M |                                        | (not used)                       |
| C6 | 1100 0110 | MOD 111 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | MOV MEM16, IMMED16               |
| C7 | 1100 0111 | MOD 001 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 010 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 011 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 100 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 101 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 110 R/M |                                        | (not used)                       |
| C7 | 1100 0111 | MOD 111 R/M |                                        | (not used)                       |
| C8 | 1100 1000 |             |                                        | (not used)                       |
| C9 | 1100 1001 |             |                                        | (not used)                       |
| CA | 1100 1010 | DATA-LO     | DATA-HI                                | RET IMMED16 (intersegment)       |
| CB | 1100 1011 |             |                                        | RET (intersegment)               |
| CC | 1100 1100 |             |                                        | INT 3                            |
| CD | 1100 1101 | DATA-8      |                                        | INT IMMED8                       |
| CE | 1100 1110 |             |                                        | INTO                             |
| CF | 1100 1111 |             |                                        | IRET                             |
| D0 | 1101 0000 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | ROL REG8/MEM8,1                  |
| D0 | 1101 0000 | MOD 001 R/M | (DISP-LO), (DISP-HI)                   | ROR REG8/MEM8,1                  |
| D0 | 1101 0000 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | RCL REG8/MEM8,1                  |
| D0 | 1101 0000 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | RCR REG8/MEM8,1                  |
| D0 | 1101 0000 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | SAL/SHL REG8/MEM8,1              |
| D0 | 1101 0000 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | SHR REG8/MEM8,1                  |
| D0 | 1101 0000 | MOD 110 R/M |                                        | (not used)                       |
| D0 | 1101 0000 | MOD 111 R/M | (DISP-LO), (DISP-HI)                   | SAR REG8/MEM8,1                  |
| D1 | 1101 0001 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | ROL REG16/MEM16,1                |
| D1 | 1101 0001 | MOD 001 R/M | (DISP-LO), (DISP-HI)                   | ROR REG16/MEM16,1                |
| D1 | 1101 0001 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | RCL REG16/MEM16,1                |
| D1 | 1101 0001 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | RCR REG16/MEM16,1                |
| D1 | 1101 0001 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | SAL/SHL REG16/MEM16,1            |
| D1 | 1101 0001 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | SHR REG16/MEM16,1                |
| D1 | 1101 0001 | MOD 110 R/M |                                        | (not used)                       |
| D1 | 1101 0001 | MOD 111 R/M | (DISP-LO), (DISP-HI)                   | SAR REG16/MEM16,1                |
| D2 | 1101 0010 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | ROL REG8/MEM8, CL                |
| D2 | 1101 0010 | MOD 001 R/M | (DISP-LO), (DISP-HI)                   | ROR REG8/MEM8, CL                |
| D2 | 1101 0010 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | RCL REG8/MEM8, CL                |
| D2 | 1101 0010 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | RCR REG8/MEM8, CL                |
| D2 | 1101 0010 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | SAL/SHL REG8/MEM8,CL             |
| D2 | 1101 0010 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | SHR REG8/MEM8, CL                |
| D2 | 1101 0010 | MOD 110 R/M |                                        | (not used)                       |
| D2 | 1101 0010 | MOD 111 R/M | (DISP-LO), (DISP-HI)                   | SAR REG8/MEM8, CL                |
| D3 | 1101 0011 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | ROL REG16/MEM16,CL               |
| D3 | 1101 0011 | MOD 001 R/M | (DISP-LO), (DISP-HI)                   | ROR REG16/MEM16,CL               |
| D3 | 1101 0011 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | RCL REG16/MEM16,CL               |
| D3 | 1101 0011 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | RCR REG16/MEM16,CL               |
| D3 | 1101 0011 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | SAL/SHL REG16/MEM16, CL          |
| D3 | 1101 0011 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | SHR REG16/MEM16,CL               |
| D3 | 1101 0011 | MOD 110 R/M |                                        | (not used)                       |
| D3 | 1101 0011 | MOD 111 R/M | (DISP-LO), (DISP-HI)                   | SAR REG16/MEM16,CL               |
| D4 | 1101 0100 | 00001010    |                                        | AAM                              |
| D5 | 1101 0101 | 00001010    |                                        | AAD                              |
| D6 | 1101 0110 |             |                                        | (not used)                       |
| D7 | 1101 0111 |             |                                        | XLAT SOURCE-TABLE                |
| D8 | 1101 1000 | MOD 000 R/M |                                        | (not used)                       |
|    | 1XXX      | MOD YYY R/M | (DISP-LO), (DISP-HI)                   | ESC OPCODE, SOURCE               |
| DF | 1101 1111 | MOD 111 R/M |                                        | (not used)                       |
| E0 | 1110 0000 | IP-INC-8    |                                        | LOOPNE/SHORT-LABEL LOOPNZ        |
| E1 | 1110 0001 | IP-INC-8    |                                        | LOOPE/SHORT-LABEL LOOPZ          |
| E2 | 1110 0010 | IP-INC-8    |                                        | LOOP SHORT-LABEL                 |
| E3 | 1110 0011 | IP-INC-8    |                                        | JCXZ SHORT-LABEL                 |
| E4 | 1110 0100 | DATA-8      |                                        | IN AL, IMMED8                    |
| E5 | 1110 0101 | DATA-8      |                                        | IN AX, IMMED8                    |
| E6 | 1110 0110 | DATA-8      |                                        | OUT AL, IMMED8                   |
| E7 | 1110 0111 | DATA-8      |                                        | OUT AX, IMMED8                   |
| E8 | 1110 1000 | IP-INC-LO   | IP-INC-HI                              | CALL NEAR-PROC                   |
| E9 | 1110 1001 | IP-INC-LO   | IP-INC-HI                              | JMP NEAR-LABEL                   |
| EA | 1110 1010 | IP-LO       | IP-HI, CS-LO,CS-HI                     | JMP FAR-LABEL                    |
| EB | 1110 1011 | IP-INC8     |                                        | JMP SHORT-LABEL                  |
| EC | 1110 1100 |             |                                        | IN AL,DX                         |
| ED | 1110 1101 |             |                                        | IN AX,DX                         |
| EE | 1110 1110 |             |                                        | OUT AL, DX                       |
| EF | 1110 1111 |             |                                        | OUT AX,DX                        |
| F0 | 1111 0000 |             |                                        | LOCK (prefix)                    |
| F1 | 1111 0001 |             |                                        | (not used)                       |
| F2 | 1111 0010 |             |                                        | REPNE/REPNZ                      |
| F3 | 1111 0011 |             |                                        | REP/REPE/REPZ                    |
| F4 | 1111 0100 |             |                                        | HLT                              |
| F5 | 1111 0101 |             |                                        | CMC                              |
| F6 | 1111 0110 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-8           | TEST REG8/MEM8, IMMED8           |
| F6 | 1111 0110 | MOD 001 R/M |                                        | (not used)                       |
| F6 | 1111 0110 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | NOT REG8/MEM8                    |
| F6 | 1111 0110 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | NEG REG8/MEM8                    |
| F6 | 1111 0110 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | MUL REG8/MEM8                    |
| F6 | 1111 0110 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | IMUL REG8/MEM8                   |
| F6 | 1111 0110 | MOD 110 R/M | (DISP-LO), (DISP-HI)                   | DIV REG8/MEM8                    |
| F6 | 1111 0110 | MOD 111 R/M | (DISP-LO), (DISP-HI)                   | IDIV REG8/MEM8                   |
| F7 | 1111 0111 | MOD 000 R/M | (DISP-LO), (DISP-HI), DATA-LO, DATA-HI | TEST REG16/MEM16, IMMED16        |
| F7 | 1111 0111 | MOD 001 R/M |                                        | (not used)                       |
| F7 | 1111 0111 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | NOT REG16/MEM16                  |
| F7 | 1111 0111 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | NEG REG16/MEM16                  |
| F7 | 1111 0111 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | MUL REG16/MEM16                  |
| F7 | 1111 0111 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | IMUL REG16/MEM16                 |
| F7 | 1111 0111 | MOD 110 R/M | (DISP-LO), (DISP-HI)                   | DIV REG16/MEM16                  |
| F7 | 1111 0111 | MOD 111 R/M | (DISP-LO), (DISP-HI)                   | IDIV REG16/MEM16                 |
| F8 | 1111 1000 |             |                                        | CLC                              |
| F9 | 1111 1001 |             |                                        | STC                              |
| FA | 1111 1010 |             |                                        | CLI                              |
| FB | 1111 1011 |             |                                        | STI                              |
| FC | 1111 1100 |             |                                        | CLD                              |
| FD | 1111 1101 |             |                                        | STD                              |
| FE | 1111 1110 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | INC REG8/MEM8                    |
| FE | 1111 1110 | MOD 001 R/M | (DISP-LO), (DISP-HI)                   | DEC REG8/MEM8                    |
| FE | 1111 1110 | MOD 010 R/M |                                        | (not used)                       |
| FE | 1111 1110 | MOD 011 R/M |                                        | (not used)                       |
| FE | 1111 1110 | MOD 100 R/M |                                        | (not used)                       |
| FE | 1111 1110 | MOD 101 R/M |                                        | (not used)                       |
| FE | 1111 1110 | MOD 110 R/M |                                        | (not used)                       |
| FE | 1111 1110 | MOD 111 R/M |                                        | (not used)                       |
| FF | 1111 1111 | MOD 000 R/M | (DISP-LO), (DISP-HI)                   | INC MEM16                        |
| FF | 1111 1111 | MOD 001 R/M | (DISP-LO), (DISP-HI)                   | DEC MEM16                        |
| FF | 1111 1111 | MOD 010 R/M | (DISP-LO), (DISP-HI)                   | CALL REG16/MEM16 (intra)         |
| FF | 1111 1111 | MOD 011 R/M | (DISP-LO), (DISP-HI)                   | CALL MEM16 (intersegment)        |
| FF | 1111 1111 | MOD 100 R/M | (DISP-LO), (DISP-HI)                   | JMP REG16/MEM16 (intra)          |
| FF | 1111 1111 | MOD 101 R/M | (DISP-LO), (DISP-HI)                   | JMP MEM16 (intersegment)         |
| FF | 1111 1111 | MOD 110 R/M | (DISP-LO), (DISP-HI)                   | PUSH MEM16                       |
| FF | 1111 1111 | MOD 111 R/M |                                        | (not used)                       |