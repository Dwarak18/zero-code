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

int firstUniqChar(const char* s) {
    int count[256] = {0};
    int len = strlen(s);
    for (int i = 0; i < len; ++i) count[(unsigned char)s[i]]++;
    for (int i = 0; i < len; ++i) if (count[(unsigned char)s[i]] == 1) return i;
    return -1;
}

typedef struct {
    char s[32];
    int expected;
} TestCase;

void test_first_uniq_char() {
    TestCase test_cases[] = {
        {"leetcode", 0},
        {"loveleetcode", 2},
        {"aabb", -1},
        {"", -1},
        {"a", 0},
        {"abcabc", -1},
        {"abcde", 0},
        {"aabbccdde", 8},
        {"aabbccddeeffg", 12},
        {"z", 0},
        {"zz", -1},
        {"abcabcabc", -1},
        {"aabbccddeeff", -1},
        {"aabbccddeeffggh", 14},
        {"aabbccddeeffgghh", -1},
        {"abc", 0},
        {"aab", 2},
        {"aabbc", 4},
        {"aabbcc", -1},
        {"abcdabcd", -1},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = firstUniqChar(test_cases[i].s);
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
    measure_performance(test_first_uniq_char);
    return 0;
}
