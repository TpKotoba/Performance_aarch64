import os, itertools, time

if __name__ == "__main__":

    # ignore ADD
    INSTRUCTION = ["SUB", "AND", "BIC", "ORN", "ORR", "EOR"]
    INTYPE = [(i, i) for i in INSTRUCTION]
    SHTYPE = ["scalar", "2D", "4S", "8H", "16B", "2S", "4H", "8B"]
    OPTYPE = [(i[0][0], i[0][1], i[1]) for i in itertools.product(INTYPE, SHTYPE)]
    DRTYPE = ["I", "N", "M", "D"]

    for instype in itertools.product(OPTYPE, DRTYPE):
        optype = instype[0]
        os.system(f"python3 generator_{instype[1]}.py {optype[0]} {optype[1]} {optype[2]} > meta_{instype[1]}-{optype[0]}-{optype[1]}-{optype[2]}.S")
        os.system(f"make meta_{instype[1]}-{optype[0]}-{optype[1]}-{optype[2]}.bin")
    t = int(time.time())
    os.system(f'echo "" > RESULT{t}.txt')
    N = len(SHTYPE)*len(DRTYPE)*len(INTYPE)
    for i, instype in enumerate(itertools.product(OPTYPE, DRTYPE)):
        optype = instype[0]
        execfile = f"./meta_{instype[1]}-{optype[0]}-{optype[1]}-{optype[2]}.bin"
        print(f"exec({i+1}/{N}): {execfile}")
        os.system(f"{execfile} >> RESULT{t}.txt")
