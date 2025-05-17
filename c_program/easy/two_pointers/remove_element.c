// remove_element.c
// C implementation of remove element with test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

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

int removeElement(int* nums, int numsSize, int val) {
    int k = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != val) {
            nums[k++] = nums[i];
        }
    }
    return k;
}

typedef struct {
    int nums[20];
    int numsSize;
    int val;
    int expected_len;
    int expected_arr[20];
} TestCase;

void set_test_case(TestCase* tc, int* nums, int n, int val, int expected_len, int* expected_arr) {
    memcpy(tc->nums, nums, n * sizeof(int));
    tc->numsSize = n;
    tc->val = val;
    tc->expected_len = expected_len;
    memcpy(tc->expected_arr, expected_arr, expected_len * sizeof(int));
}

int arrays_equal(int* a, int n, int* b, int m) {
    if (n != m) return 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] != b[i]) return 0;
    }
    return 1;
}

void test_remove_element() {
    TestCase test_cases[20];
    int idx = 0;
    int a1[] = {3,2,2,3}, a2[] = {2,2};
    set_test_case(&test_cases[idx++], a1, 4, 3, 2, a2);
    int b1[] = {0,1,2,2,3,0,4,2}, b2[] = {0,1,3,0,4};
    set_test_case(&test_cases[idx++], b1, 8, 2, 5, b2);
    int c1[] = {1}, c2[] = {};
    set_test_case(&test_cases[idx++], c1, 1, 1, 0, c2);
    int d1[] = {1,2,3,4,5}, d2[] = {1,2,3,4,5};
    set_test_case(&test_cases[idx++], d1, 5, 6, 5, d2);
    int e1[] = {1,1,1,1}, e2[] = {};
    set_test_case(&test_cases[idx++], e1, 4, 1, 0, e2);
    int f1[] = {2,2,2,2}, f2[] = {};
    set_test_case(&test_cases[idx++], f1, 4, 2, 0, f2);
    int g1[] = {1,2,3,4,5}, g2[] = {1,2,4,5};
    set_test_case(&test_cases[idx++], g1, 5, 3, 4, g2);
    int h1[] = {1,2,2,3,4}, h2[] = {1,3,4};
    set_test_case(&test_cases[idx++], h1, 5, 2, 3, h2);
    int i1[] = {1,2,3,4,5}, i2[] = {1,2,3,4};
    set_test_case(&test_cases[idx++], i1, 5, 5, 4, i2);
    int j1[] = {1,2,3,4,5}, j2[] = {2,3,4,5};
    set_test_case(&test_cases[idx++], j1, 5, 1, 4, j2);
    int k1[] = {1,2,3,4,5}, k2[] = {1,3,4,5};
    set_test_case(&test_cases[idx++], k1, 5, 2, 4, k2);
    int l1[] = {1,2,3,4,5}, l2[] = {1,2,3,5};
    set_test_case(&test_cases[idx++], l1, 5, 4, 4, l2);
    int m1[] = {1,2,3,4,5}, m2[] = {1,2,3,4,5};
    set_test_case(&test_cases[idx++], m1, 5, 0, 5, m2);
    int n1[] = {1,1,2,2,3,3,4,4}, n2[] = {1,1,2,2,4,4};
    set_test_case(&test_cases[idx++], n1, 8, 3, 6, n2);
    int o1[] = {1,2,3,4,5,1,2,3,4,5}, o2[] = {2,3,4,5,2,3,4,5};
    set_test_case(&test_cases[idx++], o1, 10, 1, 8, o2);
    int p1[] = {1,2,3,4,5,1,2,3,4,5}, p2[] = {1,2,3,4,1,2,3,4};
    set_test_case(&test_cases[idx++], p1, 10, 5, 8, p2);
    int q1[] = {1,2,3,4,5,1,2,3,4,5}, q2[] = {1,3,4,5,1,3,4,5};
    set_test_case(&test_cases[idx++], q1, 10, 2, 8, q2);
    int r1[] = {1,2,3,4,5,1,2,3,4,5}, r2[] = {1,2,4,5,1,2,4,5};
    set_test_case(&test_cases[idx++], r1, 10, 3, 8, r2);
    int s1[] = {1,2,3,4,5,1,2,3,4,5}, s2[] = {1,2,3,5,1,2,3,5};
    set_test_case(&test_cases[idx++], s1, 10, 4, 8, s2);
    int t1[] = {1,2,3,4,5,1,2,3,4,5}, t2[] = {1,2,3,4,5,1,2,3,4,5};
    set_test_case(&test_cases[idx++], t1, 10, 0, 10, t2);

    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int arr[20];
        memcpy(arr, test_cases[i].nums, test_cases[i].numsSize * sizeof(int));
        int k = removeElement(arr, test_cases[i].numsSize, test_cases[i].val);
        if (k == test_cases[i].expected_len && arrays_equal(arr, k, test_cases[i].expected_arr, k)) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got ", i + 1);
            for (int j = 0; j < k; ++j) printf("%d ", arr[j]);
            printf(", expected ");
            for (int j = 0; j < test_cases[i].expected_len; ++j) printf("%d ", test_cases[i].expected_arr[j]);
            printf("\n");
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
    measure_performance(test_remove_element);
    return 0;
}
