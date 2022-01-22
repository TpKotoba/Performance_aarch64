import sys

def print_code(instruction, shape):
    if(shape == "X"):
        r = ["x19", "x20", "x21", "x22"]
        shape = ""
    elif(shape == "W"):
        r = ["w19", "w20", "w21", "w22"]
        shape = ""
    else:
        r = ["v8", "v9", "v10", "v11"]
        shape = "."+shape
    print(f'''#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    {instruction} \\xx0\\shape, \\xx1\\shape
    nop
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
        instr = sys.argv[1]
        shape = sys.argv[2]
    except:
        instr = "ABS"
        shape = "8B"
    print_code(instr, shape)
