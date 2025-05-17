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

int searchInsert(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return left;
}

typedef struct {
    int nums[20];
    int numsSize;
    int target;
    int expected;
} TestCase;

void test_search_insert() {
    TestCase test_cases[] = {
        {{1,3,5,6}, 4, 5, 2},
        {{1,3,5,6}, 4, 2, 1},
        {{1,3,5,6}, 4, 7, 4},
        {{1,3,5,6}, 4, 0, 0},
        {{1}, 1, 0, 0},
        {{1}, 1, 1, 0},
        {{1}, 1, 2, 1},
        {{1,2,3,4,5}, 5, 3, 2},
        {{1,2,3,4,5}, 5, 6, 5},
        {{1,2,3,4,5}, 5, 0, 0},
        {{1,2,3,4,5}, 5, 1, 0},
        {{1,2,3,4,5}, 5, 5, 4},
        {{1,2,3,4,5}, 5, 4, 3},
        {{1,2,3,4,5}, 5, 2, 1},
        {{1,2,3,4,5}, 5, -1, 0},
        {{1,2,3,4,5}, 5, 10, 5},
        {{2,4,6,8,10}, 5, 5, 2},
        {{2,4,6,8,10}, 5, 8, 3},
        {{2,4,6,8,10}, 5, 1, 0},
        {{2,4,6,8,10}, 5, 11, 5},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = searchInsert(test_cases[i].nums, test_cases[i].numsSize, test_cases[i].target);
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
    measure_performance(test_search_insert);
    return 0;
}
