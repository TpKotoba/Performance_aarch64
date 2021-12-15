CC = gcc
CFLAGS = -O3 -march=native -mtune=native -mcpu=native -I$(COMMON)
COMMON = ../common/

AARCH := $(shell uname -m)
ifeq ($(AARCH),armv7l)
	CFLAGS += -mfpu=neon -marm
endif

.PHONY: clean
clean:
	-rm -f *.bin *.o *.out
	-rm -f meta_* RESULT_*