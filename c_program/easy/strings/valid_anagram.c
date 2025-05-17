// filepath: d:\coding_challenge\c_program\easy\strings\valid_anagram.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
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

// Helper: compare for qsort
int cmp_char(const void* a, const void* b) {
    return (*(char*)a) - (*(char*)b);
}

// Check if two strings are anagrams
int isAnagram(const char* s, const char* t) {
    int len_s = strlen(s);
    int len_t = strlen(t);
    if (len_s != len_t) return 0;
    char s_sorted[200], t_sorted[200];
    strcpy(s_sorted, s);
    strcpy(t_sorted, t);
    qsort(s_sorted, len_s, sizeof(char), cmp_char);
    qsort(t_sorted, len_t, sizeof(char), cmp_char);
    return strcmp(s_sorted, t_sorted) == 0;
}

typedef struct {
    char s[200];
    char t[200];
    int expected;
} TestCase;

void test_is_anagram() {
    TestCase test_cases[] = {
        {"anagram", "nagaram", 1},
        {"rat", "car", 0},
        {"", "", 1},
        {"a", "a", 1},
        {"a", "b", 0},
        {"abc", "cba", 1},
        {"abc", "ab", 0},
        {"listen", "silent", 1},
        {"triangle", "integral", 1},
        {"apple", "papel", 1},
        {"apple", "pale", 0},
        {"abcd", "dcba", 1},
        {"abcd", "abce", 0},
        {"aabbcc", "baccab", 1},
        {"aabbcc", "aabbc", 0},
        {"abcabc", "cbacba", 1},
        {"abcabc", "cbacbb", 0},
        {"aabb", "bbaa", 1},
        {"aabb", "bbaaa", 0},
        {"", "a", 0},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = isAnagram(test_cases[i].s, test_cases[i].t);
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
    measure_performance(test_is_anagram);
    return 0;
}
