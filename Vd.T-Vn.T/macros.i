#ifndef MACROS_I
#define MACROS_I

.macro push_all

    sub sp, sp, #(16*13)
    stp x19, x20, [sp, #16*0]
    stp x21, x22, [sp, #16*1]
    stp x23, x24, [sp, #16*2]
    stp x25, x26, [sp, #16*3]
    stp x27, x28, [sp, #16*4]
    stp  q8,  q9, [sp, #16*5]
    stp q10, q11, [sp, #16*7]
    stp q12, q13, [sp, #16*9]
    stp q14, q15, [sp, #16*11]

.endm

.macro pop_all

    ldp x19, x20, [sp, #16*0]
    ldp x21, x22, [sp, #16*1]
    ldp x23, x24, [sp, #16*2]
    ldp x25, x26, [sp, #16*3]
    ldp x27, x28, [sp, #16*4]
    ldp  q8,  q9, [sp, #16*5]
    ldp q10, q11, [sp, #16*7]
    ldp q12, q13, [sp, #16*9]
    ldp q14, q15, [sp, #16*11]
    add sp, sp, #(16*13)

.endm

.macro Repeat4 macro, op0, op1, op2, op3, shape
    \macro \op0, \op1, \op2, \op3, \shape
    \macro \op0, \op1, \op2, \op3, \shape
    \macro \op0, \op1, \op2, \op3, \shape
    \macro \op0, \op1, \op2, \op3, \shape
.endm

.macro Repeat16 macro, op0, op1, op2, op3, shape
    Repeat4 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat4 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat4 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat4 \macro, \op0, \op1, \op2, \op3, \shape
.endm

.macro Repeat64 macro, op0, op1, op2, op3, shape
    Repeat16 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat16 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat16 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat16 \macro, \op0, \op1, \op2, \op3, \shape
.endm

.macro Repeat256 macro, op0, op1, op2, op3, shape
    Repeat64 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat64 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat64 \macro, \op0, \op1, \op2, \op3, \shape
    Repeat64 \macro, \op0, \op1, \op2, \op3, \shape
.endm

#endif
