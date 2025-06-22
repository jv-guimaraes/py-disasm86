# disasm86 - Intel 8086 Disassembler

A simple python command-line tool to disassemble 16-bit Intel 8086 binary code.

## Usage

You can run `disasm86.py` from your terminal, passing a binary file as an argument.

**Syntax:**

```bash
python disasm86.py [options] <filename>
```

**Example:**

```bash
python disasm86.py my_program.bin
python disasm86.py --origin 0x100 bootloader.bin
```

## Options

*   **`-o <address>`, `--origin <address>`**: Sets the starting memory address for the disassembly listing.
    *   The `address` can be specified in decimal (e.g., `256`) or hexadecimal (e.g., `0x100`).
    *   Defaults to `0`.