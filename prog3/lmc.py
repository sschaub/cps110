# File: lmc.py
# Author: Stephen Schaub
# Modified by: 
#
# An implementation of a variation of the Little Man Computer
# https://en.wikipedia.org/wiki/Little_man_computer

# Global variables for LMC components
memory = [0] * 100
pc = 0
accum = 0
inbox = []
outbox = []
running = True  # Set to False when HLT is executed

# Instruction numbers
HLT = 0
ADD = 1
SUB = 2
STA = 3
LDA = 4
BRA = 5
BRZ = 6
INP = 7
OUT = 8


# ---------------- LMC Component Interfaces ------------------

def readMem(addr: int) -> int:
    """Returns value at address `addr` in memory, or 0 if `addr` is out of range"""
    if 0 <= addr < len(memory):
        return memory[addr]
    else:
        return 0

def writeMem(addr: int, val: int):
    """Writes `val` to memory cell at address `addr`"""
    if 0 <= addr < len(memory) and 0 <= val <= 999:
        memory[addr] = val

def readAccum() -> int:
    """Returns value of accumulator"""
    return accum

def writeAccum(val: int):
    """Writes `val` to accumulator, if 0 <= `val` <= 999"""
    global accum
    if 0 <= val <= 999:
        accum = val

def readPC() -> int:
    """Returns current program counter value"""
    return pc

def writePC(val: int):
    """Writes `val` to program counter, if 0 <= `val` <= 999"""
    global pc
    if 0 <= val < len(memory):
        pc = val

def readInbox() -> int:
    """TODO: Removes and returns first number from inbox. If inbox is empty, returns 0."""
    return 0

def writeOutbox(val: int):
    """Places `val` at end of outbox"""
    outbox.append(val)

# ------------ Fetch / Decode / Execute Functions ------------

def fetch() -> int:
    """Fetches and returns next instruction indicated by PC. Increments PC."""
    pcval = readPC()
    instr = readMem(pcval)
    writePC(pcval + 1)
    return instr

def decode(instr: int) -> (int, int):
    """Decodes instruction `instr`, returning its (opcode, operand)"""
    return (instr // 100, instr % 100)

def execute(opcode: int, operand: int):
    """Executes instruction corresponding to `opcode`, using `operand` if needed"""
    global running
    if opcode == OUT:
        writeOutbox(readAccum())
    elif opcode == LDA:
        writeAccum(readMem(operand))
    elif opcode == HLT:
        running = False

def step():
    """Performs one fetch-decode-execute step"""
    instr = fetch()
    (opcode, operand) = decode(instr)
    execute(opcode, operand)

def run():
    """Performs fetch-decode-execute steps until `running` is False"""
    while running:
        step()

# ----------------- Simulator setup ----------------

def reset():
    """Resets all computer components to their initial state"""
    global pc, memory, accum, inbox, outbox, running
    pc = 0
    memory = [0] * 100
    accum = 0
    inbox = []
    outbox = []
    running = True

def load(program: list, indata: list):
    """Resets computer, loads memory with `program`, and sets inbox to `indata`"""
    global inbox
    reset()
    for i in range(len(program)):
        writeMem(i, program[i])
    inbox = indata

# ---------------- Simulator "display" ----------------------

def dumpStr() -> str:
    line = ""
    for i in range(len(memory)):
        if i % 10 == 0:
            line += "\n"
        line += "{0:2}[{1:3}] ".format(i, memory[i])
    line += "\n"
    disassem = toAssembly(readMem(readPC()))
    line += (" " * 32) + "PC[{0:2}] Acc[{1:3}] {2}\n".format(readPC(), readAccum(), disassem)
    line += "In box: {}\n".format(inbox)
    line += "Out box: {}\n".format(outbox)
    return line


def dump():
    print(dumpStr())


def toAssembly(instr: int) -> str:
    """TODO: Returns assembly language translation of machine language instruction `instr`"""
    return "NOT DONE"


def disassemble(start: int, end: int):
    """Displays assembly language listing of memory contents `start` to `end`"""
    for addr in range(start, end + 1):
        print(str(addr).rjust(2) + ": " + toAssembly(readMem(addr)))

# ----------- Define shortcut names for interactive use

def sd():
    step()
    dump()

s = step
d = dump
r = run       

# ----------------- Unit Tests ------------------------

def test_mem():
    reset()
    assert memory == [0] * 100
    writeMem(1, 5)
    assert readMem(1) == 5

    reset()
    writeMem(-1, 5)
    assert memory == [0] * 100

    writeMem(1, 1000)
    assert memory == [0] * 100

def test_LDA():
    reset()
    writeMem(3, 50)
    execute(LDA, 3)
    assert readAccum() == 50

def test_OUT():
    reset()
    writeAccum(3)
    execute(OUT, 0)
    assert outbox == [3]


if __name__ == "__main__":
    reset()
