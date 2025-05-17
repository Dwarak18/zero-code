#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

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

int strStr(const char* haystack, const char* needle) {
    int n = strlen(haystack), m = strlen(needle);
    if (m == 0) return 0;
    for (int i = 0; i <= n - m; ++i) {
        if (strncmp(haystack + i, needle, m) == 0) return i;
    }
    return -1;
}

typedef struct {
    char haystack[32];
    char needle[32];
    int expected;
} TestCase;

void test_strStr() {
    TestCase test_cases[] = {
        {"hello", "ll", 2},
        {"aaaaa", "bba", -1},
        {"", "", 0},
        {"a", "a", 0},
        {"a", "b", -1},
        {"mississippi", "issip", 4},
        {"mississippi", "issi", 1},
        {"mississippi", "mississippi", 0},
        {"mississippi", "mississippia", -1},
        {"abc", "c", 2},
        {"abc", "", 0},
        {"", "a", -1},
        {"needle", "needle", 0},
        {"needle", "le", 4},
        {"abcabcabc", "cab", 2},
        {"abcabcabc", "bca", 1},
        {"abcabcabc", "abc", 0},
        {"abcabcabc", "abcd", -1},
        {"abc", "abcabc", -1},
        {"abcabcabc", "cabc", 2},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = strStr(test_cases[i].haystack, test_cases[i].needle);
        if (result == test_cases[i].expected) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got %d, expected %d\n", i + 1, result, test_cases[i].expected);
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
    measure_performance(test_strStr);
    return 0;
}
