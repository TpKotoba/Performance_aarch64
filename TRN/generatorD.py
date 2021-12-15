import sys

def print_code(instructionA, instructionB, shape):
    print(f'''#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    {instructionA} \\xx2\\shape, \\xx0\\shape, \\xx1\\shape
    {instructionB} \\xx2\\shape, \\xx0\\shape, \\xx1\\shape
    .endm

target:
    push_all
loop:
    
    Repeat256  core, v21, v21, v21, v22, .{shape}
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    ''')

if __name__ == "__main__":
    try:
        shape = sys.argv[3]
    except:
        shape = "4S"
    try: 
        ins1 = sys.argv[1]
    except:
        ins1 = "trn1"
    try:
        ins2 = sys.argv[2]
    except:
        ins2 = "trn2"
    print_code(ins1, ins2, shape)
