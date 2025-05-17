// jump_game.c
// C implementation of Jump Game (Greedy) with test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_N 32

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

int canJump(int* nums, int n) {
    int max_reach = 0;
    for (int i = 0; i < n; ++i) {
        if (i > max_reach) return 0;
        if (i + nums[i] > max_reach) max_reach = i + nums[i];
    }
    return 1;
}

typedef struct {
    int nums[MAX_N];
    int n;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int* nums, int n, int expected) {
    memcpy(tc->nums, nums, n * sizeof(int));
    tc->n = n;
    tc->expected = expected;
}

void test_canJump() {
    TestCase test_cases[20];
    int idx = 0;
    int a1[] = {2,3,1,1,4};
    set_test_case(&test_cases[idx++], a1, 5, 1);
    int a2[] = {3,2,1,0,4};
    set_test_case(&test_cases[idx++], a2, 5, 0);
    int a3[] = {0};
    set_test_case(&test_cases[idx++], a3, 1, 1);
    int a4[] = {2,0,0};
    set_test_case(&test_cases[idx++], a4, 3, 1);
    int a5[] = {1,2,3};
    set_test_case(&test_cases[idx++], a5, 3, 1);
    int a6[] = {1,0,1,0};
    set_test_case(&test_cases[idx++], a6, 4, 0);
    int a7[] = {2,5,0,0};
    set_test_case(&test_cases[idx++], a7, 4, 1);
    int a8[] = {1,1,1,1,1};
    set_test_case(&test_cases[idx++], a8, 5, 1);
    int a9[] = {1,1,0,1};
    set_test_case(&test_cases[idx++], a9, 4, 0);
    int a10[] = {2,0,6,9,8,4,5,0,8,9,1,2,1,2,6,5,1,2,6,3};
    set_test_case(&test_cases[idx++], a10, 20, 1);
    int a11[] = {1,2,0,1,0,2,0};
    set_test_case(&test_cases[idx++], a11, 7, 1);
    int a12[] = {1,1,1,0};
    set_test_case(&test_cases[idx++], a12, 4, 1);
    int a13[] = {1,0,0,0};
    set_test_case(&test_cases[idx++], a13, 4, 0);
    int a14[] = {2,0,0,0};
    set_test_case(&test_cases[idx++], a14, 4, 1);
    int a15[] = {0,2,3};
    set_test_case(&test_cases[idx++], a15, 3, 0);
    int a16[] = {2,3,1,1,0,4};
    set_test_case(&test_cases[idx++], a16, 6, 0);
    int a17[] = {2,3,1,1,0,0,4};
    set_test_case(&test_cases[idx++], a17, 7, 0);
    int a18[] = {2,3,1,1,0,0,0,4};
    set_test_case(&test_cases[idx++], a18, 8, 0);
    int a19[] = {2,3,1,1,0,0,0,0,4};
    set_test_case(&test_cases[idx++], a19, 9, 0);
    int a20[] = {2,3,1,1,0,0,0,0,0,4};
    set_test_case(&test_cases[idx++], a20, 10, 0);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = canJump(test_cases[i].nums, test_cases[i].n);
        if (result == test_cases[i].expected) {
            printf("Test case %d passed.\n", i+1);
            passed++;
        } else {
            printf("Test case %d failed: got %d, expected %d\n", i+1, result, test_cases[i].expected);
        }
    }
    printf("Passed %d/%d test cases.\n", passed, idx);
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
    measure_performance(test_canJump);
    return 0;
}
