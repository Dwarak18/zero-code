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

void merge(int* nums1, int m, int* nums2, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
        else nums1[k--] = nums2[j--];
    }
    while (j >= 0) nums1[k--] = nums2[j--];
}

typedef struct {
    int nums1[20];
    int m;
    int nums2[20];
    int n;
    int expected[20];
    int expectedSize;
} TestCase;

int arrays_equal(int* a, int* b, int n) {
    for (int i = 0; i < n; ++i) if (a[i] != b[i]) return 0;
    return 1;
}

void test_merge() {
    TestCase test_cases[] = {
        {{1,2,3,0,0,0}, 3, {2,5,6}, 3, {1,2,2,3,5,6}, 6},
        {{1}, 1, {}, 0, {1}, 1},
        {{0}, 0, {1}, 1, {1}, 1},
        {{2,0}, 1, {1}, 1, {1,2}, 2},
        {{4,5,6,0,0,0}, 3, {1,2,3}, 3, {1,2,3,4,5,6}, 6},
        {{1,2,4,5,6,0}, 5, {3}, 1, {1,2,3,4,5,6}, 6},
        {{1,0,0,0}, 1, {2,3,4}, 3, {1,2,3,4}, 4},
        {{0,0,0}, 0, {2,5,6}, 3, {2,5,6}, 3},
        {{1,2,3,0,0,0}, 3, {4,5,6}, 3, {1,2,3,4,5,6}, 6},
        {{1,2,3,0,0,0}, 3, {1,2,3}, 3, {1,1,2,2,3,3}, 6},
        {{1,2,3,0,0,0}, 3, {0,0,0}, 3, {0,0,0,1,2,3}, 6},
        {{0,0,0,0}, 0, {1,2,3,4}, 4, {1,2,3,4}, 4},
        {{1,0,0,0,0}, 1, {2,3,4,5}, 4, {1,2,3,4,5}, 5},
        {{1,2,0,0,0}, 2, {3,4,5}, 3, {1,2,3,4,5}, 5},
        {{1,2,3,4,0,0,0,0}, 4, {5,6,7,8}, 4, {1,2,3,4,5,6,7,8}, 8},
        {{1,2,3,4,0,0,0,0}, 4, {1,2,3,4}, 4, {1,1,2,2,3,3,4,4}, 8},
        {{1,2,3,4,0,0,0,0}, 4, {0,0,0,0}, 4, {0,0,0,0,1,2,3,4}, 8},
        {{0,0,0,0,0}, 0, {1,2,3,4,5}, 5, {1,2,3,4,5}, 5},
        {{1,0,0,0,0,0}, 1, {2,3,4,5,6}, 5, {1,2,3,4,5,6}, 6},
        {{1,2,0,0,0,0}, 2, {3,4,5,6}, 4, {1,2,3,4,5,6}, 6},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int arr1[20];
        memcpy(arr1, test_cases[i].nums1, sizeof(int) * (test_cases[i].m + test_cases[i].n));
        merge(arr1, test_cases[i].m, test_cases[i].nums2, test_cases[i].n);
        if (arrays_equal(arr1, test_cases[i].expected, test_cases[i].expectedSize)) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got [");
            for (int j = 0; j < test_cases[i].expectedSize; ++j) printf("%d%s", arr1[j], j == test_cases[i].expectedSize-1 ? "" : ",");
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
    measure_performance(test_merge);
    return 0;
}
