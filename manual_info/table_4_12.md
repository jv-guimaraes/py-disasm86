### Table 4-12. 8086 Instruction Encoding

| MOV = Move | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Register/memory to/from register | 1 0 0 0 1 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate to register/memory | 1 1 0 0 0 1 1 w | mod 0 0 0 r/m | (DISP-LO) | (DISP-HI) | data | data if w = 1 |
| Immediate to register | 1 0 1 1 w reg | data | data if w = 1 |  |  |  |
| Memory to accumulator | 1 0 1 0 0 0 0 w | addr-lo | addr-hi |  |  |  |
| Accumulator to memory | 1 0 1 0 0 0 1 w | addr-lo | addr-hi |  |  |  |
| Register/memory to segment register | 1 0 0 0 1 1 1 0 | mod 0 SR r/m | (DISP-LO) | (DISP-HI) |  |  |
| Segment register to register/memory | 1 0 0 0 1 1 0 0 | mod 0 SR r/m | (DISP-LO) | (DISP-HI) |  |  |

| PUSH = Push | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| Register/memory | 1 1 1 1 1 1 1 1 | mod 1 1 0 r/m | (DISP-LO) | (DISP-HI) |  |
| Register | 0 1 0 1 0 reg |  |  |  |  |
| Segment register | 0 0 0 reg 1 1 0 |  |  |  |  |

| POP = Pop | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| Register/memory | 1 0 0 0 1 1 1 1 | mod 0 0 0 r/m | (DISP-LO) | (DISP-HI) |  |
| Register | 0 1 0 1 1 reg |  |  |  |  |
| Segment register | 0 0 0 reg 1 1 1 |  |  |  |  |

| XCHG = Exchange | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 |
|---|---|---|---|---|
| Register/memory with register | 1 0 0 0 0 1 1 w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |
| Register with accumulator | 1 0 0 1 0 reg |  |  |  |

| IN = Input from | BYTE 1 | BYTE 2 | BYTE 3 |
|---|---|---|---|
| Fixed port | 1 1 1 0 0 1 0 w | DATA-8 |  |
| Variable port | 1 1 1 0 1 1 0 w |  |  |

| OUT = Output to | BYTE 1 | BYTE 2 | BYTE 3 |
|---|---|---|---|
| Fixed port | 1 1 1 0 0 1 1 w | DATA-8 |  |
| Variable port | 1 1 1 0 1 1 1 w |  |  |

| Function | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 |
|---|---|---|---|---|
| XLAT = Translate byte to AL | 1 1 0 1 0 1 1 1 |  |  |  |
| LEA = Load EA to register | 1 0 0 0 1 1 0 1 | mod reg r/m | (DISP-LO) | (DISP-HI) |
| LDS = Load pointer to DS | 1 1 0 0 0 1 0 1 | mod reg r/m | (DISP-LO) | (DISP-HI) |
| LES = Load pointer to ES | 1 1 0 0 0 1 0 0 | mod reg r/m | (DISP-LO) | (DISP-HI) |
| LAHF = Load AH with flags | 1 0 0 1 1 1 1 1 |  |  |  |
| SAHF = Store AH into flags | 1 0 0 1 1 1 1 0 |  |  |  |
| PUSHF = Push flags | 1 0 0 1 1 1 0 0 |  |  |  |
| POPF = Pop flags | 1 0 0 1 1 1 0 1 |  |  |  |

| ADD = Add | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory with register to either | 0 0 0 0 0 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate to register/memory | 1 0 0 0 0 0 s w | mod 0 0 0 r/m | (DISP-LO) | (DISP-HI) | data | data if s: w=01 |
| Immediate to accumulator | 0 0 0 0 0 1 0 w | data | data if w=1 |  |  |  |

| ADC = Add with carry | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory with register to either | 0 0 0 1 0 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate to register/memory | 1 0 0 0 0 0 s w | mod 0 1 0 r/m | (DISP-LO) | (DISP-HI) | data | data if s: w=01 |
| Immediate to accumulator | 0 0 0 1 0 1 0 w | data | data if w=1 |  |  |  |

