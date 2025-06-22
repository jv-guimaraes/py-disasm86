import argparse
import sys
from typing import Dict, Tuple, Optional, List

REG_FIELD_MAP = {
    0: {0b000:'al', 0b001:'cl', 0b010:'dl', 0b011:'bl', 0b100:'ah', 0b101:'ch', 0b110:'dh', 0b111:'bh'},
    1: {0b000:'ax', 0b001:'cx', 0b010:'dx', 0b011:'bx', 0b100:'sp', 0b101:'bp', 0b110:'si', 0b111:'di'}
}

SEG_REG_MAP = {0b00:"es", 0b01:"cs", 0b10:"ss", 0b11:"ds"}

EFFECTIVE_ADDRESS_CALCULATION = {
    0b000:"[bx+si]", 0b001:"[bx+di]", 0b010:"[bp+si]", 0b011:"[bp+di]",
    0b100:"[si]",    0b101:"[di]",    0b110:"[bp]",    0b111:"[bx]",
}

GROUP_OPCODE_MAP = {
    0x80: {0b000:"add", 0b001:"or", 0b010:"adc", 0b011:"sbb", 0b100:"and", 0b101:"sub", 0b110:"xor", 0b111:"cmp"},
    0x81: {0b000:"add", 0b001:"or", 0b010:"adc", 0b011:"sbb", 0b100:"and", 0b101:"sub", 0b110:"xor", 0b111:"cmp"},
    0x82: {0b000:"add", 0b010:"adc", 0b011:"sbb", 0b101:"sub", 0b111:"cmp"},
    0x83: {0b000:"add", 0b001:"or", 0b010:"adc", 0b011:"sbb", 0b100:"and", 0b101:"sub", 0b110:"xor", 0b111:"cmp"},
    0x8f: {0b000:"pop"},
    0xf6: {0b000:"test", 0b010:"not", 0b011:"neg", 0b100:"mul", 0b101:"imul", 0b110:"div", 0b111:"idiv"},
    0xf7: {0b000:"test", 0b010:"not", 0b011:"neg", 0b100:"mul", 0b101:"imul", 0b110:"div", 0b111:"idiv"},
    0xfe: {0b000:"inc", 0b001:"dec"},
    0xff: {0b000:"inc", 0b001:"dec", 0b010:"call", 0b011:"call", 0b100:"jmp", 0b101:"jmp", 0b110:"push"},
}

SHIFT_ROTATE_MAP = {
    0b000:"rol", 0b001:"ror", 0b010:"rcl", 0b011:"rcr", 0b100:"shl", 0b101:"shr", 0b111:"sar"
}

JUMP_MNEMONICS = {
    0x70:"jo", 0x71:"jno", 0x72:"jb", 0x73:"jnb", 0x74:"jz", 0x75:"jnz", 0x76:"jbe", 0x77:"ja",
    0x78:"js", 0x79:"jns", 0x7a:"jp", 0x7b:"jnp", 0x7c:"jl", 0x7d:"jge", 0x7e:"jle", 0x7f:"jg",
    0xe0:"loopne", 0xe1:"loope", 0xe2:"loop", 0xe3:"jcxz"
}

SINGLE_BYTE_MNEMONICS = {
    0x27: "daa", 0x2f: "das", 0x37: "aaa", 0x3f: "aas",
    0x90: "nop", 0x98: "cbw", 0x99: "cwd", 0x9b: "wait",
    0x9c: "pushf", 0x9d: "popf", 0x9e: "sahf", 0x9f: "lahf",
    0xa4: "movsb", 0xa5: "movsw", 0xa6: "cmpsb", 0xa7: "cmpsw",
    0xaa: "stosb", 0xab: "stosw", 0xac: "lodsb", 0xad: "lodsw",
    0xae: "scasb", 0xaf: "scasw", 0xc3: "ret", 0xcb: "retf",
    0xcc: "int3", 0xce: "into", 0xcf: "iret", 0xd7: "xlatb",
    0xf4: "hlt", 0xf5: "cmc", 0xf8: "clc", 0xf9: "stc",
    0xfa: "cli", 0xfb: "sti", 0xfc: "cld", 0xfd: "std"
}

def get_rm_string(mod: int, rm: int, data: bytes) -> Tuple[Optional[str], int]:
    if mod == 0b11: return None, 0
    
    if mod == 0b00 and rm == 0b110:
        if len(data) < 2: return "INVALID", 0
        addr_val = int.from_bytes(data[:2], 'little')
        return f"[{addr_val:#x}]", 2
    
    if mod == 0b00:
        return EFFECTIVE_ADDRESS_CALCULATION[rm], 0

    disp_bytes = 1 if mod == 0b01 else 2
    if len(data) < disp_bytes: return "INVALID", 0
    
    disp_val = int.from_bytes(data[:disp_bytes], 'little', signed=True)
    addr = EFFECTIVE_ADDRESS_CALCULATION[rm]
    sign = "+" if disp_val >= 0 else "-"
    return f"{addr[:-1]}{sign}0x{abs(disp_val):x}]", disp_bytes

