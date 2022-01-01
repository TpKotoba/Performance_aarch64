import sys

def print_code(instructionA, instructionB, shape):
    r = ["v8", "v9", "v10", "v11"]
    print(f'''#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    {instructionA} \\xx0\\shape, \\xx1\\shape, \\xx2\\shape
    nop
    .endm

target:
    push_all
loop:
    
    Repeat256  core, {r[0]}, {r[1]}, {r[2]}, {r[3]}, .{shape}
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    ''')

if __name__ == "__main__":
    try: 
        ins1 = sys.argv[1]
        ins2 = sys.argv[2]
        shape = sys.argv[3]
    except:
        ins1 = "ADD"
        ins2 = "ADD"
        shape = "4S"
    print_code(ins1, ins2, shape)
