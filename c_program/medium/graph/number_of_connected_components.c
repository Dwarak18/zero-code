// number_of_connected_components.c
// C implementation of Number of Connected Components in an Undirected Graph (Union-Find)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_NODES 20
#define MAX_EDGES 40

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

int find(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

void union_set(int* parent, int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);
    if (rootX != rootY) parent[rootY] = rootX;
}

int countComponents(int n, int edges[][2], int edgeSize) {
    int parent[MAX_NODES];
    for (int i = 0; i < n; ++i) parent[i] = i;
    for (int i = 0; i < edgeSize; ++i) {
        union_set(parent, edges[i][0], edges[i][1]);
    }
    int count = 0;
    for (int i = 0; i < n; ++i) {
        if (find(parent, i) == i) count++;
    }
    return count;
}

typedef struct {
    int n;
    int edges[MAX_EDGES][2];
    int edgeSize;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int n, int edges[][2], int edgeSize, int expected) {
    tc->n = n;
    tc->edgeSize = edgeSize;
    for (int i = 0; i < edgeSize; ++i) {
        tc->edges[i][0] = edges[i][0];
        tc->edges[i][1] = edges[i][1];
    }
    tc->expected = expected;
}

void test_countComponents() {
    TestCase test_cases[20];
    int idx = 0;
    int a1[][2] = {{0,1},{1,2},{3,4}};
    set_test_case(&test_cases[idx++], 5, a1, 3, 2);
    int a2[][2] = {{0,1},{1,2},{2,3},{3,4}};
    set_test_case(&test_cases[idx++], 5, a2, 4, 1);
    set_test_case(&test_cases[idx++], 5, NULL, 0, 5);
    set_test_case(&test_cases[idx++], 1, NULL, 0, 1);
    int a5[][2] = {{1,0}};
    set_test_case(&test_cases[idx++], 2, a5, 1, 1);
    set_test_case(&test_cases[idx++], 2, NULL, 0, 2);
    int a7[][2] = {{0,1}};
    set_test_case(&test_cases[idx++], 3, a7, 1, 2);
    int a8[][2] = {{0,1},{1,2}};
    set_test_case(&test_cases[idx++], 3, a8, 2, 1);
    int a9[][2] = {{0,1},{2,3}};
    set_test_case(&test_cases[idx++], 4, a9, 2, 2);
    int a10[][2] = {{0,1},{1,2},{2,3}};
    set_test_case(&test_cases[idx++], 4, a10, 3, 1);
    int a11[][2] = {{0,1},{1,2},{3,4},{4,5}};
    set_test_case(&test_cases[idx++], 6, a11, 4, 2);
    int a12[][2] = {{0,1},{1,2},{2,3},{3,4},{4,5}};
    set_test_case(&test_cases[idx++], 6, a12, 5, 1);
    int a13[][2] = {{0,1},{1,2},{3,4},{5,6}};
    set_test_case(&test_cases[idx++], 7, a13, 4, 3);
    int a14[][2] = {{0,1},{1,2},{2,3},{3,4},{4,5},{5,6}};
    set_test_case(&test_cases[idx++], 7, a14, 6, 1);
    int a15[][2] = {{0,1},{1,2},{3,4},{5,6},{6,7}};
    set_test_case(&test_cases[idx++], 8, a15, 5, 3);
    int a16[][2] = {{0,1},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7}};
    set_test_case(&test_cases[idx++], 8, a16, 7, 1);
    int a17[][2] = {{0,1},{2,3},{4,5},{6,7},{8,9}};
    set_test_case(&test_cases[idx++], 10, a17, 5, 5);
    int a18[][2] = {{0,1},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,8},{8,9}};
    set_test_case(&test_cases[idx++], 10, a18, 9, 1);
    set_test_case(&test_cases[idx++], 10, NULL, 0, 10);
    int a20[][2] = {{0,1},{2,3},{4,5},{6,7},{8,9},{1,2},{3,4},{5,6},{7,8}};
    set_test_case(&test_cases[idx++], 10, a20, 9, 1);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = countComponents(test_cases[i].n, test_cases[i].edges, test_cases[i].edgeSize);
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
    measure_performance(test_countComponents);
    return 0;
}