def disassemble_reg_mem_instruction(mnemonic: str, data: bytes) -> Tuple[str, int]:
    opcode, mod_rm_byte = data[0], data[1]
    
    is_lea_lds_les = mnemonic in ["lea", "lds", "les"]
    d, w = (1, 1) if is_lea_lds_les else ((opcode >> 1) & 1, opcode & 1)
    
    mod, reg_code, rm_code = (mod_rm_byte >> 6) & 3, (mod_rm_byte >> 3) & 7, mod_rm_byte & 7
    reg_operand = REG_FIELD_MAP[w][reg_code]
    
    if mod == 0b11:
        if is_lea_lds_les: return "INVALID", 2
        rm_operand, disp_bytes = REG_FIELD_MAP[w][rm_code], 0
    else:
        rm_operand, disp_bytes = get_rm_string(mod, rm_code, data[2:])

    length = 2 + disp_bytes
    
    if mnemonic == "xchg":
        return f"xchg {rm_operand},{reg_operand}", length

    op1, op2 = (reg_operand, rm_operand) if d == 1 else (rm_operand, reg_operand)
    return f"{mnemonic} {op1},{op2}", length

def disassemble_immediate_to_acc_instruction(mnemonic: str, data: bytes) -> Tuple[str, int]:
    w = data[0] & 1
    length = 2 if w == 0 else 3
    if len(data) < length: return "INVALID", length
    
    imm = data[1] if w == 0 else int.from_bytes(data[1:3], 'little')
    return f"{mnemonic} {'al' if w==0 else 'ax'},{imm:#x}", length

def disassemble_group_instruction(opcode: int, data: bytes) -> Tuple[str, int]:
    w = 1 if opcode in [0x8f, 0xff] or (opcode & 1) else opcode & 1
    s = (opcode >> 1) & 1 if opcode in [0x80, 0x81, 0x83] else 0

    length, mod_rm_byte = 2, data[1]
    mod, op_ext, rm_code = (mod_rm_byte >> 6) & 3, (mod_rm_byte >> 3) & 7, mod_rm_byte & 7
    
    if not (mnemonic := GROUP_OPCODE_MAP.get(opcode, {}).get(op_ext)):
        return f"db {opcode:#04x}", 1
    
    if mod == 0b11:
        operand = REG_FIELD_MAP[w][rm_code]
        disp_bytes = 0
    else:
        mem_op, disp_bytes = get_rm_string(mod, rm_code, data[2:])
        prefix = "" if mnemonic in ["call", "jmp"] else ("word " if w == 1 else "byte ")
        operand = f"{prefix}{mem_op}"
    length += disp_bytes
    
    takes_imm = opcode in [0x80, 0x81, 0x82, 0x83] or (opcode in [0xf6, 0xf7] and op_ext == 0)
    if takes_imm:
        operand_str = operand if mod != 0b11 else REG_FIELD_MAP[w][rm_code]
        imm_bytes = 1 if (s == 0 and w == 0) or opcode in [0x83, 0xf6] else 2
        
        if len(data) < length + imm_bytes: return "INVALID", length
        imm_val = int.from_bytes(data[length:length+imm_bytes], 'little', signed=(opcode == 0x83))
        length += imm_bytes

        if opcode == 0x83:
            sign = "+" if imm_val >= 0 else "-"
            return f"{mnemonic} {operand_str},byte {sign}0x{abs(imm_val):x}", length
        return f"{mnemonic} {operand_str},{imm_val:#x}", length

    if op_ext in [0b011, 0b101] and mnemonic in ["call", "jmp"]:
        return f"{mnemonic} far {operand.replace('word ', '')}", length

    return f"{mnemonic} {operand}", length

def disassemble_shift_rotate_instruction(data: bytes) -> Tuple[str, int]:
    opcode, mod_rm_byte = data[0], data[1]
    v, w = (opcode >> 1) & 1, opcode & 1
    mod, op_ext, rm_code = (mod_rm_byte >> 6) & 3, (mod_rm_byte >> 3) & 7, mod_rm_byte & 7

    if not (mnemonic := SHIFT_ROTATE_MAP.get(op_ext)):
         return f"db {opcode:#04x}", 1
    
    count_operand = "cl" if v == 1 else "1"
    
    if mod == 0b11:
        operand, disp_bytes = REG_FIELD_MAP[w][rm_code], 0
    else:
        mem_op, disp_bytes = get_rm_string(mod, rm_code, data[2:])
        operand = f"{'word ' if w == 1 else 'byte '}{mem_op}"
        
    return f"{mnemonic} {operand},{count_operand}", 2 + disp_bytes

