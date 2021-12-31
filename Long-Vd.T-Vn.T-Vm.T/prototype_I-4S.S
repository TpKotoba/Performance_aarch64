#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape_Ta, shape_Tb
    SADDL2 \xx2\shape_Ta, \xx0\shape_Tb, \xx1\shape_Tb
    SADDL2 \xx2\shape_Ta, \xx0\shape_Tb, \xx1\shape_Tb
    .endm

target:
    push_all
loop:
    
    Repeat256  core, v8, v9, v10, v11, .2D, .4S
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    
