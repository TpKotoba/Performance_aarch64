#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core xx0, xx1, xx2, xx3, shape
    ADD \xx0\shape, \xx1\shape, \xx2\shape
    ADD \xx0\shape, \xx1\shape, \xx2\shape
    .endm

target:
    push_all
loop:
    
    Repeat256  core, x19, x20, x21, x22, 
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    
