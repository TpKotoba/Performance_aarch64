PY = python3

all: auto*.py
	$(PY) $^

%.bin: %.S ../common/test.c
	$(CC) $(CFLAGS) $^ -o $@ -DNAME=$@ -DINSTR=256

include ../common/make.mk