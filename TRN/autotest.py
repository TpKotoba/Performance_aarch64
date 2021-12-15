import os, itertools, time

if __name__ == "__main__":

    TRNS = ["trn1", "trn2"]
    INTYPE = itertools.product(TRNS, TRNS)
    SHTYPE = ["2D", "4S", "8H", "16B"]
    OPTYPE = [(i[0][0], i[0][1], i[1]) for i in itertools.product(INTYPE, SHTYPE)]
    DRTYPE = ["I", "N", "M", "D"]

    for instype in itertools.product(OPTYPE, DRTYPE):
        optype = instype[0]
        os.system(f"python3 generator{instype[1]}.py {optype[0]} {optype[1]} {optype[2]} > meta_{instype[1]}-{optype[0]}-{optype[1]}-{optype[2]}.S")
        os.system(f"make meta_{instype[1]}-{optype[0]}-{optype[1]}-{optype[2]}.bin")
    t = int(time.time())
    os.system(f'echo "" > RESULT{t}.txt')
    for instype in itertools.product(OPTYPE, DRTYPE):
        optype = instype[0]
        os.system(f"./meta_{instype[1]}-{optype[0]}-{optype[1]}-{optype[2]}.bin >> RESULT{t}.txt")
