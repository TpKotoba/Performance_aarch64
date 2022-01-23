import os, itertools, time, sys

if __name__ == "__main__":

    try:
        comment = "-"+str(sys.argv[1])
    except:
        comment = ""

    INSTRUCTION = ["BIF", "BIT", "BSL", "PMUL"]
    SHAPE = ["16B", "8B"]
    STYLE = ["dep", "par", "nop"]

    for instype in itertools.product(INSTRUCTION, SHAPE, STYLE):
        os.system(f"python3 generator_{instype[2]}.py {instype[0]} {instype[1]} > meta_{instype[2]}-{instype[0]}-{instype[1]}.S")
        os.system(f"make meta_{instype[2]}-{instype[0]}-{instype[1]}.bin")
    logfile = f"RESULT{comment}-{int(time.time())}.txt"
    os.system(f'echo "" > {logfile}')
    N = len(INSTRUCTION)*len(SHAPE)*len(STYLE)
    for i, instype in enumerate(itertools.product(INSTRUCTION, SHAPE, STYLE)):
        execfile = f"./meta_{instype[2]}-{instype[0]}-{instype[1]}.bin"
        print(f"exec({i+1}/{N}): {execfile}")
        os.system(f"{execfile} >> {logfile}")