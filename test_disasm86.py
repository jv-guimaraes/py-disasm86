import unittest
import re
from disasm86 import disassemble

def parse_completionist_file(filename="completionist_decode.txt"):
    test_cases = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if (line := line.strip()) and (match := re.match(r'^[0-9A-Fa-f]+\s+([0-9A-Fa-f]+)\s+(.*)', line)):
                    hex_code = match.group(1)
                    asm = " ".join(match.group(2).strip().lower().split())
                    test_cases.append((hex_code, asm))
    except FileNotFoundError:
        return None
    return test_cases

class TestDisassembler(unittest.TestCase):

    def test_all_instructions_from_file(self):
        all_tests = parse_completionist_file()
        if all_tests is None:
            self.fail("Test file 'completionist_decode.txt' not found. Cannot run tests.")
        
        failures = []
        for hex_code, expected_asm in all_tests:
            with self.subTest(hex=hex_code, expected=expected_asm):
                byte_code = bytes.fromhex(hex_code)
                my_asm, _ = disassemble(byte_code, origin=0)
                
                # Canonicalize mnemonics from file for loop/sal instructions
                if expected_asm.startswith("loopnz"): expected_asm = expected_asm.replace("loopnz", "loopne", 1)
                if expected_asm.startswith("loopz"): expected_asm = expected_asm.replace("loopz", "loope", 1)
                if expected_asm.startswith("sal"): expected_asm = expected_asm.replace("sal", "shl", 1)

                if my_asm != expected_asm:
                    failures.append((hex_code, expected_asm, my_asm))

        if failures:
            msg = f"\n--- {len(failures)} Disassembly Mismatches ---\n"
            for h, expected, mine in failures:
                msg += f"  - Hex: {h.ljust(18)} Expected: '{expected}', Got: '{mine}'\n"
            self.fail(msg)

if __name__ == '__main__':
    unittest.main()
