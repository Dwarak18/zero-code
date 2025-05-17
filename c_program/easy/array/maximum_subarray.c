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

// maxSubArray function (Kadane's Algorithm)
int maxSubArray(int* nums, int numsSize) {
    int curr_sum = nums[0];
    int max_sum = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        curr_sum = nums[i] > curr_sum + nums[i] ? nums[i] : curr_sum + nums[i];
        max_sum = max_sum > curr_sum ? max_sum : curr_sum;
    }
    return max_sum;
}

typedef struct {
    int nums[20];
    int numsSize;
    int expected;
} TestCase;

void test_max_subarray() {
    TestCase test_cases[] = {
        {{-2,1,-3,4,-1,2,1,-5,4}, 9, 6},
        {{1}, 1, 1},
        {{5,4,-1,7,8}, 5, 23},
        {{1,2,3,4,5}, 5, 15},
        {{-1,-2,-3,-4}, 4, -1},
        {{0,0,0,0}, 4, 0},
        {{1,-1,1,-1,1,-1,1}, 7, 1},
        {{2,-1,2,3,4,-5}, 6, 10},
        {{1,2,-1,2,1,-5,4}, 7, 5},
        {{3,-2,5,-1}, 4, 6},
        {{1,2,3,-2,5}, 5, 9},
        {{1,-2,3,10,-4,7,2,-5}, 8, 18},
        {{1,2,3,4,-10,5,6,7,8}, 9, 26},
        {{1,-1,1,-1,1,-1,1,-1,1}, 9, 1},
        {{1,2,3,-2,5,-3,2,2}, 8, 10},
        {{1,2,3,4,5,-15,10,10}, 8, 20},
        {{1,2,3,4,5,-15,10,10,-5,10}, 10, 25},
        {{1,2,3,4,5,-15,10,10,-5,10,10}, 11, 35},
        {{1,2,3,4,5,-15,10,10,-5,10,10,10}, 12, 45},
        {{1,2,3,4,5,-15,10,10,-5,10,10,10,10}, 13, 55},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = maxSubArray(test_cases[i].nums, test_cases[i].numsSize);
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
    measure_performance(test_max_subarray);
    return 0;
}
