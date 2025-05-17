// four_sum_ii.c
// C implementation of 4Sum II using hash table
// Includes test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_N 10
#define HASH_SIZE 10007

typedef struct Entry {
    int key;
    int value;
    struct Entry* next;
} Entry;

Entry* hash_table[HASH_SIZE];

unsigned int hash(int key) {
    return ((unsigned int)key) % HASH_SIZE;
}

void hash_clear() {
    for (int i = 0; i < HASH_SIZE; ++i) {
        Entry* e = hash_table[i];
        while (e) {
            Entry* tmp = e;
            e = e->next;
            free(tmp);
        }
        hash_table[i] = NULL;
    }
}

void hash_add(int key, int value) {
    unsigned int h = hash(key);
    Entry* e = hash_table[h];
    while (e) {
        if (e->key == key) {
            e->value += value;
            return;
        }
        e = e->next;
    }
    e = (Entry*)malloc(sizeof(Entry));
    e->key = key;
    e->value = value;
    e->next = hash_table[h];
    hash_table[h] = e;
}

int hash_get(int key) {
    unsigned int h = hash(key);
    Entry* e = hash_table[h];
    while (e) {
        if (e->key == key) return e->value;
        e = e->next;
    }
    return 0;
}

int fourSumCount(int* A, int* B, int* C, int* D, int n) {
    hash_clear();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            hash_add(A[i] + B[j], 1);
        }
    }
    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            count += hash_get(-(C[i] + D[j]));
        }
    }
    return count;
}

typedef struct {
    int A[MAX_N], B[MAX_N], C[MAX_N], D[MAX_N];
    int n;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int* A, int* B, int* C, int* D, int n, int expected) {
    memcpy(tc->A, A, n * sizeof(int));
    memcpy(tc->B, B, n * sizeof(int));
    memcpy(tc->C, C, n * sizeof(int));
    memcpy(tc->D, D, n * sizeof(int));
    tc->n = n;
    tc->expected = expected;
}

void test_fourSumCount() {
    TestCase tests[20];
    int idx = 0;
    int a1[] = {1,2}, b1[] = {-2,-1}, c1[] = {-1,2}, d1[] = {0,2};
    set_test_case(&tests[idx++], a1, b1, c1, d1, 2, 2);
    int a2[] = {0}, b2[] = {0}, c2[] = {0}, d2[] = {0};
    set_test_case(&tests[idx++], a2, b2, c2, d2, 1, 1);
    int a3[] = {1,1}, b3[] = {-1,-1}, c3[] = {0,1}, d3[] = {0,-1};
    set_test_case(&tests[idx++], a3, b3, c3, d3, 2, 4);
    int a4[] = {1,2,3}, b4[] = {4,5,6}, c4[] = {7,8,9}, d4[] = {10,11,12};
    set_test_case(&tests[idx++], a4, b4, c4, d4, 3, 0);
    int a5[] = {0,1,2}, b5[] = {0,1,2}, c5[] = {0,1,2}, d5[] = {0,1,2};
    set_test_case(&tests[idx++], a5, b5, c5, d5, 3, 19);
    int a6[] = {1,-1}, b6[] = {-1,1}, c6[] = {1,-1}, d6[] = {-1,1};
    set_test_case(&tests[idx++], a6, b6, c6, d6, 2, 16);
    int a7[] = {1,2,3,4}, b7[] = {-1,-2,-3,-4}, c7[] = {0,0,0,0}, d7[] = {0,0,0,0};
    set_test_case(&tests[idx++], a7, b7, c7, d7, 4, 64);
    int a8[] = {1,2}, b8[] = {2,1}, c8[] = {-1,-2}, d8[] = {-2,-1};
    set_test_case(&tests[idx++], a8, b8, c8, d8, 2, 8);
    int a9[] = {1,2,3}, b9[] = {-3,-2,-1}, c9[] = {0,0,0}, d9[] = {0,0,0};
    set_test_case(&tests[idx++], a9, b9, c9, d9, 3, 27);
    int a10[] = {1,2,3,4,5}, b10[] = {-5,-4,-3,-2,-1}, c10[] = {0,0,0,0,0}, d10[] = {0,0,0,0,0};
    set_test_case(&tests[idx++], a10, b10, c10, d10, 5, 125);
    int a11[] = {1,2,3,4,5}, b11[] = {1,2,3,4,5}, c11[] = {-1,-2,-3,-4,-5}, d11[] = {-1,-2,-3,-4,-5};
    set_test_case(&tests[idx++], a11, b11, c11, d11, 5, 625);
    int a12[] = {1}, b12[] = {1}, c12[] = {1}, d12[] = {-3};
    set_test_case(&tests[idx++], a12, b12, c12, d12, 1, 1);
    int a13[] = {1,2}, b13[] = {2,3}, c13[] = {-2,-3}, d13[] = {-1,-2};
    set_test_case(&tests[idx++], a13, b13, c13, d13, 2, 8);
    int a14[] = {0,0,0,0}, b14[] = {0,0,0,0}, c14[] = {0,0,0,0}, d14[] = {0,0,0,0};
    set_test_case(&tests[idx++], a14, b14, c14, d14, 4, 256);
    int a15[] = {1,2,3,4}, b15[] = {1,2,3,4}, c15[] = {-1,-2,-3,-4}, d15[] = {-1,-2,-3,-4};
    set_test_case(&tests[idx++], a15, b15, c15, d15, 4, 256);
    int a16[] = {1,2,3}, b16[] = {1,2,3}, c16[] = {-1,-2,-3}, d16[] = {-1,-2,-3};
    set_test_case(&tests[idx++], a16, b16, c16, d16, 3, 81);
    int a17[] = {1,2}, b17[] = {1,2}, c17[] = {-1,-2}, d17[] = {-1,-2};
    set_test_case(&tests[idx++], a17, b17, c17, d17, 2, 16);
    int a18[] = {1}, b18[] = {1}, c18[] = {-1}, d18[] = {-1};
    set_test_case(&tests[idx++], a18, b18, c18, d18, 1, 1);
    int a19[] = {1,2,3,4,5,6,7,8,9,10}, b19[] = {-10,-9,-8,-7,-6,-5,-4,-3,-2,-1}, c19[] = {0,0,0,0,0,0,0,0,0,0}, d19[] = {0,0,0,0,0,0,0,0,0,0};
    set_test_case(&tests[idx++], a19, b19, c19, d19, 10, 10000);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = fourSumCount(tests[i].A, tests[i].B, tests[i].C, tests[i].D, tests[i].n);
        if (result == tests[i].expected) {
            printf("Test case %d passed.\n", i+1);
            passed++;
        } else {
            printf("Test case %d failed: got %d, expected %d\n", i+1, result, tests[i].expected);
        }
    }
    printf("Passed %d/%d test cases.\n", passed, idx);
}

void measure_performance() {
    int n = 10;
    int A[10], B[10], C[10], D[10];
    for (int i = 0; i < n; ++i) {
        A[i] = i+1;
        B[i] = -(i+1);
        C[i] = 0;
        D[i] = 0;
    }
    clock_t start = clock();
    for (int i = 0; i < 1000; ++i) {
        fourSumCount(A, B, C, D, n);
    }
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Performance test: 1000 runs on n=10 took %.3f seconds.\n", elapsed);
}

int main() {
    test_fourSumCount();
    measure_performance();
    return 0;
}
