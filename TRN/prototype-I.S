#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    trn1 \xx2\shape, \xx0\shape, \xx1\shape
    trn2 \xx2\shape, \xx0\shape, \xx1\shape
    .endm

target:
    push_all
loop:
    
    Repeat256  core, v19, v20, v21, v22, .4S
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    
