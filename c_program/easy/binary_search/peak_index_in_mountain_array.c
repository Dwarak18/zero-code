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

int peakIndexInMountainArray(int* arr, int arrSize) {
    int left = 0, right = arrSize - 1;
    while (left < right) {
        int mid = (left + right) / 2;
        if (arr[mid] < arr[mid + 1]) left = mid + 1;
        else right = mid;
    }
    return left;
}

typedef struct {
    int arr[20];
    int arrSize;
    int expected;
} TestCase;

void test_peak_index() {
    TestCase test_cases[] = {
        {{0,1,0}, 3, 1},
        {{0,2,1,0}, 4, 1},
        {{0,10,5,2}, 4, 1},
        {{3,4,5,1}, 4, 2},
        {{24,69,100,99,79,78,67,36,26,19}, 10, 2},
        {{1,2,3,4,5,3,1}, 7, 4},
        {{0,1,2,3,4,5,6,7,8,9,10,5,2}, 13, 10},
        {{18,29,38,59,98,100,99,98,90}, 9, 5},
        {{0,1,2,3,2,1,0}, 7, 3},
        {{0,2,4,6,8,10,8,6,4,2,0}, 11, 5},
        {{1,3,5,7,6,4,2}, 7, 3},
        {{2,4,6,8,10,9,7,5,3,1}, 10, 4},
        {{0,5,10,5,0}, 5, 2},
        {{0,2,1,0}, 4, 1},
        {{0,1,0}, 3, 1},
        {{1,3,2}, 3, 1},
        {{0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0}, 19, 9},
        {{0,1,2,3,4,3,2,1,0}, 9, 4},
        {{0,1,0}, 3, 1},
        {{0,2,1,0}, 4, 1},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = peakIndexInMountainArray(test_cases[i].arr, test_cases[i].arrSize);
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
    measure_performance(test_peak_index);
    return 0;
}
