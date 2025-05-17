// longest_consecutive_sequence.c
// C implementation of Longest Consecutive Sequence using hash set
// Includes test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_N 200
#define HASH_SIZE 1009

typedef struct Entry {
    int key;
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

void hash_add(int key) {
    unsigned int h = hash(key);
    Entry* e = hash_table[h];
    while (e) {
        if (e->key == key) return;
        e = e->next;
    }
    e = (Entry*)malloc(sizeof(Entry));
    e->key = key;
    e->next = hash_table[h];
    hash_table[h] = e;
}

int hash_contains(int key) {
    unsigned int h = hash(key);
    Entry* e = hash_table[h];
    while (e) {
        if (e->key == key) return 1;
        e = e->next;
    }
    return 0;
}

int longestConsecutive(int* nums, int n) {
    hash_clear();
    for (int i = 0; i < n; ++i) hash_add(nums[i]);
    int longest = 0;
    for (int i = 0; i < n; ++i) {
        int num = nums[i];
        if (!hash_contains(num-1)) {
            int length = 1;
            while (hash_contains(num+length)) ++length;
            if (length > longest) longest = length;
        }
    }
    return longest;
}

typedef struct {
    int nums[MAX_N];
    int n;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int* nums, int n, int expected) {
    memcpy(tc->nums, nums, n * sizeof(int));
    tc->n = n;
    tc->expected = expected;
}

void test_longestConsecutive() {
    TestCase tests[10];
    int idx = 0;
    int a1[] = {100,4,200,1,3,2};
    set_test_case(&tests[idx++], a1, 6, 4);
    int a2[] = {0,3,7,2,5,8,4,6,0,1};
    set_test_case(&tests[idx++], a2, 10, 9);
    int a3[] = {1,2,0,1};
    set_test_case(&tests[idx++], a3, 4, 3);
    int a4[] = {9,1,4,7,3,-1,0,5,8,-1,6};
    set_test_case(&tests[idx++], a4, 11, 7);
    int a5[] = {0};
    set_test_case(&tests[idx++], a5, 1, 1);
    int a6[] = {1,2,3,4,5};
    set_test_case(&tests[idx++], a6, 5, 5);
    int a7[] = {1,3,5,2,4};
    set_test_case(&tests[idx++], a7, 5, 5);
    int a8[] = {1,2,3,4,5,6,7,8,9,10};
    set_test_case(&tests[idx++], a8, 10, 10);
    int a9[] = {10,9,8,7,6,5,4,3,2,1};
    set_test_case(&tests[idx++], a9, 10, 10);
    int a10[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    set_test_case(&tests[idx++], a10, 15, 15);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = longestConsecutive(tests[i].nums, tests[i].n);
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
    for (int i = 0; i < MAX_N; ++i) arr[i] = i+1;
    clock_t start = clock();
    for (int i = 0; i < 1000; ++i) {
        longestConsecutive(arr, MAX_N);
    }
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Performance test: 1000 runs on n=%d took %.3f seconds.\n", MAX_N, elapsed);
}

int main() {
    test_longestConsecutive();
    measure_performance();
    return 0;
}
