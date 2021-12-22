import sys

def print_code(instructionA, instructionB, shape):
    if(shape == "scalar"):
        r = ["x19", "x20", "x21", "x22"]
        shape = ""
    elif(shape in ["2D", "4S", "8H", "16B"]):
        r = ["v8", "v9", "v10", "v11"]
        shape = "."+shape
    elif(shape in ["2S", "4H", "8B"]):
        r = ["d8", "d9", "d10", "d11"]
        shape = "."+shape
    print(f'''#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    {instructionA} \\xx0\\shape, \\xx1\\shape, \\xx2\\shape
    {instructionB} \\xx0\\shape, \\xx1\\shape, \\xx2\\shape
    .endm

target:
    push_all
loop:
    
    Repeat256  core, {r[0]}, {r[1]}, {r[2]}, {r[3]}, {shape}
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    ''')

if __name__ == "__main__":
    try: 
        ins1 = sys.argv[1]
    except:
        ins1 = "ADD"
    try:
        ins2 = sys.argv[2]
    except:
        ins2 = "ADD"
    try:
        shape = sys.argv[3]
    except:
        shape = "scalar"
    print_code(ins1, ins2, shape)
