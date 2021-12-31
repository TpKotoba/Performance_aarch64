import sys

def print_code(instructionA, instructionB, shapeD, shapeN):
    r = ["v8", "v9", "v10", "v11"]
    print(f'''#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape_Ta, shape_Tb
    {instructionA} \\xx0\\shape_Ta, \\xx1\\shape_Tb, \\xx2\\shape_Tb
    {instructionB} \\xx0\\shape_Ta, \\xx1\\shape_Tb, \\xx2\\shape_Tb
    .endm

target:
    push_all
loop:
    
    Repeat256  core, {r[0]}, {r[1]}, {r[0]}, {r[3]}, .{shapeD}, .{shapeN}
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    ''')

if __name__ == "__main__":
    try: 
        ins1   = sys.argv[1]
        ins2   = sys.argv[2]
        shapeD = sys.argv[3]
        shapeN = sys.argv[4]
    except:
        ins1 = "SADDL"
        ins2 = "SADDL"
        shapeD = "8H"
        shapeN = "8B"
    print_code(ins1, ins2, shapeD, shapeN)
