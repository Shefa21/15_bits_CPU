## 🎞 CPU Simulation

![CPU Simulation](media/cpu_simulation.gif)

🧠 15-bit CPU Design
Custom CPU design project for CSE332: Computer Architecture & Organization under TNF Ma'am
Designed using a customized 15-bit Instruction Set Architecture (ISA)

📌 Overview
This project is a simplified 15-bit CPU built from scratch, focusing on core architecture and instruction execution. It simulates basic CPU operations, including arithmetic, logic, data transfer, and control flow — all controlled by a custom hardwired control unit.

🧱 Features
🔢 15-bit Instruction Format

🧮 Custom RISC-style ISA

🗃 8 General-Purpose Registers (R0–R7)

🧠 Single-cycle CPU (fetch → decode → execute)

📤 Hardwired Control Unit

🧮 ALU with arithmetic and logic ops

💾 Separate instruction and data memory

⚙️ Architecture

[Instruction Memory] → [Control Unit] ↔ [Datapath]
                               ↓
    [Registers] ←→ [ALU] ←→ [Data Memory]
Instruction Size: 15 bits

Registers: 8 (3-bit register addresses)

Opcode: 3 bits

Function Code / Immediate / Addressing Fields: Varies based on instruction type

🧾 Custom Instruction Set

Opcode	Mnemonic	Type	Description
000	ADD	R	R[dest] = R[src1] + R[src2]
001	SUB	R	R[dest] = R[src1] - R[src2]
010	AND	R	Logical AND
011	OR	R	Logical OR
100	LOAD	I	Load from memory to reg
101	STORE	I	Store reg to memory
110	JMP	J	Jump to address
111	HALT	-	Stop execution
You can expand this table with JZ, JNZ, MOV, NOT, INC, DEC, etc. based on your implementation.

🔄 Instruction Format Examples
R-Type (Register to Register)

| Opcode (3) | Dest (3) | Src1 (3) | Src2 (3) | Unused (3) |
I-Type (Immediate / Memory)


| Opcode (3) | Dest (3) | Address/Immediate (9)        |
J-Type (Jump)

| Opcode (3) | Jump Address (12)                      |
🧪 Sample Programs
Example: Adding two numbers and storing the result


LOAD R1, 010000000  ; Load value from memory to R1  
LOAD R2, 010000001  ; Load another value to R2  
ADD  R3, R1, R2     ; R3 = R1 + R2  
STORE R3, 010000010 ; Store result back to memory  
HALT
🧰 Tools Used
✅ Logisim / Digital Logic Simulator

✅ Hand-designed control logic (no microcode)

✅ Custom assembly for writing test programs

📚 Learning Highlights
✅ Designed and implemented a complete CPU datapath

✅ Built a hardwired control unit

✅ Customized and tested our own instruction set

✅ Gained practical understanding of instruction cycles and hardware logic