| INC = Increment | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| Register/memory | 1 1 1 1 1 1 1 1 | mod 0 0 0 r/m | (DISP-LO) | (DISP-HI) |  |
| Register | 0 1 0 0 0 reg |  |  |  |  |
| AAA = ASCII adjust for add | 0 0 1 1 0 1 1 1 |  |  |  |  |
| DAA = Decimal adjust for add | 0 0 1 0 0 1 1 1 |  |  |  |  |

| SUB = Subtract | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory and register to either | 0 0 1 0 1 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate from register/memory | 1 0 0 0 0 0 s w | mod 1 0 1 r/m | (DISP-LO) | (DISP-HI) | data | data if s: w=01 |
| Immediate from accumulator | 0 0 1 0 1 1 0 w | data | data if w=1 |  |  |  |

| SBB = Subtract with borrow | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory and register to either | 0 0 0 1 1 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate from register/memory | 1 0 0 0 0 0 s w | mod 0 1 1 r/m | (DISP-LO) | (DISP-HI) | data | data if s: w=01 |
| Immediate from accumulator | 0 0 0 1 1 1 0 w | data | data if w=1 |  |  |  |

| DEC Decrement | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| Register/memory | 1 1 1 1 1 1 1 1 | mod 0 0 1 r/m | (DISP-LO) | (DISP-HI) |  |
| Register | 0 1 0 0 1 reg |  |  |  |  |
| NEG Change sign | 1 1 1 1 0 1 1 w | mod 0 1 1 r/m | (DISP-LO) | (DISP-HI) |  |

| CMP = Compare | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Register/memory and register | 0 0 1 1 1 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate with register/memory | 1 0 0 0 0 0 s w | mod 1 1 1 r/m | (DISP-LO) | (DISP-HI) | data | data if s: w=1 |
| Immediate with accumulator | 0 0 1 1 1 1 0 w | data |  |  |  |  |

| Operation | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| AAS Ascii adjust for subtract | 0 0 1 1 1 1 1 1 |  |  |  |  |  |
| DAS Decimal adjust for subtract | 0 0 1 0 1 1 1 1 |  |  |  |  |  |
| MUL Multiply (unsigned) | 1 1 1 1 0 1 1 w | mod 1 0 0 r/m | (DISP-LO) | (DISP-HI) |  |  |
| IMUL Integer multiply (signed) | 1 1 1 1 0 1 1 w | mod 1 0 1 r/m | (DISP-LO) | (DISP-HI) |  |  |
| AAM ASCII adjust for multiply | 1 1 0 1 0 1 0 0 | 0 0 0 0 1 0 1 0 | (DISP-LO) | (DISP-HI) |  |  |
| DIV Divide (unsigned) | 1 1 1 1 0 1 1 w | mod 1 1 0 r/m | (DISP-LO) | (DISP-HI) |  |  |
| IDIV Integer divide (signed) | 1 1 1 1 0 1 1 w | mod 1 1 1 r/m | (DISP-LO) | (DISP-HI) |  |  |
| AAD ASCII adjust for divide | 1 1 0 1 0 1 0 1 | 0 0 0 0 1 0 1 0 | (DISP-LO) | (DISP-HI) |  |  |
| CBW Convert byte to word | 1 0 0 1 1 0 0 0 |  |  |  |  |  |
| CWD Convert word to double word | 1 0 0 1 1 0 0 1 |  |  |  |  |  |

| Operation | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| NOT Invert | 1 1 1 1 0 1 1 w | mod 0 1 0 r/m | (DISP-LO) | (DISP-HI) |  |
| SHL/SAL Shift logical/arithmetic left | 1 1 0 1 0 0 0 v w | mod 1 0 0 r/m | (DISP-LO) | (DISP-HI) |  |
| SHR Shift logical right | 1 1 0 1 0 0 0 v w | mod 1 0 1 r/m | (DISP-LO) | (DISP-HI) |  |
| SAR Shift arithmetic right | 1 1 0 1 0 0 0 v w | mod 1 1 1 r/m | (DISP-LO) | (DISP-HI) |  |
| ROL Rotate left | 1 1 0 1 0 0 0 v w | mod 0 0 0 r/m | (DISP-LO) | (DISP-HI) |  |
| ROR Rotate right | 1 1 0 1 0 0 0 v w | mod 0 0 1 r/m | (DISP-LO) | (DISP-HI) |  |
| RCL Rotate through carry flag left | 1 1 0 1 0 0 0 v w | mod 0 1 0 r/m | (DISP-LO) | (DISP-HI) |  |
| RCR Rotate through carry right | 1 1 0 1 0 0 0 v w | mod 0 1 1 r/m | (DISP-LO) | (DISP-HI) |  |

