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

// Helper to reverse a subarray
void reverse(int* arr, int start, int end) {
    while (start < end) {
        int tmp = arr[start];
        arr[start] = arr[end];
        arr[end] = tmp;
        start++;
        end--;
    }
}

// rotate function
void rotate(int* nums, int numsSize, int k) {
    if (numsSize == 0) return;
    k = k % numsSize;
    if (k == 0) return;
    reverse(nums, 0, numsSize - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, numsSize - 1);
}

typedef struct {
    int nums[20];
    int numsSize;
    int k;
    int expected[20];
    int expectedSize;
} TestCase;

int arrays_equal(int* a, int* b, int n) {
    for (int i = 0; i < n; ++i) {
        if (a[i] != b[i]) return 0;
    }
    return 1;
}

void test_rotate() {
    TestCase test_cases[] = {
        {{1,2,3,4,5,6,7}, 7, 3, {5,6,7,1,2,3,4}, 7},
        {{1,2,3,4,5,6,7}, 7, 1, {7,1,2,3,4,5,6}, 7},
        {{1,2,3,4,5,6,7}, 7, 7, {1,2,3,4,5,6,7}, 7},
        {{1,2,3,4,5,6,7}, 7, 0, {1,2,3,4,5,6,7}, 7},
        {{1,2,3,4,5,6,7}, 7, 2, {6,7,1,2,3,4,5}, 7},
        {{1,2,3,4,5,6,7}, 7, 4, {4,5,6,7,1,2,3}, 7},
        {{1,2,3,4,5,6,7}, 7, 5, {3,4,5,6,7,1,2}, 7},
        {{1,2,3,4,5,6,7}, 7, 6, {2,3,4,5,6,7,1}, 7},
        {{1,2,3,4,5,6,7}, 7, 8, {7,1,2,3,4,5,6}, 7},
        {{1,2,3,4,5,6,7}, 7, 10, {5,6,7,1,2,3,4}, 7},
        {{1,2,3,4,5,6,7}, 7, 14, {1,2,3,4,5,6,7}, 7},
        {{1,2,3,4,5,6,7}, 7, 13, {2,3,4,5,6,7,1}, 7},
        {{1,2,3,4,5,6,7}, 7, 12, {3,4,5,6,7,1,2}, 7},
        {{1,2,3,4,5,6,7}, 7, 11, {4,5,6,7,1,2,3}, 7},
        {{1,2,3,4,5,6,7}, 7, 9, {6,7,1,2,3,4,5}, 7},
        {{1,2,3,4,5,6,7}, 7, 15, {7,1,2,3,4,5,6}, 7},
        {{1,2,3,4,5,6,7}, 7, 16, {6,7,1,2,3,4,5}, 7},
        {{1,2,3,4,5,6,7}, 7, 17, {5,6,7,1,2,3,4}, 7},
        {{1,2,3,4,5,6,7}, 7, 18, {4,5,6,7,1,2,3}, 7},
        {{1,2,3,4,5,6,7}, 7, 19, {3,4,5,6,7,1,2}, 7},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int arr[20];
        memcpy(arr, test_cases[i].nums, sizeof(int) * test_cases[i].numsSize);
        rotate(arr, test_cases[i].numsSize, test_cases[i].k);
        if (arrays_equal(arr, test_cases[i].expected, test_cases[i].expectedSize)) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got [");
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
    measure_performance(test_rotate);
    return 0;
}
