// filepath: d:\coding_challenge\c_program\easy\strings\reverse_string.c
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

// Reverse a string in-place
void reverseString(char* s, int sSize) {
    int l = 0, r = sSize - 1;
    while (l < r) {
        char tmp = s[l];
        s[l] = s[r];
        s[r] = tmp;
        l++;
        r--;
    }
}

typedef struct {
    char input[100];
    char expected[100];
} TestCase;

void test_reverse_string() {
    TestCase test_cases[] = {
        {"hello", "olleh"},
        {"Hannah", "hannaH"},
        {"a", "a"},
        {"ab", "ba"},
        {"racecar", "racecar"},
        {"", ""},
        {"abcde", "edcba"},
        {"12345", "54321"},
        {"!@#$%", "%$#@!"},
        {"madam", "madam"},
        {"level", "level"},
        {"noon", "noon"},
        {"python", "nohtyp"},
        {"openai", "ianepo"},
        {"race", "ecar"},
        {"data", "atad"},
        {"science", "ecneics"},
        {"reverse", "esrever"},
        {"string", "gnirts"},
        {"test", "tset"},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        char arr[100];
        strcpy(arr, test_cases[i].input);
        reverseString(arr, strlen(arr));
        if (strcmp(arr, test_cases[i].expected) == 0) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got '%s', expected '%s'\n", i + 1, arr, test_cases[i].expected);
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
    measure_performance(test_reverse_string);
    return 0;
}
