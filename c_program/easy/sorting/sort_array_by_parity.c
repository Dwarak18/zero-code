#include <stdio.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>
#include <string.h>

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

void sortArrayByParity(int* A, int ASize, int* out) {
    int even = 0;
    for (int i = 0; i < ASize; ++i) {
        if (A[i] % 2 == 0) out[even++] = A[i];
    }
    for (int i = 0; i < ASize; ++i) {
        if (A[i] % 2 != 0) out[even++] = A[i];
    }
}

typedef struct {
    int A[20];
    int ASize;
    int expected[20];
    int expectedSize;
} TestCase;

int arrays_equal(int* a, int* b, int n) {
    for (int i = 0; i < n; ++i) if (a[i] != b[i]) return 0;
    return 1;
}

void test_sort_array_by_parity() {
    TestCase test_cases[] = {
        {{3,1,2,4}, 4, {2,4,3,1}, 4},
        {{0}, 1, {0}, 1},
        {{1}, 1, {1}, 1},
        {{2,4,6,8}, 4, {2,4,6,8}, 4},
        {{1,3,5,7}, 4, {1,3,5,7}, 4},
        {{2,1}, 2, {2,1}, 2},
        {{1,2}, 2, {2,1}, 2},
        {{2,2,2,1,1,1}, 6, {2,2,2,1,1,1}, 6},
        {{1,1,1,2,2,2}, 6, {2,2,2,1,1,1}, 6},
        {{2,1,4,3}, 4, {2,4,1,3}, 4},
        {{1,2,3,4,5,6}, 6, {2,4,6,1,3,5}, 6},
        {{6,5,4,3,2,1}, 6, {6,4,2,5,3,1}, 6},
        {{1,3,5,2,4,6}, 6, {2,4,6,1,3,5}, 6},
        {{2,1,2,1,2,1}, 6, {2,2,2,1,1,1}, 6},
        {{1,2,1,2,1,2}, 6, {2,2,2,1,1,1}, 6},
        {{2,2,2,2,2,2}, 6, {2,2,2,2,2,2}, 6},
        {{1,1,1,1,1,1}, 6, {1,1,1,1,1,1}, 6},
        {{2,1,3,4,5,6,7,8,9,10}, 10, {2,4,6,8,10,1,3,5,7,9}, 10},
        {{10,9,8,7,6,5,4,3,2,1}, 10, {10,8,6,4,2,9,7,5,3,1}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {2,4,6,8,10,1,3,5,7,9}, 10},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int out[20];
        sortArrayByParity(test_cases[i].A, test_cases[i].ASize, out);
        if (arrays_equal(out, test_cases[i].expected, test_cases[i].expectedSize)) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got [");
            for (int j = 0; j < test_cases[i].expectedSize; ++j) printf("%d%s", out[j], j == test_cases[i].expectedSize-1 ? "" : ",");
            printf("], expected [");
            for (int j = 0; j < test_cases[i].expectedSize; ++j) printf("%d%s", test_cases[i].expected[j], j == test_cases[i].expectedSize-1 ? "" : ",");
            printf("]\n");
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
    measure_performance(test_sort_array_by_parity);
    return 0;
}
