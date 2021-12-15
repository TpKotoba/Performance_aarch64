#ifndef MACROS_I
#define MACROS_I

.macro push_all

    sub sp, sp, #(16*9)
    stp x19, x20, [sp, #16*0]
    stp x21, x22, [sp, #16*1]
    stp x23, x24, [sp, #16*2]
    stp x25, x26, [sp, #16*3]
    stp x27, x28, [sp, #16*4]
    stp  d8,  d9, [sp, #16*5]
    stp d10, d11, [sp, #16*6]
    stp d12, d13, [sp, #16*7]
    stp d14, d15, [sp, #16*8]

.endm

.macro pop_all

    ldp x19, x20, [sp, #16*0]
    ldp x21, x22, [sp, #16*1]
    ldp x23, x24, [sp, #16*2]
    ldp x25, x26, [sp, #16*3]
    ldp x27, x28, [sp, #16*4]
    ldp  d8,  d9, [sp, #16*5]
    ldp d10, d11, [sp, #16*6]
    ldp d12, d13, [sp, #16*7]
    ldp d14, d15, [sp, #16*8]
    add sp, sp, #(16*9)

.endm

.macro Repeat4 macro, op0, op1, op2, op3, shape
    \macro  \op0, \op1, \op2, \op3, \shape
    \macro  \op0, \op1, \op2, \op3, \shape
    \macro  \op0, \op1, \op2, \op3, \shape
    \macro  \op0, \op1, \op2, \op3, \shape
.endm

.macro Repeat16 macro, op0, op1, op2, op3, shape
    Repeat4     \macro, \op0, \op1, \op2, \op3, \shape
    Repeat4     \macro, \op0, \op1, \op2, \op3, \shape
    Repeat4     \macro, \op0, \op1, \op2, \op3, \shape
    Repeat4     \macro, \op0, \op1, \op2, \op3, \shape
.endm

.macro Repeat64 macro, op0, op1, op2, op3, shape
    Repeat16    \macro, \op0, \op1, \op2, \op3, \shape
    Repeat16    \macro, \op0, \op1, \op2, \op3, \shape
    Repeat16    \macro, \op0, \op1, \op2, \op3, \shape
    Repeat16    \macro, \op0, \op1, \op2, \op3, \shape
.endm

.macro Repeat256 macro, op0, op1, op2, op3, shape
    Repeat64    \macro, \op0, \op1, \op2, \op3, \shape
    Repeat64    \macro, \op0, \op1, \op2, \op3, \shape
    Repeat64    \macro, \op0, \op1, \op2, \op3, \shape
    Repeat64    \macro, \op0, \op1, \op2, \op3, \shape
.endm

#endif