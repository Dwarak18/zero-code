// minimum_number_of_arrows_to_burst_balloons.c
// C implementation of Minimum Number of Arrows to Burst Balloons (Greedy) with test cases and performance measurement
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

int cmp_end(const void* a, const void* b) {
    int* pa = (int*)a;
    int* pb = (int*)b;
    return pa[1] - pb[1];
}

int findMinArrowShots(int points[MAX_N][2], int n) {
    if (n == 0) return 0;
    qsort(points, n, sizeof(points[0]), cmp_end);
    int arrows = 1;
    int end = points[0][1];
    for (int i = 1; i < n; ++i) {
        if (points[i][0] > end) {
            arrows++;
            end = points[i][1];
        }
    }
    return arrows;
}

typedef struct {
    int points[MAX_N][2];
    int n;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int points[MAX_N][2], int n, int expected) {
    for (int i = 0; i < n; ++i) { tc->points[i][0] = points[i][0]; tc->points[i][1] = points[i][1]; }
    tc->n = n;
    tc->expected = expected;
}

void test_findMinArrowShots() {
    TestCase test_cases[20];
    int idx = 0;
    int p1[MAX_N][2] = {{10,16},{2,8},{1,6},{7,12}};
    set_test_case(&test_cases[idx++], p1, 4, 2);
    int p2[MAX_N][2] = {{1,2},{3,4},{5,6},{7,8}};
    set_test_case(&test_cases[idx++], p2, 4, 4);
    int p3[MAX_N][2] = {{1,2},{2,3},{3,4},{4,5}};
    set_test_case(&test_cases[idx++], p3, 4, 2);
    int p4[MAX_N][2] = {{1,2}};
    set_test_case(&test_cases[idx++], p4, 1, 1);
    int p5[MAX_N][2] = {{2,3},{2,3}};
    set_test_case(&test_cases[idx++], p5, 2, 1);
    int p6[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9}};
    set_test_case(&test_cases[idx++], p6, 5, 5);
    int p7[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2}};
    set_test_case(&test_cases[idx++], p7, 6, 5);
    int p8[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3}};
    set_test_case(&test_cases[idx++], p8, 7, 5);
    int p9[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4}};
    set_test_case(&test_cases[idx++], p9, 8, 5);
    int p10[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5}};
    set_test_case(&test_cases[idx++], p10, 9, 5);
    int p11[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5},{5,6}};
    set_test_case(&test_cases[idx++], p11, 10, 5);
    int p12[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7}};
    set_test_case(&test_cases[idx++], p12, 11, 5);
    int p13[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8}};
    set_test_case(&test_cases[idx++], p13, 12, 5);
    int p14[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9}};
    set_test_case(&test_cases[idx++], p14, 13, 5);
    int p15[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9},{9,10}};
    set_test_case(&test_cases[idx++], p15, 14, 5);
    int p16[MAX_N][2] = {{1,10},{2,3},{4,5},{6,7},{8,9},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9},{9,10},{10,11}};
    set_test_case(&test_cases[idx++], p16, 15, 6);
    int p17[MAX_N][2] = {{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9},{9,10},{10,11}};
    set_test_case(&test_cases[idx++], p17, 10, 5);
    int p18[MAX_N][2] = {{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9},{9,10},{10,11},{11,12}};
    set_test_case(&test_cases[idx++], p18, 11, 6);
    int p19[MAX_N][2] = {{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9},{9,10},{10,11},{11,12},{12,13}};
    set_test_case(&test_cases[idx++], p19, 12, 7);
    int p20[MAX_N][2] = {{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9},{9,10},{10,11},{11,12},{12,13},{13,14}};
    set_test_case(&test_cases[idx++], p20, 13, 8);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = findMinArrowShots(test_cases[i].points, test_cases[i].n);
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
    measure_performance(test_findMinArrowShots);
    return 0;
}