def disassemble_jump_instruction(mnemonic: str, data: bytes, origin: int) -> Tuple[str, int]:
    length, disp = 2, int.from_bytes(data[1:2], 'little', signed=True)
    return f"{mnemonic} short {origin + length + disp:#x}", length

def _disassemble_instruction(data: bytes, origin: int) -> Tuple[str, int]:
    if not data: return "No data", 0
    opcode = data[0]

    if mnemonic := SINGLE_BYTE_MNEMONICS.get(opcode):
        return mnemonic, 1

    if (opcode & 0b11100110) == 0b00000110:
        if opcode == 0x0f: return f"db {opcode:#04x}", 1
        sreg = SEG_REG_MAP[(opcode >> 3) & 3]
        mnemonic = "push" if (opcode & 1) == 0 else "pop"
        return f"{mnemonic} {sreg}", 1

    if opcode in [0xc6, 0xc7]:
        w = opcode & 1
        mod, op_ext, rm_code = (data[1] >> 6) & 3, (data[1] >> 3) & 7, data[1] & 7
        if op_ext != 0: return f"db {opcode:#04x}", 1

        if mod == 0b11:
             rm_op, disp_bytes = REG_FIELD_MAP[w][rm_code], 0
             prefix = ""
        else:
            rm_op, disp_bytes = get_rm_string(mod, rm_code, data[2:])
            prefix = "word " if w == 1 else "byte "
            
        operand = f"{prefix}{rm_op}"
        length = 2 + disp_bytes
        imm_bytes = 1 if w == 0 else 2
        if len(data) < length + imm_bytes: return "INVALID", length
        imm_val = int.from_bytes(data[length:length+imm_bytes], 'little')
        return f"mov {operand},{imm_val:#x}", length + imm_bytes
    
    if opcode in [0x86, 0x87]:
        return disassemble_reg_mem_instruction("xchg", data)
    if 0x91 <= opcode <= 0x97:
        return f"xchg ax,{REG_FIELD_MAP[1][opcode & 7]}", 1
        
    if opcode in [0x8c, 0x8e]:
        mod, sr_code, rm_code = (data[1] >> 6) & 3, (data[1] >> 3) & 3, data[1] & 7
        sreg = SEG_REG_MAP[sr_code]
        if mod == 0b11:
            rm_op, disp_bytes = REG_FIELD_MAP[1][rm_code], 0
        else:
            rm_op, disp_bytes = get_rm_string(mod, rm_code, data[2:])
        op1, op2 = (sreg, rm_op) if opcode == 0x8e else (rm_op, sreg)
        return f"mov {op1},{op2}", 2 + disp_bytes

    if (opcode >> 2) == 0b101000:
        w, d = opcode & 1, (opcode >> 1) & 1
        addr = int.from_bytes(data[1:3], 'little')
        acc = 'ax' if w else 'al'
        op1, op2 = (acc, f"[{addr:#x}]") if d == 0 else (f"[{addr:#x}]", acc)
        return f"mov {op1},{op2}", 3

    if opcode in [0x8d, 0xc4, 0xc5]:
        return disassemble_reg_mem_instruction({0x8d: "lea", 0xc4: "les", 0xc5: "lds"}[opcode], data)
        
    if 0xe4 <= opcode <= 0xef:
        is_out, w = (opcode & 2) != 0, opcode & 1
        acc = 'ax' if w else 'al'
        mnemonic = "out" if is_out else "in"
        if (opcode & 8) == 0:
            port = data[1]
            op1, op2 = (f"{port:#x}", acc) if is_out else (acc, f"{port:#x}")
            return f"{mnemonic} {op1},{op2}", 2
        else:
            op1, op2 = ("dx", acc) if is_out else (acc, "dx")
            return f"{mnemonic} {op1},{op2}", 1
            
    if opcode in [0xd4, 0xd5]:
        mnemonic = "aam" if opcode == 0xd4 else "aad"
        if len(data) > 1 and data[1] != 0x0a:
            return f"{mnemonic} {data[1]:#x}", 2
        return mnemonic, 2

    if opcode == 0xcd:
        return f"int {data[1]:#x}", 2
    if (opcode >> 2) == 0b110100:
        return disassemble_shift_rotate_instruction(data)

    if 0x40 <= opcode <= 0x5f:
        reg = REG_FIELD_MAP[1][opcode & 7]
        high_nibble = opcode >> 4
        if high_nibble == 4:
            mnemonic = "inc" if (opcode & 8) == 0 else "dec"
        else:
            mnemonic = "push" if (opcode & 8) == 0 else "pop"
        return f"{mnemonic} {reg}", 1
    
    if 0xb0 <= opcode <= 0xbf:
        w, reg_code = (opcode >> 3) & 1, opcode & 7
        length = 2 if w == 0 else 3
        if len(data) < length: return "INVALID", length
        imm = data[1] if w == 0 else int.from_bytes(data[1:3], 'little')
        return f"mov {REG_FIELD_MAP[w][reg_code]},{imm:#x}", length

    if mnemonic := JUMP_MNEMONICS.get(opcode):
        return disassemble_jump_instruction(mnemonic, data, origin)
    
    if opcode in [0xe8, 0xe9, 0xeb]:
        is_call, is_short = opcode == 0xe8, opcode == 0xeb
        disp_size = 1 if is_short else 2
        length = 1 + disp_size
        disp = int.from_bytes(data[1:length], 'little', signed=True)
        mnemonic = "call" if is_call else "jmp"
        prefix = "short " if is_short else ""
        return f"{mnemonic} {prefix}{origin + length + disp:#x}", length
    
    if opcode == 0x9a:
        return f"call far {int.from_bytes(data[3:5], 'little'):#06x}:{int.from_bytes(data[1:3], 'little'):#06x}", 5
    if opcode == 0xea:
        return f"jmp far {int.from_bytes(data[3:5], 'little'):#06x}:{int.from_bytes(data[1:3], 'little'):#06x}", 5
    if opcode in [0xc2, 0xca]:
        return f"{'ret' if opcode == 0xc2 else 'retf'} {int.from_bytes(data[1:3], 'little'):#x}", 3
    if opcode in GROUP_OPCODE_MAP:
        return disassemble_group_instruction(opcode, data)

    op_type_map: Dict[str, Dict[int, str]] = {
        "rm":{0b000000:"add", 0b000100:"adc", 0b000110:"sbb", 0b000010:"or", 0b001000:"and", 0b001010:"sub", 0b001100:"xor", 0b001110:"cmp", 0b100001:"test", 0b100010:"mov"},
        "acc":{0b0000010:"add", 0b0001010:"adc", 0b0001110:"sbb", 0b0000110:"or", 0b0010010:"and", 0b0010110:"sub", 0b0011010:"xor", 0b0011110:"cmp", 0b1010100:"test"}
    }
    
    if mn_rm := op_type_map["rm"].get(opcode >> 2):
        return disassemble_reg_mem_instruction(mn_rm, data)
    if mn_acc := op_type_map["acc"].get(opcode >> 1):
        return disassemble_immediate_to_acc_instruction(mn_acc, data)

    return f"db {opcode:#04x}", 1

