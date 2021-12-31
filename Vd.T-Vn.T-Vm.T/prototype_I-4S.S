#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    ADD \xx2\shape, \xx0\shape, \xx1\shape
    ADD \xx2\shape, \xx0\shape, \xx1\shape
    .endm

target:
    push_all
loop:
    
    Repeat256  core, v8, v9, v10, v11, .4S
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    
