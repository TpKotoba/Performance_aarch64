import os, itertools, time

if __name__ == "__main__":

    INSTRUCTION = []
    with open("./Instructions.txt", mode="r") as FILEIN:
        for line in FILEIN:
            INSTRUCTION.append(line.split(" ")[0])
    SHTYPE = ["2D", "4S", "8H", "16B", "2S", "4H", "8B"]

    for optype in itertools.product(INSTRUCTION, SHTYPE):
        os.system(f"python3 generator_T.py {optype[0]} {optype[0]} {optype[1]} > meta_T-{optype[0]}-{optype[0]}-{optype[1]}.S")
        os.system(f"make meta_T-{optype[0]}-{optype[1]}-{optype[2]}.bin")
    t = int(time.time())
    os.system(f'echo "" > RESULT{t}.txt')
    N = len(SHTYPE)*len(INSTRUCTION)
    for i, optype in enumerate(itertools.product(INSTRUCTION, SHTYPE)):
        execfile = f"./meta_T-{optype[0]}-{optype[0]}-{optype[1]}.bin"
        print(f"exec({i+1}/{N}): {execfile}")
        os.system(f"{execfile} >> RESULT{t}.txt")