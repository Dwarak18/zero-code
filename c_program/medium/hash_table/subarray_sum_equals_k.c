// subarray_sum_equals_k.c
// C implementation of Subarray Sum Equals K using hash map
// Includes test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_N 32
#define HASH_SIZE 1009

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

int subarraySum(int* nums, int n, int k) {
    hash_clear();
    hash_add(0, 1);
    int res = 0, curr = 0;
    for (int i = 0; i < n; ++i) {
        curr += nums[i];
        res += hash_get(curr - k);
        hash_add(curr, 1);
    }
    return res;
}

typedef struct {
    int nums[MAX_N];
    int n;
    int k;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int* nums, int n, int k, int expected) {
    memcpy(tc->nums, nums, n * sizeof(int));
    tc->n = n;
    tc->k = k;
    tc->expected = expected;
}

void test_subarraySum() {
    TestCase tests[20];
    int idx = 0;
    int a1[] = {1,1,1};
    set_test_case(&tests[idx++], a1, 3, 2, 2);
    int a2[] = {1,2,3};
    set_test_case(&tests[idx++], a2, 3, 3, 2);
    int a3[] = {1};
    set_test_case(&tests[idx++], a3, 1, 0, 0);
    int a4[] = {1,-1,0};
    set_test_case(&tests[idx++], a4, 3, 0, 3);
    int a5[] = {3,4,7,2,-3,1,4,2};
    set_test_case(&tests[idx++], a5, 8, 7, 4);
    int a6[] = {1,2,1,2,1};
    set_test_case(&tests[idx++], a6, 5, 3, 4);
    int a7[] = {1,-1,1,-1,1};
    set_test_case(&tests[idx++], a7, 5, 0, 4);
    int a8[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a8, 5, 9, 2);
    int a9[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a9, 5, 15, 1);
    int a10[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a10, 5, 1, 1);
    int a11[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a11, 5, 5, 2);
    int a12[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a12, 5, 10, 1);
    int a13[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a13, 5, 14, 0);
    int a14[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a14, 5, 0, 0);
    int a15[] = {0,0,0,0,0};
    set_test_case(&tests[idx++], a15, 5, 0, 15);
    int a16[] = {1,-1,1,-1,1,-1,1,-1,1};
    set_test_case(&tests[idx++], a16, 9, 0, 16);
    int a17[] = {1,2,3,4,5,6,7,8,9,10};
    set_test_case(&tests[idx++], a17, 10, 10, 1);
    int a18[] = {1,2,3,4,5,6,7,8,9,10};
    set_test_case(&tests[idx++], a18, 10, 55, 1);
    int a19[] = {1,2,3,4,5,6,7,8,9,10};
    set_test_case(&tests[idx++], a19, 10, 100, 0);
    int a20[] = {1,2,3,4,5,6,7,8,9,10};
    set_test_case(&tests[idx++], a20, 10, 0, 0);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = subarraySum(tests[i].nums, tests[i].n, tests[i].k);
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
    int arr[MAX_N];
    for (int i = 0; i < MAX_N; ++i) arr[i] = (i % 3) - 1;
    int k = 0;
    clock_t start = clock();
    for (int i = 0; i < 1000; ++i) {
        subarraySum(arr, MAX_N, k);
    }
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Performance test: 1000 runs on n=%d took %.3f seconds.\n", MAX_N, elapsed);
}

int main() {
    test_subarraySum();
    measure_performance();
    return 0;
}
