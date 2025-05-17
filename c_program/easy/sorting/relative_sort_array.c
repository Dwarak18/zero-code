#include <stdio.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>

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

// Global order map for custom sort
int order_map[1010];

int cmp(const void* a, const void* b) {
    int x = *(int*)a, y = *(int*)b;
    int ox = order_map[x], oy = order_map[y];
    if (ox != oy) return ox - oy;
    return x - y;
}

void relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    for (int i = 0; i < 1010; ++i) order_map[i] = 1001;
    for (int i = 0; i < arr2Size; ++i) order_map[arr2[i]] = i;
    qsort(arr1, arr1Size, sizeof(int), cmp);
}

typedef struct {
    int arr1[20];
    int arr1Size;
    int arr2[20];
    int arr2Size;
    int expected[20];
    int expectedSize;
} TestCase;

int arrays_equal(int* a, int* b, int n) {
    for (int i = 0; i < n; ++i) if (a[i] != b[i]) return 0;
    return 1;
}

void test_relative_sort_array() {
    TestCase test_cases[] = {
        {{2,3,1,3,2,4,6,7,9,2,19}, 11, {2,1,4,3,9,6}, 6, {2,2,2,1,4,3,3,9,6,7,19}, 11},
        {{28,6,22,8,44,17}, 6, {22,28,8,6}, 4, {22,28,8,6,17,44}, 6},
        {{1,2,3,4,5}, 5, {2,1,4}, 3, {2,1,4,3,5}, 5},
        {{1,2,3,4,5}, 5, {5,4,3,2,1}, 5, {5,4,3,2,1}, 5},
        {{1,2,3,4,5}, 5, {1,2,3}, 3, {1,2,3,4,5}, 5},
        {{1,2,3,4,5}, 5, {6,7,8}, 3, {1,2,3,4,5}, 5},
        {{2,3,1,3,2,4,6,7,9,2,19}, 11, {2,1,4,3,9,6,7,19}, 8, {2,2,2,1,4,3,3,9,6,7,19}, 11},
        {{2,3,1,3,2,4,6,7,9,2,19}, 11, {}, 0, {1,2,2,2,3,3,4,6,7,9,19}, 11},
        {{1,1,1,2,2,2,3,3,3}, 9, {3,2,1}, 3, {3,3,3,2,2,2,1,1,1}, 9},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {2,4,6,8,10}, 5, {2,4,6,8,10,1,3,5,7,9}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {10,9,8,7,6}, 5, {10,9,8,7,6,1,2,3,4,5}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {1,2,3,4,5}, 5, {1,2,3,4,5,6,7,8,9,10}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {11,12,13}, 3, {1,2,3,4,5,6,7,8,9,10}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {10,9,8,7,6,5,4,3,2,1}, 10, {10,9,8,7,6,5,4,3,2,1}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {}, 0, {1,2,3,4,5,6,7,8,9,10}, 10},
        {{1,1,1,1,1,1,1,1,1,1}, 10, {1}, 1, {1,1,1,1,1,1,1,1,1,1}, 10},
        {{2,2,2,2,2,2,2,2,2,2}, 10, {2}, 1, {2,2,2,2,2,2,2,2,2,2}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {5,6,7,8,9,10}, 6, {5,6,7,8,9,10,1,2,3,4}, 10},
        {{1,2,3,4,5,6,7,8,9,10}, 10, {1,3,5,7,9}, 5, {1,3,5,7,9,2,4,6,8,10}, 10},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int arr1[20];
        memcpy(arr1, test_cases[i].arr1, sizeof(int) * test_cases[i].arr1Size);
        relativeSortArray(arr1, test_cases[i].arr1Size, test_cases[i].arr2, test_cases[i].arr2Size);
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
    measure_performance(test_relative_sort_array);
    return 0;
}
