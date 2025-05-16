#include <stdio.h>
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

// The twoSum function
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                int* result = (int*)malloc(2 * sizeof(int));
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

// Test cases
typedef struct {
    int nums[10];
    int numsSize;
    int target;
    int expected[2];
    int expectedSize;
    int expectNull;
} TestCase;

void test_two_sum() {
    TestCase test_cases[] = {
        {{2, 7, 11, 15}, 4, 9, {0, 1}, 2, 0},
        {{3, 2, 4}, 3, 6, {1, 2}, 2, 0},
        {{3, 3}, 2, 6, {0, 1}, 2, 0},
        {{1, 2, 3, 4, 5}, 5, 9, {3, 4}, 2, 0},
        {{0, 4, 3, 0}, 4, 0, {0, 3}, 2, 0},
        {{-1, -2, -3, -4, -5}, 5, -8, {2, 4}, 2, 0},
        {{1, 5, 1, 5}, 4, 10, {1, 3}, 2, 0},
        {{1, 2}, 2, 3, {0, 1}, 2, 0},
        {{1, 2, 3}, 3, 7, {0, 0}, 0, 1},
        {{2, 5, 5, 11}, 4, 10, {1, 2}, 2, 0},
        {{1, 3, 4, 2}, 4, 6, {2, 3}, 2, 0},
        {{1, 2, 3, 4, 4}, 5, 8, {3, 4}, 2, 0},
        {{1, 2, 3, 4, 5, 6}, 6, 11, {4, 5}, 2, 0},
        {{1, 2, 3, 4, 5, 6}, 6, 7, {0, 5}, 2, 0},
        {{1, 2, 3, 4, 5, 6}, 6, 2, {0, 0}, 0, 1},
        {{1, 2, 3, 4, 5, 6}, 6, 12, {0, 0}, 0, 1},
        {{1, 2, 3, 4, 5, 6}, 6, 5, {0, 3}, 2, 0},
        {{1, 2, 3, 4, 5, 6}, 6, 9, {2, 5}, 2, 0},
        {{1, 2, 3, 4, 5, 6}, 6, 10, {3, 5}, 2, 0},
        {{1, 2, 3, 4, 5, 6}, 6, 8, {1, 5}, 2, 0},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int returnSize = 0;
        int* result = twoSum(test_cases[i].nums, test_cases[i].numsSize, test_cases[i].target, &returnSize);
        int ok = 0;
        if (test_cases[i].expectNull) {
            ok = (result == NULL);
        } else if (result && returnSize == 2) {
            ok = (result[0] == test_cases[i].expected[0] && result[1] == test_cases[i].expected[1]);
        }
        if (ok) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            if (result && returnSize == 2)
                printf("Test case %d failed: got [%d, %d], expected [%d, %d]\n", i + 1, result[0], result[1], test_cases[i].expected[0], test_cases[i].expected[1]);
            else
                printf("Test case %d failed: got NULL, expected [%d, %d]\n", i + 1, test_cases[i].expected[0], test_cases[i].expected[1]);
        }
        if (result) free(result);
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
    measure_performance(test_two_sum);
    return 0;
}