| AND = And | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory with register to either | 0 0 1 0 0 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate to register/memory | 1 0 0 0 0 0 s w | mod 1 0 0 r/m | (DISP-LO) | (DISP-HI) | data | data if w=1 |
| Immediate to accumulator | 0 0 1 0 0 1 0 w | data | data if w=1 |  |  |  |

| TEST = And function to flags no result | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Register/memory and register | 0 0 0 0 1 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate data and register/memory | 1 1 1 1 0 1 1 w | mod 0 0 0 r/m | (DISP-LO) | (DISP-HI) | data | data if w=1 |
| Immediate data and accumulator | 1 0 1 0 1 0 0 w | data |  |  |  |  |

| OR = Or | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory and register to either | 0 0 0 0 1 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate to register/memory | 1 0 0 0 0 0 s w | mod 0 0 1 r/m | (DISP-LO) | (DISP-HI) | data | data if w=1 |
| Immediate to accumulator | 0 0 0 0 1 1 0 w | data | data if w=1 |  |  |  |

| XOR = Exclusive or | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 | BYTE 6 |
|---|---|---|---|---|---|---|
| Reg/memory and register to either | 0 0 1 1 0 0 0 d w | mod reg r/m | (DISP-LO) | (DISP-HI) |  |  |
| Immediate to register/memory | 0 0 1 1 0 1 0 w | data | (DISP-LO) | (DISP-HI) | data | data if w=1 |
| Immediate to accumulator | 0 0 1 1 0 1 0 w | data | data if w=1 |  |  |  |

| String Operations | BYTE 1 |
|---|---|
| REP = Repeat | 1 1 1 1 0 0 1 z |
| MOVS = Move byte/word | 1 0 1 0 0 1 0 w |
| CMPS = Compare byte/word | 1 0 1 0 0 1 1 w |
| SCAS = Scan byte/word | 1 0 1 0 1 1 1 w |
| LODS = Load byte/wd to AL/AX | 1 0 1 0 1 1 0 w |
| STDS = Stor byte/wd from AL/A | 1 0 1 0 1 0 1 w |

| CALL = Call | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| Direct within segment | 1 1 1 0 1 0 0 0 | IP-INC-LO | IP-INC-HI |  |  |
| Indirect within segment | 1 1 1 1 1 1 1 1 | mod 0 1 0 r/m | (DISP-LO) | (DISP-HI) |  |
| Direct intersegment | 1 0 0 1 1 0 1 0 | IP-lo / CS-lo | IP-hi / CS-hi |
| Indirect intersegment | 1 1 1 1 1 1 1 1 | mod 0 1 1 r/m | (DISP-LO) | (DISP-HI) |  |

| JMP = Unconditional Jump | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 | BYTE 5 |
|---|---|---|---|---|---|
| Direct within segment | 1 1 1 0 1 0 0 1 | IP-INC-LO | IP-INC-HI |  |  |
| Direct within segment-short | 1 1 1 0 1 0 1 1 | IP-INC8 |  |  |  |
| Indirect within segment | 1 1 1 1 1 1 1 1 | mod 1 0 0 r/m | (DISP-LO) | (DISP-HI) |  |
| Direct intersegment | 1 1 1 0 1 0 1 0 | IP-lo / CS-lo | IP-hi / CS-hi
| Indirect intersegment | 1 1 1 1 1 1 1 1 | mod 1 0 1 r/m | (DISP-LO) | (DISP-HI) |  |

| RET = Return from CALL | BYTE 1 | BYTE 2 | BYTE 3 |
|---|---|---|---|
| Within segment | 1 1 0 0 0 0 1 1 |  |  |
| Within seg adding immed to SP | 1 1 0 0 0 0 1 0 | data-lo | data-hi |
| Intersegment | 1 1 0 0 1 0 1 1 |  |  |
| Intersegment adding immediate to SP | 1 1 0 0 1 0 1 0 | data-lo | data-hi |

