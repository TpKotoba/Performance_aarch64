import os, itertools, time

if __name__ == "__main__":

    INSTRUCTION = []
    with open("./Instructions.txt", mode="r") as FILEIN:
        for line in FILEIN:
            INSTRUCTION.append(line.split(" ")[0])
    SHTYPE  = [("2S", "4S", "2D"), ("4H", "8H", "4S"), ("8B", "16B", "8H")]
    OPTYPE = itertools.product(INSTRUCTION, SHTYPE)
    DRTYPE = ["I", "N", "M", "D"]

    for instype in itertools.product(OPTYPE, DRTYPE):
        optype = instype[0] #(instruction, shape_tuple)
        # lower_part: 2S, 2D; 4H, 4S; 8B, 8H
        os.system(f"python3 generator_{instype[1]}.py {optype[0]} {optype[0]} {optype[1][2]} {optype[1][0]} > meta_{instype[1]}-{optype[0]}-{optype[0]}-{optype[1][2]}-{optype[1][0]}.S")
        os.system(f"make meta_{instype[1]}-{optype[0]}-{optype[0]}-{optype[1][2]}-{optype[1][0]}.bin")
        # Higher_part: 4S, 2D; 8H, 4S; 16B, 8H
        os.system(f"python3 generator_{instype[1]}.py {optype[0]}2 {optype[0]}2 {optype[1][2]} {optype[1][1]} > meta_{instype[1]}-{optype[0]}2-{optype[0]}2-{optype[1][2]}-{optype[1][1]}.S")
        os.system(f"make meta_{instype[1]}-{optype[0]}2-{optype[0]}2-{optype[1][2]}-{optype[1][1]}.bin")
    t = int(time.time())
    os.system(f'echo "" > RESULT{t}.txt')
    N = len(SHTYPE)*len(DRTYPE)*len(INSTRUCTION)*2
    for i, instype in enumerate(itertools.product(OPTYPE, DRTYPE)):
        optype = instype[0]
        execfile = f"./meta_{instype[1]}-{optype[0]}-{optype[0]}-{optype[1][2]}-{optype[1][0]}.bin"
        print(f"exec({2*i+1}/{N}): {execfile}")
        os.system(f"{execfile} >> RESULT{t}.txt")
        execfile = f"./meta_{instype[1]}-{optype[0]}2-{optype[0]}2-{optype[1][2]}-{optype[1][1]}.bin"
        print(f"exec({2*i+2}/{N}): {execfile}")
        os.system(f"{execfile} >> RESULT{t}.txt")