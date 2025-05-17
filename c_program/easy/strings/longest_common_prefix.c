// filepath: d:\coding_challenge\c_program\easy\strings\longest_common_prefix.c
#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

// Function to get current and peak memory usage in MB
void get_memory_usage(double *current_mb, double *peak_mb) {
    PROCESS_MEMORY_COUNTERS pmc;
    if (GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc))) {
        *current_mb = pmc.WorkingSetSize / (1024.0 * 1024.0);
        *peak_mb = pmc.PeakWorkingSetSize / (1024.0 * 1024.0);
    } else {
        *current_mb = 0;
        *peak_mb = 0;
    }
}

// Find the longest common prefix among an array of strings
void longestCommonPrefix(char strs[][100], int strsSize, char* out_prefix) {
    if (strsSize == 0) {
        out_prefix[0] = '\0';
        return;
    }
    strcpy(out_prefix, strs[0]);
    for (int i = 1; i < strsSize; ++i) {
        while (strncmp(strs[i], out_prefix, strlen(out_prefix)) != 0) {
            out_prefix[strlen(out_prefix) - 1] = '\0';
            if (strlen(out_prefix) == 0) {
                out_prefix[0] = '\0';
                return;
            }
        }
    }
}

typedef struct {
    char strs[10][100];
    int strsSize;
    char expected[100];
} TestCase;

// Helper to set up a test case with a 2D char array
void set_test_case(TestCase* tc, char arr[][100], int strsSize, const char* expected) {
    tc->strsSize = strsSize;
    for (int i = 0; i < strsSize; ++i) {
        strncpy(tc->strs[i], arr[i], 99);
        tc->strs[i][99] = '\0';
    }
    for (int i = strsSize; i < 10; ++i) {
        tc->strs[i][0] = '\0';
    }
    strncpy(tc->expected, expected, 99);
    tc->expected[99] = '\0';
}

void test_longest_common_prefix() {
    TestCase test_cases[21];
    int num_cases = 21;
    int idx = 0;
    char arr[10][100];
    // 1
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "flower"); strcpy(arr[1], "flow"); strcpy(arr[2], "flight");
    set_test_case(&test_cases[idx++], arr, 3, "fl");
    // 2
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "dog"); strcpy(arr[1], "racecar"); strcpy(arr[2], "car");
    set_test_case(&test_cases[idx++], arr, 3, "");
    // 3
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "interspace"); strcpy(arr[1], "internet"); strcpy(arr[2], "internal");
    set_test_case(&test_cases[idx++], arr, 3, "inter");
    // 4
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "a");
    set_test_case(&test_cases[idx++], arr, 1, "a");
    // 5
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], ""); strcpy(arr[1], "");
    set_test_case(&test_cases[idx++], arr, 2, "");
    // 6
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abc"); strcpy(arr[2], "abc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 7
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "ab"); strcpy(arr[2], "a");
    set_test_case(&test_cases[idx++], arr, 3, "a");
    // 8
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "def"); strcpy(arr[2], "ghi");
    set_test_case(&test_cases[idx++], arr, 3, "");
    // 9
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "prefix"); strcpy(arr[1], "preach"); strcpy(arr[2], "prevent");
    set_test_case(&test_cases[idx++], arr, 3, "pre");
    // 10
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "a"); strcpy(arr[1], "b"); strcpy(arr[2], "c");
    set_test_case(&test_cases[idx++], arr, 3, "");
    // 11
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abcde"); strcpy(arr[1], "abc"); strcpy(arr[2], "abcd");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 12
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcd"); strcpy(arr[2], "abce");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 13
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcde"); strcpy(arr[2], "abcdef");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 14
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abc"); strcpy(arr[2], "abcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 15
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abc"); strcpy(arr[2], "abcabcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 16
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcabc"); strcpy(arr[2], "abcabcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 17
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcabcabc"); strcpy(arr[2], "abcabcabcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 18
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcabcabcabc"); strcpy(arr[2], "abcabcabcabcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 19
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcabcabcabcabc"); strcpy(arr[2], "abcabcabcabcabcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");
    // 20
    memset(arr, 0, sizeof(arr));
    strcpy(arr[0], "abc"); strcpy(arr[1], "abcabcabcabcabcabc"); strcpy(arr[2], "abcabcabcabcabcabcabc");
    set_test_case(&test_cases[idx++], arr, 3, "abc");

    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        char result[100];
        longestCommonPrefix(test_cases[i].strs, test_cases[i].strsSize, result);
        if (strcmp(result, test_cases[i].expected) == 0) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got '%s', expected '%s'\n", i + 1, result, test_cases[i].expected);
        }
    }
    printf("Passed %d/%d test cases.\n", passed, num_cases);
}

void measure_performance(void (*func)()) {
    printf("\n--- Measuring performance ---\n");

    double mem_before, peak_before, mem_after, peak_after;
    get_memory_usage(&mem_before, &peak_before);

    clock_t cpu_start = clock();
    LARGE_INTEGER freq, wall_start, wall_end;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&wall_start);

    func();

    clock_t cpu_end = clock();
    QueryPerformanceCounter(&wall_end);

    get_memory_usage(&mem_after, &peak_after);

    double wall_time = (double)(wall_end.QuadPart - wall_start.QuadPart) / freq.QuadPart;
    double cpu_time = (double)(cpu_end - cpu_start) / CLOCKS_PER_SEC;

    printf("Wall-clock time: %.6f seconds\n", wall_time);
    printf("CPU process time: %.6f seconds\n", cpu_time);
    printf("Current memory usage: %.6f MB\n", mem_after);
    printf("Peak memory usage: %.6f MB\n", peak_after);
    printf("--- End of measurement ---\n\n");
}

int main() {
    measure_performance(test_longest_common_prefix);
    return 0;
}
