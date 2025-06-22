| Field | Value | Function |
|---|---|---|
| S | 0 | No sign extension |
|   | 1 | Sign extend 8-bit immediate data to 16 bits if W=1 |
| W | 0 | Instruction operates on byte data |
|   | 1 | Instruction operates on word data |
| D | 0 | Instruction source is specified in REG field |
|   | 1 | Instruction destination is specified in REG field |
| V | 0 | Shift/rotate count is one |
|   | 1 | Shift/rotate count is specified in CL register |
| Z | 0 | Repeat/loop while zero flag is clear |
|   | 1 | Repeat/loop while zero flag is set |