| Condition | BYTE 1 | BYTE 2 |
|---|---|---|
| JE/JZ = Jump on equal/zero | 0 1 1 1 0 1 0 0 | IP-INC8 |
| JL/JNGE = Jump on less/not greater or equal | 0 1 1 1 1 1 0 0 | IP-INC8 |
| JLE/JNG = Jump on less or equal/not greater | 0 1 1 1 1 1 1 0 | IP-INC8 |
| JB/JNAE = Jump on below/not above or equal | 0 1 1 1 0 0 1 0 | IP-INC8 |
| JBE/JNA = Jump on below or equal/not above | 0 1 1 1 0 1 1 0 | IP-INC8 |
| JP/JPE = Jump on parity/parity even | 0 1 1 1 1 0 1 0 | IP-INC8 |
| JO = Jump on overflow | 0 1 1 1 0 0 0 0 | IP-INC8 |
| JS = Jump on sign | 0 1 1 1 0 0 0 0 | IP-INC8 |
| JNE/JNZ = Jump on not equal/not zero | 0 1 1 1 0 1 0 1 | IP-INC8 |
| JNL/JGE = Jump on not less/greater or equal | 0 1 1 1 1 1 0 1 | IP-INC8 |
| JNLE/JG = Jump on not less or equal/greater | 0 1 1 1 1 1 1 1 | IP-INC8 |
| JNB/JAE = Jump on not below/above or equal | 0 1 1 1 0 0 1 1 | IP-INC8 |
| JNB/JAE = Jump on not below or equal/above | 0 1 1 1 0 1 1 1 | IP-INC8 |
| JNP/JPO = Jump on not par/par odd | 0 1 1 1 1 0 1 1 | IP-INC8 |
| JNO = Jump on not overflow | 0 1 1 1 0 0 0 1 | IP-INC8 |
| JNS = Jump on not sign | 0 1 1 1 1 0 0 1 | IP-INC8 |
| LOOP = Loop CX times | 1 1 1 0 0 0 1 0 | IP-INC8 |
| LOOPZ/LOOPE = Loop while zero/equal | 1 1 1 0 0 0 0 1 | IP-INC8 |
| LOOPNZ/LOOPNE = Loop while not zero/equal | 1 1 1 0 0 0 0 0 | IP-INC8 |
| JCXZ = Jump on CX zero | 1 1 1 0 0 0 1 1 | IP-INC8 |

| INT = Interrupt | BYTE 1 | BYTE 2 |
|---|---|---|
| Type specified | 1 1 0 0 1 1 0 1 | DATA-8 |
| Type 3 | 1 1 0 0 1 1 0 0 |  |
| INTO = Interrupt on overflow | 1 1 0 0 1 1 1 0 |  |
| IRET = Interrupt return | 1 1 0 0 1 1 1 1 |  |

| PROCESSOR CONTROL | BYTE 1 | BYTE 2 | BYTE 3 | BYTE 4 |
|---|---|---|---|---|
| CLC = Clear carry | 1 1 1 1 1 0 0 0 |  |  |  |
| CMC = Complement carry | 1 1 1 1 0 1 0 1 |  |  |  |
| STC = Set carry | 1 1 1 1 1 0 0 1 |  |  |  |
| CLD = Clear direction | 1 1 1 1 1 1 0 0 |  |  |  |
| STD = Set direction | 1 1 1 1 1 1 0 1 |  |  |  |
| CLI = Clear interrupt | 1 1 1 1 1 0 1 0 |  |  |  |
| STI = Set interrupt | 1 1 1 1 1 0 1 1 |  |  |  |
| HLT = Halt | 1 1 1 1 0 1 0 0 |  |  |  |
| WAIT = Wait | 1 0 0 1 1 0 1 1 |  |  |  |
| ESC = Escape (to external device) | 1 1 0 1 1 x x x | mod y y r/m | (DISP-LO) | (DISP-HI) |
| LOCK = Bus lock prefix | 1 1 1 1 0 0 0 0 |  |  |  |
| SEGMENT = Override prefix | 0 0 1 reg 1 1 0 |  |  |  |