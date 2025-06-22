| IDENTIFIER | EXPLANATION |
|---|---|
| MOD | Mode field |
| REG | Register field |
| R/M | Register/Memory field |
| SR | Segment register code: 00=ES, 01=CS, 10=SS, 11=DS. |
| W, S, D, V, Z | Single-bit instruction fields |
| DATA-8 | 8-bit immediate constant. |
| DATA-SX | 8-bit immediate value that is automatically sign-extended to 16-bits before use. |
| DATA-LO | Low-order byte of 16-bit immediate constant. |
| DATA-HI | High-order byte of 16-bit immediate constant. |
| (DISP-LO) | Low-order byte of optional 8- or 16-bit unsigned displacement; MOD indicates if present. |
| (DISP-HI) | High-order byte of optional 16-bit unsigned displacement; MOD indicates if present. |
| IP-LO | Low-order byte of new IP value. |
| IP-HI | High-order byte of new IP value. |
| CS-LO | Low-order byte of new CS value. |
| CS-HI | High-order byte of new CS value. |
| IP-INC8 | 8-bit signed increment to instruction pointer. |
| IP-INC-LO | Low-order byte of signed 16-bit instruction pointer increment. |
| IP-INC-HI | High-order byte of signed 16-bit instruction pointer increment. |
| ADDR-LO | Low-order byte of direct address (offset) of memory operand; EA not calculated. |
| ADDR-HI | High-order byte of direct address (offset) of memory operand; EA not calculated. |
| --- | Bits may contain any value. |
| XXX | First 3 bits of ESC opcode. |
| YYY | Second 3 bits of ESC opcode. |
| REG8 | 8-bit general register operand. |
| REG16 | 16-bit general register operand. |
| MEM8 | 8-bit memory operand (any addressing mode). |
| MEM16 | 16-bit memory operand (any addressing mode). |
| IMMED8 | 8-bit immediate operand. |
| IMMED16 | 16-bit immediate operand. |
| SEGREG | Segment register operand. |
| DEST-STR8 | Byte string addressed by DI. |
| SRC-STR8 | Byte string addressed by SI. |
| DEST-STR16 | Word string addressed by DI. |
| SRC-STR16 | Word string addressed by SI. |
| SHORT-LABEL | Label within +- 127 bytes of instruction. |
| NEAR-PROC | Procedure in current code segment. |
| FAR-PROC | Procedure in another code segment. |
| NEAR-LABEL | Label in current code segment but farther than $-128$ to $+127$ bytes from instruction. |
| FAR-LABEL | Label in another code segment. |
| SOURCE-TABLE | XLAT translation table addressed by BX. |
| OPCODE | ESC opcode operand. |
| SOURCE | ESC register or memory operand. |