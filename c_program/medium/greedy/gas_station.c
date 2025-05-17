// gas_station.c
// C implementation of Gas Station (Greedy) with test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_N 20

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

int canCompleteCircuit(int* gas, int* cost, int n) {
    int sum_gas = 0, sum_cost = 0;
    for (int i = 0; i < n; ++i) { sum_gas += gas[i]; sum_cost += cost[i]; }
    if (sum_gas < sum_cost) return -1;
    int total = 0, start = 0;
    for (int i = 0; i < n; ++i) {
        total += gas[i] - cost[i];
        if (total < 0) {
            start = i + 1;
            total = 0;
        }
    }
    return start;
}

typedef struct {
    int gas[MAX_N];
    int cost[MAX_N];
    int n;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int* gas, int* cost, int n, int expected) {
    memcpy(tc->gas, gas, n * sizeof(int));
    memcpy(tc->cost, cost, n * sizeof(int));
    tc->n = n;
    tc->expected = expected;
}

void test_canCompleteCircuit() {
    TestCase test_cases[20];
    int idx = 0;
    int g1[] = {1,2,3,4,5}, c1[] = {3,4,5,1,2};
    set_test_case(&test_cases[idx++], g1, c1, 5, 3);
    int g2[] = {2,3,4}, c2[] = {3,4,3};
    set_test_case(&test_cases[idx++], g2, c2, 3, -1);
    int g3[] = {5,1,2,3,4}, c3[] = {4,4,1,5,1};
    set_test_case(&test_cases[idx++], g3, c3, 5, 4);
    int g4[] = {1,2,3,4,5}, c4[] = {5,4,3,2,1};
    set_test_case(&test_cases[idx++], g4, c4, 5, 0);
    int g5[] = {2,3,4}, c5[] = {3,4,3};
    set_test_case(&test_cases[idx++], g5, c5, 3, -1);
    int g6[] = {3,3,4}, c6[] = {3,4,4};
    set_test_case(&test_cases[idx++], g6, c6, 3, -1);
    int g7[] = {4,5,2,6,5,3}, c7[] = {3,2,7,3,2,9};
    set_test_case(&test_cases[idx++], g7, c7, 6, 3);
    int g8[] = {1,2,3,4,5}, c8[] = {1,2,3,4,5};
    set_test_case(&test_cases[idx++], g8, c8, 5, 0);
    int g9[] = {1,2,3,4,5}, c9[] = {2,3,4,5,1};
    set_test_case(&test_cases[idx++], g9, c9, 5, 4);
    int g10[] = {2,2,2}, c10[] = {2,2,2};
    set_test_case(&test_cases[idx++], g10, c10, 3, 0);
    int g11[] = {2,2,2}, c11[] = {2,2,3};
    set_test_case(&test_cases[idx++], g11, c11, 3, -1);
    int g12[] = {2,2,2}, c12[] = {3,2,2};
    set_test_case(&test_cases[idx++], g12, c12, 3, 1);
    int g13[] = {2,2,2}, c13[] = {2,3,2};
    set_test_case(&test_cases[idx++], g13, c13, 3, 2);
    int g14[] = {2,2,2}, c14[] = {2,2,3};
    set_test_case(&test_cases[idx++], g14, c14, 3, -1);
    int g15[] = {2,2,2}, c15[] = {3,2,2};
    set_test_case(&test_cases[idx++], g15, c15, 3, 1);
    int g16[] = {2,2,2}, c16[] = {2,3,2};
    set_test_case(&test_cases[idx++], g16, c16, 3, 2);
    int g17[] = {1,2,3,4,5}, c17[] = {3,4,5,1,2};
    set_test_case(&test_cases[idx++], g17, c17, 5, 3);
    int g18[] = {1,2,3,4,5}, c18[] = {2,3,4,5,1};
    set_test_case(&test_cases[idx++], g18, c18, 5, 4);
    int g19[] = {1,2,3,4,5}, c19[] = {1,2,3,4,5};
    set_test_case(&test_cases[idx++], g19, c19, 5, 0);
    int g20[] = {1,2,3,4,5}, c20[] = {5,4,3,2,1};
    set_test_case(&test_cases[idx++], g20, c20, 5, 0);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = canCompleteCircuit(test_cases[i].gas, test_cases[i].cost, test_cases[i].n);
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
    measure_performance(test_canCompleteCircuit);
    return 0;
}
