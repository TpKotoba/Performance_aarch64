#include "macros.i"

    .align  2
    .global target
#ifndef __clang__
    .type   target, %function
#endif

    .macro core
    DUP v8.2D, x0
    ADD x0, x0, x0
    .endm

target:
    push_all
loop:
    
    Repeat256  core
    
    subs    x0, x0, #1
    bge     loop
end:
    pop_all
    br  lr
    
