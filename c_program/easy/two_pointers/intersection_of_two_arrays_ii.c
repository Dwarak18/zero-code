// intersection_of_two_arrays_ii.c
// C implementation of intersection of two arrays II with test cases and performance measurement
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

// Helper function for qsort
int cmp_int(const void *a, const void *b) {
    return (*(int*)a) - (*(int*)b);
}

// Find intersection of two arrays (allow duplicates)
int intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* out) {
    qsort(nums1, nums1Size, sizeof(int), cmp_int);
    qsort(nums2, nums2Size, sizeof(int), cmp_int);
    int i = 0, j = 0, k = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] == nums2[j]) {
            out[k++] = nums1[i];
            i++; j++;
        } else if (nums1[i] < nums2[j]) {
            i++;
        } else {
            j++;
        }
    }
    return k;
}

typedef struct {
    int nums1[20];
    int nums1Size;
    int nums2[20];
    int nums2Size;
    int expected[20];
    int expectedSize;
} TestCase;

void set_test_case(TestCase* tc, int* nums1, int n1, int* nums2, int n2, int* expected, int eSize) {
    memcpy(tc->nums1, nums1, n1 * sizeof(int));
    tc->nums1Size = n1;
    memcpy(tc->nums2, nums2, n2 * sizeof(int));
    tc->nums2Size = n2;
    memcpy(tc->expected, expected, eSize * sizeof(int));
    tc->expectedSize = eSize;
}

int arrays_equal(int* a, int n, int* b, int m) {
    if (n != m) return 0;
    int tmp1[20], tmp2[20];
    memcpy(tmp1, a, n * sizeof(int));
    memcpy(tmp2, b, n * sizeof(int));
    qsort(tmp1, n, sizeof(int), cmp_int);
    qsort(tmp2, n, sizeof(int), cmp_int);
    for (int i = 0; i < n; ++i) {
        if (tmp1[i] != tmp2[i]) return 0;
    }
    return 1;
}

void test_intersect() {
    TestCase test_cases[21];
    int idx = 0;
    int a1[] = {1,2,2,1}, a2[] = {2,2}, e1[] = {2,2};
    set_test_case(&test_cases[idx++], a1, 4, a2, 2, e1, 2);
    int b1[] = {4,9,5}, b2[] = {9,4,9,8,4}, e2[] = {4,9};
    set_test_case(&test_cases[idx++], b1, 3, b2, 5, e2, 2);
    int c1[] = {1,2,2,1}, c2[] = {2}, e3[] = {2};
    set_test_case(&test_cases[idx++], c1, 4, c2, 1, e3, 1);
    int d1[] = {1,2,2,1}, d2[] = {3}, e4[] = {};
    set_test_case(&test_cases[idx++], d1, 4, d2, 1, e4, 0);
    int e5_1[] = {1}, e5_2[] = {1}, e5_e[] = {1};
    set_test_case(&test_cases[idx++], e5_1, 1, e5_2, 1, e5_e, 1);
    int f1[] = {1,2,2,1}, f2[] = {1,1}, f3[] = {1,1};
    set_test_case(&test_cases[idx++], f1, 4, f2, 2, f3, 2);
    int g1[] = {1,2,2,1}, g2[] = {2,2,2}, g3[] = {2,2};
    set_test_case(&test_cases[idx++], g1, 4, g2, 3, g3, 2);
    int h1[] = {1,2,3,4,5}, h2[] = {6,7,8,9}, h3[] = {};
    set_test_case(&test_cases[idx++], h1, 5, h2, 4, h3, 0);
    int i1[] = {1,1,1,1}, i2[] = {1,1}, i3[] = {1,1};
    set_test_case(&test_cases[idx++], i1, 4, i2, 2, i3, 2);
    int j1[] = {2,2,2}, j2[] = {2,2}, j3[] = {2,2};
    set_test_case(&test_cases[idx++], j1, 3, j2, 2, j3, 2);
    int k1[] = {1,2,3}, k2[] = {1,1,1,2,2,3,3}, k3[] = {1,2,3};
    set_test_case(&test_cases[idx++], k1, 3, k2, 7, k3, 3);
    int l1[] = {1,2,2,3}, l2[] = {2,2,3,3}, l3[] = {2,2,3};
    set_test_case(&test_cases[idx++], l1, 4, l2, 4, l3, 3);
    int m1[] = {1,2,3,4}, m2[] = {2,4,6,8}, m3[] = {2,4};
    set_test_case(&test_cases[idx++], m1, 4, m2, 4, m3, 2);
    int n1[] = {1,2,2,1}, n2[] = {1,2,2,1}, n3[] = {1,2,2,1};
    set_test_case(&test_cases[idx++], n1, 4, n2, 4, n3, 4);
    int o1[] = {1,2,2,1}, o2[] = {}, o3[] = {};
    set_test_case(&test_cases[idx++], o1, 4, o2, 0, o3, 0);
    int p1[] = {}, p2[] = {1,2,2,1}, p3[] = {};
    set_test_case(&test_cases[idx++], p1, 0, p2, 4, p3, 0);
    int q1[] = {1,2,2,1}, q2[] = {2,1}, q3[] = {1,2};
    set_test_case(&test_cases[idx++], q1, 4, q2, 2, q3, 2);
    int r1[] = {1,2,2,1}, r2[] = {2,2,2,2}, r3[] = {2,2};
    set_test_case(&test_cases[idx++], r1, 4, r2, 4, r3, 2);
    int s1[] = {1,2,2,1}, s2[] = {1,1,1,1}, s3[] = {1,1};
    set_test_case(&test_cases[idx++], s1, 4, s2, 4, s3, 2);
    int t1[] = {1,2,2,1}, t2[] = {2,2,1,1}, t3[] = {1,2,2,1};
    set_test_case(&test_cases[idx++], t1, 4, t2, 4, t3, 4);

    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result[20];
        int resSize = intersect(test_cases[i].nums1, test_cases[i].nums1Size, test_cases[i].nums2, test_cases[i].nums2Size, result);
        if (arrays_equal(result, resSize, test_cases[i].expected, test_cases[i].expectedSize)) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed.\n", i + 1);
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
    measure_performance(test_intersect);
    return 0;
}
