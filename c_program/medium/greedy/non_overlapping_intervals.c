// non_overlapping_intervals.c
// C implementation of Non-overlapping Intervals (Greedy) with test cases and performance measurement
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

int eraseOverlapIntervals(int intervals[MAX_N][2], int n) {
    if (n == 0) return 0;
    qsort(intervals, n, sizeof(intervals[0]), cmp_end);
    int count = 0;
    int end = intervals[0][1];
    for (int i = 1; i < n; ++i) {
        if (intervals[i][0] < end) {
            count++;
        } else {
            end = intervals[i][1];
        }
    }
    return count;
}

typedef struct {
    int intervals[MAX_N][2];
    int n;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int intervals[MAX_N][2], int n, int expected) {
    for (int i = 0; i < n; ++i) { tc->intervals[i][0] = intervals[i][0]; tc->intervals[i][1] = intervals[i][1]; }
    tc->n = n;
    tc->expected = expected;
}

void test_eraseOverlapIntervals() {
    TestCase test_cases[20];
    int idx = 0;
    int i1[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3}};
    set_test_case(&test_cases[idx++], i1, 4, 1);
    int i2[MAX_N][2] = {{1,2},{1,2},{1,2}};
    set_test_case(&test_cases[idx++], i2, 3, 2);
    int i3[MAX_N][2] = {{1,2},{2,3}};
    set_test_case(&test_cases[idx++], i3, 2, 0);
    int i4[MAX_N][2] = {{1,100},{11,22},{1,11},{2,12}};
    set_test_case(&test_cases[idx++], i4, 4, 2);
    int i5[MAX_N][2] = {{0,2},{1,3},{2,4},{3,5},{4,6}};
    set_test_case(&test_cases[idx++], i5, 5, 2);
    int i6[MAX_N][2] = {{1,5},{2,3},{3,4},{4,5}};
    set_test_case(&test_cases[idx++], i6, 4, 1);
    int i7[MAX_N][2] = {{1,2}};
    set_test_case(&test_cases[idx++], i7, 1, 0);
    int i8[MAX_N][2] = {{1,2},{2,3},{3,4},{4,5}};
    set_test_case(&test_cases[idx++], i8, 4, 0);
    int i9[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4}};
    set_test_case(&test_cases[idx++], i9, 5, 2);
    int i10[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5}};
    set_test_case(&test_cases[idx++], i10, 6, 3);
    int i11[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6}};
    set_test_case(&test_cases[idx++], i11, 7, 4);
    int i12[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7}};
    set_test_case(&test_cases[idx++], i12, 8, 5);
    int i13[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8}};
    set_test_case(&test_cases[idx++], i13, 9, 6);
    int i14[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9}};
    set_test_case(&test_cases[idx++], i14, 10, 7);
    int i15[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9},{8,10}};
    set_test_case(&test_cases[idx++], i15, 11, 8);
    int i16[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9},{8,10},{9,11}};
    set_test_case(&test_cases[idx++], i16, 12, 9);
    int i17[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9},{8,10},{9,11},{10,12}};
    set_test_case(&test_cases[idx++], i17, 13, 10);
    int i18[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9},{8,10},{9,11},{10,12},{11,13}};
    set_test_case(&test_cases[idx++], i18, 14, 11);
    int i19[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9},{8,10},{9,11},{10,12},{11,13},{12,14}};
    set_test_case(&test_cases[idx++], i19, 15, 12);
    int i20[MAX_N][2] = {{1,2},{2,3},{3,4},{1,3},{2,4},{3,5},{4,6},{5,7},{6,8},{7,9},{8,10},{9,11},{10,12},{11,13},{12,14},{13,15}};
    set_test_case(&test_cases[idx++], i20, 16, 13);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = eraseOverlapIntervals(test_cases[i].intervals, test_cases[i].n);
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
    measure_performance(test_eraseOverlapIntervals);
    return 0;
}
