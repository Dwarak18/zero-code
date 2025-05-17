// partition_labels.c
// Greedy solution for partitioning labels
// Includes test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LEN 500
#define MAX_PARTS 100

typedef struct {
    char s[MAX_LEN+1];
    int expected[MAX_PARTS];
    int expected_size;
} TestCase;

// Returns the number of partitions, fills result[] with partition sizes
int partitionLabels(const char* s, int* result) {
    int last[256];
    int len = strlen(s);
    for (int i = 0; i < 256; ++i) last[i] = -1;
    for (int i = 0; i < len; ++i) last[(unsigned char)s[i]] = i;
    int j = 0, anchor = 0, res_idx = 0;
    for (int i = 0; i < len; ++i) {
        if (last[(unsigned char)s[i]] > j) j = last[(unsigned char)s[i]];
        if (i == j) {
            result[res_idx++] = i - anchor + 1;
            anchor = i + 1;
        }
    }
    return res_idx;
}

void test_partitionLabels() {
    TestCase tests[] = {
        {"ababcbacadefegdehijhklij", {9,7,8}, 3},
        {"eccbbbbdec", {10}, 1},
        {"abc", {1,1,1}, 3},
        {"aabbcc", {2,2,2}, 3},
        {"abac", {3,1}, 2},
        {"aaaaa", {5}, 1},
        {"ab", {1,1}, 2},
        {"a", {1}, 1},
        {"abacbc", {6}, 1},
        {"abacbcd", {7}, 1},
        {"abacbcde", {8}, 1},
        {"abacbcdef", {9}, 1},
        {"abacbcdefg", {10}, 1},
        {"abacbcdefgh", {11}, 1},
        {"abacbcdefghi", {12}, 1},
        {"abacbcdefghij", {13}, 1},
        {"abacbcdefghijk", {14}, 1},
        {"abacbcdefghijkl", {15}, 1},
        {"abacbcdefghijklm", {16}, 1},
        {"abacbcdefghijklmn", {17}, 1},
    };
    int num_tests = sizeof(tests)/sizeof(tests[0]);
    int passed = 0;
    int result[MAX_PARTS];
    for (int i = 0; i < num_tests; ++i) {
        int n = partitionLabels(tests[i].s, result);
        int ok = (n == tests[i].expected_size);
        for (int j = 0; ok && j < n; ++j) {
            if (result[j] != tests[i].expected[j]) ok = 0;
        }
        if (ok) {
            printf("Test case %d passed.\n", i+1);
            ++passed;
        } else {
            printf("Test case %d failed: input=\"%s\", expected=[", i+1, tests[i].s);
            for (int j = 0; j < tests[i].expected_size; ++j) printf("%d%s", tests[i].expected[j], j+1==tests[i].expected_size?"":", ");
            printf("], got=[");
            for (int j = 0; j < n; ++j) printf("%d%s", result[j], j+1==n?"":", ");
            printf("]\n");
        }
    }
    printf("Passed %d/%d test cases.\n", passed, num_tests);
}

void measure_performance() {
    char s[MAX_LEN+1];
    for (int i = 0; i < MAX_LEN; ++i) s[i] = 'a' + (i % 26);
    s[MAX_LEN] = '\0';
    int result[MAX_PARTS];
    clock_t start = clock();
    for (int i = 0; i < 10000; ++i) {
        partitionLabels(s, result);
    }
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Performance test: 10000 runs on string of length %d took %.3f seconds.\n", MAX_LEN, elapsed);
}

int main() {
    test_partitionLabels();
    measure_performance();
    return 0;
}
