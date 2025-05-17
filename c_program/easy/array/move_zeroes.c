#include <stdio.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>
#include <string.h>

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

// moveZeroes function
void moveZeroes(int* nums, int numsSize) {
    int zero_index = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != 0) {
            nums[zero_index++] = nums[i];
        }
    }
    for (int i = zero_index; i < numsSize; ++i) {
        nums[i] = 0;
    }
}

typedef struct {
    int nums[20];
    int numsSize;
    int expected[20];
    int expectedSize;
} TestCase;

int arrays_equal(int* a, int* b, int n) {
    for (int i = 0; i < n; ++i) {
        if (a[i] != b[i]) return 0;
    }
    return 1;
}

void test_move_zeroes() {
    TestCase test_cases[] = {
        {{0,1,0,3,12}, 5, {1,3,12,0,0}, 5},
        {{0,0,1}, 3, {1,0,0}, 3},
        {{1,0,1}, 3, {1,1,0}, 3},
        {{0,0,0,0}, 4, {0,0,0,0}, 4},
        {{1,2,3,4}, 4, {1,2,3,4}, 4},
        {{0,1,2,0,3,0,4}, 7, {1,2,3,4,0,0,0}, 7},
        {{1,0,0,2,0,3}, 6, {1,2,3,0,0,0}, 6},
        {{0,0,1,0,0,2,0,0,3}, 9, {1,2,3,0,0,0,0,0,0}, 9},
        {{1,2,0,0,3,4,0,5}, 8, {1,2,3,4,5,0,0,0}, 8},
        {{0,1,0,2,0,3,0,4,0,5}, 10, {1,2,3,4,5,0,0,0,0,0}, 10},
        {{1,0,2,0,3,0,4,0,5,0}, 10, {1,2,3,4,5,0,0,0,0,0}, 10},
        {{0,0,0,1}, 4, {1,0,0,0}, 4},
        {{1,0,0,0}, 4, {1,0,0,0}, 4},
        {{0,1,0,0}, 4, {1,0,0,0}, 4},
        {{1,0,0,0,0}, 5, {1,0,0,0,0}, 5},
        {{0,0,0,0,1}, 5, {1,0,0,0,0}, 5},
        {{1,2,0,0,0,3,4,0,5}, 9, {1,2,3,4,5,0,0,0,0}, 9},
        {{0,0,0,0,0,0,0,0,0,1}, 10, {1,0,0,0,0,0,0,0,0,0}, 10},
        {{1,0,0,0,0,0,0,0,0,0}, 10, {1,0,0,0,0,0,0,0,0,0}, 10},
        {{0,0,0,0,0,0,0,0,0,0}, 10, {0,0,0,0,0,0,0,0,0,0}, 10},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int arr[20];
        memcpy(arr, test_cases[i].nums, sizeof(int) * test_cases[i].numsSize);
        moveZeroes(arr, test_cases[i].numsSize);
        if (arrays_equal(arr, test_cases[i].expected, test_cases[i].expectedSize)) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got [", i + 1);
            for (int j = 0; j < test_cases[i].numsSize; ++j) printf("%d%s", arr[j], j == test_cases[i].numsSize-1 ? "" : ",");
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
    measure_performance(test_move_zeroes);
    return 0;
}
