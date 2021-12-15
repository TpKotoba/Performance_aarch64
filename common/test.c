#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "cpucycles.h"

// hack for using -DNAME=$@ in common/make.mk
#define STRINGIZE(x) #x
#define STRINGIZE_VALUE_OF(x) STRINGIZE(x)

// program name for the test
#ifndef NAME
#define NAME	"unnamed"
#endif

#ifndef ROUND
#define ROUND  	256
#endif

static int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

extern 	void target(uint32_t a);

#ifndef DIFF
#define DIFF 65536
#endif

#ifndef INSTR
#define INSTR 256
#endif
  
int main(void){

	int64_t count_0, count_1, counts[ROUND], count_sum = 0;

#ifndef __aarch64__
	hal_init_perfcounters(1,1);
#endif

	int round;

	for (round = 0; round < ROUND; round++) {

		// Performance benchmarking
		count_0 = hal_get_time();
		target((DIFF>>4)+DIFF);
		count_1 = hal_get_time();
		counts[round] = count_1-count_0;
		count_0 = hal_get_time();
		target(DIFF>>4);
		count_1 = hal_get_time();
		counts[round] -= count_1-count_0;

		count_sum += counts[round];
	}

	qsort(counts, ROUND, sizeof(int64_t), cmpfunc);

	//printf( "\n================================================================================\n" );
	//printf( "Program: %s;\n", STRINGIZE_VALUE_OF(NAME) );
	printf( "%s ", STRINGIZE_VALUE_OF(NAME) );
	//printf( "Cycle counts for %d rounds of sample: (%d instructions)\n", ROUND, INSTR*DIFF);
#ifdef __aarch64__
	//printf( "Average = %lld , Median = %lld\n", count_sum/ROUND,counts[ROUND>>1]);
	printf( "%lld %lld\n", count_sum/ROUND,counts[ROUND>>1]);
#else
	//printf( "%lld , %lld\n", count_sum/ROUND<<6,counts[ROUND>>1]<<6);
	printf( "%lld %lld\n", count_sum/ROUND<<6,counts[ROUND>>1]<<6);
#endif

	return 0;
}