def disassemble(data: bytes, origin: int = 0) -> Tuple[str, int]:
    if not data: return "No data", 0
    
    original_data = data
    prefixes: List[str] = []
    segment_prefix: Optional[str] = None
    prefix_op_map: Dict[int, str] = {0x26:"es", 0x2e:"cs", 0x36:"ss", 0x3e:"ds", 0xf0:"lock", 0xf2:"repne", 0xf3:"rep"}

    while data and data[0] in prefix_op_map:
        prefix_str = prefix_op_map[data[0]]
        if data[0] in [0x26, 0x2e, 0x36, 0x3e]:
            segment_prefix = prefix_str
        else:
            prefixes.append(prefix_str)
        data = data[1:]

    if not data: return f"db {original_data[0]:#04x}", 1

    if "rep" in prefixes and data[0] in [0xa6, 0xa7, 0xae, 0xaf]:
        prefixes[prefixes.index("rep")] = "repe"

    prefix_len = len(original_data) - len(data)
    asm, length = _disassemble_instruction(data, origin + prefix_len)

    if segment_prefix and "[" in asm:
        asm = asm.replace("[", f"[{segment_prefix}:", 1)
        
    full_prefix = " ".join(prefixes)
    final_asm = (full_prefix + " " + asm) if full_prefix else asm
    final_asm = final_asm.replace(" short ", " ")

    return final_asm, length

def main() -> None:
    parser = argparse.ArgumentParser(description="A simple 8086 disassembler.")
    parser.add_argument("filename", help="The binary file to disassemble.")
    parser.add_argument("-o", "--origin", type=lambda x: int(x, 0), default=0,
                        help="The origin address (in hex or decimal) for disassembly. Default is 0.")
    args = parser.parse_args()

    try:
        with open(args.filename, "rb") as f:
            binary_data = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{args.filename}'", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    offset = 0
    while offset < len(binary_data):
        current_data = binary_data[offset:]
        current_address = args.origin + offset
        
        asm, length = disassemble(current_data, current_address)
        
        if length == 0:
            print(f"Error: Disassembler returned zero length at offset {offset:#x}")
            break

        hex_dump = binary_data[offset:offset+length].hex().upper()
        print(f"{current_address:08X}  {hex_dump:<17} {asm}")
        offset += length

if __name__ == "__main__":
    main()