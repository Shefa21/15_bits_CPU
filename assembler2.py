r_type_functions = {
    "and": "000",
    "xor": "001",
    "nop": "000",
    "sub": "010",
}

i_type_opcodes = {
    "ori": "010",
    "addi": "011",
    "sw": "100",
    "beq": "001",
    "lw": "110",
}

j_type_opcodes = {
    "jmp": "101",
}

# Function to convert decimal to binary of fixed width
def decimal_to_binary(value, bits):
    if value < 0:
        value = (1 << bits) + value
    return format(value, f"0{bits}b")

# Function to convert binary to hexadecimal
def binary_to_hex(binary):
    return hex(int(binary, 2))[2:].zfill(4)  # 15 bits -> 4 hex digits

# Main assembler function
def assemble(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        outfile.write("v2.0 raw\n")
        
        for line in infile:
            line = line.strip().lower()
            if not line:
                continue
            
            parts = line.split()
            instr_type = parts[0]

            # NOP instruction processing (fixed bits)
            if instr_type == "nop":
                opcode = "000"
                rs = "000"
                rt = "000"
                rd = "000"
                func = "000"
                binary_instruction = f"{opcode}{rs}{rt}{rd}{func}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            # Process R-type instructions
            elif instr_type in r_type_functions:
                opcode = "000"
                func = r_type_functions[instr_type]
                rd = decimal_to_binary(int(parts[1][1:]), 3)
                rs = decimal_to_binary(int(parts[2][1:]), 3)
                rt = decimal_to_binary(int(parts[3][1:]), 3)
                binary_instruction = f"{opcode}{rs}{rt}{rd}{func}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            # Process I-type instructions
            elif instr_type in i_type_opcodes:
                opcode = i_type_opcodes[instr_type]
                rt_or_rd = decimal_to_binary(int(parts[1][1:]), 3)
                rs = decimal_to_binary(int(parts[2][1:]), 3)
                immediate = decimal_to_binary(int(parts[3]), 6)
                binary_instruction = f"{opcode}{rs}{rt_or_rd}{immediate}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            # Process J-type instructions
            elif instr_type in j_type_opcodes:
                opcode = j_type_opcodes[instr_type]
                address = decimal_to_binary(int(parts[1]), 12)
                binary_instruction = f"{opcode}{address}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            else:
                raise ValueError(f"Unknown instruction: {instr_type}")

# Run assembler
input_file = "inputs.txt"
output_file = "outputs"
assemble(input_file, output_file)
