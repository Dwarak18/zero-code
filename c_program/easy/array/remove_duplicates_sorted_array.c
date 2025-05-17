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

// removeDuplicates function
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int write_index = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] != nums[i - 1]) {
            nums[write_index++] = nums[i];
        }
    }
    return write_index;
}

typedef struct {
    int nums[20];
    int numsSize;
    int expected_length;
} TestCase;

void test_remove_duplicates() {
    TestCase test_cases[] = {
        {{1,1,2}, 3, 2},
        {{0,0,1,1,1,2,2,3,3,4}, 10, 5},
        {{1,2,3,4,5}, 5, 5},
        {{1,1,1,1,1}, 5, 1},
        {{1,2,2,3,3,3,4,4,4,4}, 10, 4},
        {{1}, 1, 1},
        {{}, 0, 0},
        {{2,2,2,2,2,2,2,2,2,2}, 10, 1},
        {{1,2,2,2,3,4,4,5,5,6}, 10, 6},
        {{1,1,2,2,3,3,4,4,5,5}, 10, 5},
        {{1,2,3,3,3,4,5,5,6,7}, 10, 7},
        {{1,1,1,2,2,3,3,4,4,5}, 10, 5},
        {{1,2,3,4,4,4,5,6,7,8}, 10, 8},
        {{1,1,2,3,4,5,6,7,8,9}, 10, 9},
        {{1,2,3,4,5,5,5,5,5,5}, 10, 5},
        {{1,2,3,3,3,3,3,3,3,3}, 10, 3},
        {{1,1,1,1,1,1,1,1,1,2}, 10, 2},
        {{1,2,2,2,2,2,2,2,2,2}, 10, 2},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int arr[20];
        memcpy(arr, test_cases[i].nums, sizeof(int) * test_cases[i].numsSize);
        int length = removeDuplicates(arr, test_cases[i].numsSize);
        if (length == test_cases[i].expected_length) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got %d, expected %d\n", i + 1, length, test_cases[i].expected_length);
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
    measure_performance(test_remove_duplicates);
    return 0;
}
