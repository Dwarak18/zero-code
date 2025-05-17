// top_k_frequent_elements.c
// C implementation of Top K Frequent Elements using hash map and min-heap
// Includes test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_N 32
#define HASH_SIZE 103
#define MAX_K 10

// Hash map for frequency counting
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

Entry* hash_find(int key) {
    unsigned int h = hash(key);
    Entry* e = hash_table[h];
    while (e) {
        if (e->key == key) return e;
        e = e->next;
    }
    return NULL;
}

// Min-heap for top K
typedef struct {
    int key;
    int freq;
} HeapNode;

void heapify_down(HeapNode* heap, int n, int i) {
    int smallest = i;
    int l = 2*i+1, r = 2*i+2;
    if (l < n && heap[l].freq < heap[smallest].freq) smallest = l;
    if (r < n && heap[r].freq < heap[smallest].freq) smallest = r;
    if (smallest != i) {
        HeapNode t = heap[i]; heap[i] = heap[smallest]; heap[smallest] = t;
        heapify_down(heap, n, smallest);
    }
}

void heapify_up(HeapNode* heap, int i) {
    while (i > 0) {
        int p = (i-1)/2;
        if (heap[i].freq < heap[p].freq) {
            HeapNode t = heap[i]; heap[i] = heap[p]; heap[p] = t;
            i = p;
        } else break;
    }
}

int topKFrequent(int* nums, int n, int k, int* result) {
    hash_clear();
    for (int i = 0; i < n; ++i) hash_add(nums[i], 1);
    HeapNode heap[MAX_K];
    int heap_size = 0;
    // Insert all unique numbers into heap
    for (int i = 0; i < HASH_SIZE; ++i) {
        Entry* e = hash_table[i];
        while (e) {
            if (heap_size < k) {
                heap[heap_size].key = e->key;
                heap[heap_size].freq = e->value;
                heapify_up(heap, heap_size);
                ++heap_size;
            } else if (e->value > heap[0].freq) {
                heap[0].key = e->key;
                heap[0].freq = e->value;
                heapify_down(heap, k, 0);
            }
            e = e->next;
        }
    }
    // Output top k elements
    for (int i = 0; i < heap_size; ++i) result[i] = heap[i].key;
    return heap_size;
}

typedef struct {
    int nums[MAX_N];
    int n;
    int k;
    int expected[MAX_K];
    int expected_size;
} TestCase;

void set_test_case(TestCase* tc, int* nums, int n, int k, int* expected, int expected_size) {
    memcpy(tc->nums, nums, n * sizeof(int));
    tc->n = n;
    tc->k = k;
    memcpy(tc->expected, expected, expected_size * sizeof(int));
    tc->expected_size = expected_size;
}

// Helper: check if two arrays are equal as sets
int set_equal(int* a, int n, int* b, int m) {
    if (n != m) return 0;
    int used[MAX_K] = {0};
    for (int i = 0; i < n; ++i) {
        int found = 0;
        for (int j = 0; j < m; ++j) if (!used[j] && a[i] == b[j]) { used[j] = 1; found = 1; break; }
        if (!found) return 0;
    }
    return 1;
}

void test_topKFrequent() {
    TestCase tests[10];
    int idx = 0;
    int a1[] = {1,1,1,2,2,3}, e1[] = {1,2};
    set_test_case(&tests[idx++], a1, 6, 2, e1, 2);
    int a2[] = {1}, e2[] = {1};
    set_test_case(&tests[idx++], a2, 1, 1, e2, 1);
    int a3[] = {1,2}, e3[] = {1,2};
    set_test_case(&tests[idx++], a3, 2, 2, e3, 2);
    int a4[] = {1,2,2,3,3,3}, e4[] = {3};
    set_test_case(&tests[idx++], a4, 6, 1, e4, 1);
    int a5[] = {1,2,2,3,3,3}, e5[] = {3,2};
    set_test_case(&tests[idx++], a5, 6, 2, e5, 2);
    int a6[] = {1,2,2,3,3,3}, e6[] = {3,2,1};
    set_test_case(&tests[idx++], a6, 6, 3, e6, 3);
    int a7[] = {4,1,-1,2,-1,2,3}, e7[] = {-1,2};
    set_test_case(&tests[idx++], a7, 7, 2, e7, 2);
    int a8[] = {1,1,2,2,3,3,4,4,5,5}, e8[] = {1,2,3};
    set_test_case(&tests[idx++], a8, 10, 3, e8, 3);
    int a9[] = {1,1,1,2,2,3,3,3,4,4,4,4}, e9[] = {4};
    set_test_case(&tests[idx++], a9, 12, 1, e9, 1);
    int passed = 0;
    int result[MAX_K];
    for (int i = 0; i < idx; ++i) {
        int n = topKFrequent(tests[i].nums, tests[i].n, tests[i].k, result);
        if (set_equal(result, n, tests[i].expected, tests[i].expected_size)) {
            printf("Test case %d passed.\n", i+1);
            passed++;
        } else {
            printf("Test case %d failed: got [");
            for (int j = 0; j < n; ++j) printf("%d%s", result[j], j+1==n?"":", ");
            printf("] expected [");
            for (int j = 0; j < tests[i].expected_size; ++j) printf("%d%s", tests[i].expected[j], j+1==tests[i].expected_size?"":", ");
            printf("]\n");
        }
    }
    printf("Passed %d/%d test cases.\n", passed, idx);
}

void measure_performance() {
    int arr[MAX_N];
    for (int i = 0; i < MAX_N; ++i) arr[i] = (i % 5) + 1;
    int result[MAX_K];
    clock_t start = clock();
    for (int i = 0; i < 1000; ++i) {
        topKFrequent(arr, MAX_N, 3, result);
    }
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Performance test: 1000 runs on n=%d took %.3f seconds.\n", MAX_N, elapsed);
}

int main() {
    test_topKFrequent();
    measure_performance();
    return 0;
}
