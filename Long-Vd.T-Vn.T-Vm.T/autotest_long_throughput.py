import os, itertools, time

if __name__ == "__main__":

    INSTRUCTION = []
    with open("./Instructions.txt", mode="r") as FILEIN:
        for line in FILEIN:
            INSTRUCTION.append(line.split(" ")[0])
    SHTYPE  = [("2S", "4S", "2D"), ("4H", "8H", "4S"), ("8B", "16B", "8H")]

    for optype in itertools.product(INSTRUCTION, SHTYPE):
        # lower_part: 2D, 2S; 4S, 4H; 8H, 8B
        os.system(f"python3 generator_T.py {optype[0]} {optype[0]} {optype[1][2]} {optype[1][0]} > meta_T-{optype[0]}-{optype[1][2]}-{optype[1][0]}.S")
        os.system(f"make meta_T-{optype[0]}-{optype[1][2]}-{optype[1][0]}.bin")
        # Higher_part: 2D, 4S; 4S, 8H; 8H, 16B
        os.system(f"python3 generator_T.py {optype[0]}2 {optype[0]}2 {optype[1][2]} {optype[1][1]} > meta_T-{optype[0]}2-{optype[1][2]}-{optype[1][1]}.S")
        os.system(f"make meta_T-{optype[0]}2-{optype[1][2]}-{optype[1][1]}.bin")
    t = int(time.time())
    os.system(f'echo "" > RESULT{t}.txt')
    N = len(INSTRUCTION)*6
    for i, optype in enumerate(itertools.product(INSTRUCTION, SHTYPE)):
        execfile = f"./meta_T-{optype[0]}-{optype[1][2]}-{optype[1][0]}.bin"
        print(f"exec({2*i+1}/{N}): {execfile}")
        os.system(f"{execfile} >> RESULT{t}.txt")
        execfile = f"./meta_T-{optype[0]}2-{optype[1][2]}-{optype[1][1]}.bin"
        print(f"exec({2*i+2}/{N}): {execfile}")
        os.system(f"{execfile} >> RESULT{t}.txt")