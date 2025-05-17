// pacific_atlantic_water_flow.c
// C implementation of Pacific Atlantic Water Flow with test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_M 10
#define MAX_N 10
#define MAX_RES 100

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

// BFS for Pacific/Atlantic reachability
void bfs(int m, int n, int heights[MAX_M][MAX_N], int* starts, int startsSize, int visited[MAX_M][MAX_N]) {
    int queue[MAX_M*MAX_N][2], front = 0, rear = 0;
    for (int i = 0; i < startsSize; ++i) {
        int x = starts[2*i], y = starts[2*i+1];
        queue[rear][0] = x; queue[rear][1] = y; rear++;
        visited[x][y] = 1;
    }
    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    while (front < rear) {
        int x = queue[front][0], y = queue[front][1]; front++;
        for (int d = 0; d < 4; ++d) {
            int nx = x + dirs[d][0], ny = y + dirs[d][1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && heights[nx][ny] >= heights[x][y]) {
                visited[nx][ny] = 1;
                queue[rear][0] = nx; queue[rear][1] = ny; rear++;
            }
        }
    }
}

int pacificAtlantic(int m, int n, int heights[MAX_M][MAX_N], int res[MAX_RES][2]) {
    int pacific[MAX_M][MAX_N] = {0}, atlantic[MAX_M][MAX_N] = {0};
    int pacific_starts[MAX_M*2 + MAX_N*2], pacific_size = 0;
    int atlantic_starts[MAX_M*2 + MAX_N*2], atlantic_size = 0;
    for (int j = 0; j < n; ++j) { pacific[pacific_size][0] = 0; pacific[pacific_size][1] = j; pacific_size++; }
    for (int i = 0; i < m; ++i) { pacific[pacific_size][0] = i; pacific[pacific_size][1] = 0; pacific_size++; }
    for (int j = 0; j < n; ++j) { atlantic[atlantic_size][0] = m-1; atlantic[atlantic_size][1] = j; atlantic_size++; }
    for (int i = 0; i < m; ++i) { atlantic[atlantic_size][0] = i; atlantic[atlantic_size][1] = n-1; atlantic_size++; }
    int pacific_flat[MAX_M*2 + MAX_N*2], atlantic_flat[MAX_M*2 + MAX_N*2];
    for (int i = 0; i < pacific_size; ++i) { pacific_flat[2*i] = pacific[i][0]; pacific_flat[2*i+1] = pacific[i][1]; }
    for (int i = 0; i < atlantic_size; ++i) { atlantic_flat[2*i] = atlantic[i][0]; atlantic_flat[2*i+1] = atlantic[i][1]; }
    int pacific_visited[MAX_M][MAX_N] = {0}, atlantic_visited[MAX_M][MAX_N] = {0};
    bfs(m, n, heights, pacific_flat, pacific_size, pacific_visited);
    bfs(m, n, heights, atlantic_flat, atlantic_size, atlantic_visited);
    int count = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (pacific_visited[i][j] && atlantic_visited[i][j]) {
                res[count][0] = i; res[count][1] = j; count++;
            }
        }
    }
    return count;
}

int compare_results(int a[MAX_RES][2], int n, int b[MAX_RES][2], int m) {
    if (n != m) return 0;
    int matched[MAX_RES] = {0};
    for (int i = 0; i < n; ++i) {
        int found = 0;
        for (int j = 0; j < m; ++j) {
            if (!matched[j] && a[i][0] == b[j][0] && a[i][1] == b[j][1]) { matched[j] = 1; found = 1; break; }
        }
        if (!found) return 0;
    }
    return 1;
}

typedef struct {
    int m, n;
    int heights[MAX_M][MAX_N];
    int expected[MAX_RES][2];
    int expectedSize;
} TestCase;

void set_test_case(TestCase* tc, int m, int n, int heights[MAX_M][MAX_N], int expected[MAX_RES][2], int expectedSize) {
    tc->m = m; tc->n = n;
    for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) tc->heights[i][j] = heights[i][j];
    for (int i = 0; i < expectedSize; ++i) { tc->expected[i][0] = expected[i][0]; tc->expected[i][1] = expected[i][1]; }
    tc->expectedSize = expectedSize;
}

void test_pacificAtlantic() {
    TestCase test_cases[5];
    int idx = 0;
    int h1[MAX_M][MAX_N] = {
        {1,2,2,3,5},
        {3,2,3,4,4},
        {2,4,5,3,1},
        {6,7,1,4,5},
        {5,1,1,2,4}
    };
    int e1[MAX_RES][2] = {{0,4},{1,3},{1,4},{2,2},{3,0},{3,1},{4,0}};
    set_test_case(&test_cases[idx++], 5, 5, h1, e1, 7);
    int h2[MAX_M][MAX_N] = {{2,1},{1,2}};
    int e2[MAX_RES][2] = {{0,0},{0,1},{1,0},{1,1}};
    set_test_case(&test_cases[idx++], 2, 2, h2, e2, 4);
    int h3[MAX_M][MAX_N] = {{1}};
    int e3[MAX_RES][2] = {{0,0}};
    set_test_case(&test_cases[idx++], 1, 1, h3, e3, 1);
    int h4[MAX_M][MAX_N] = {{1,2,3},{8,9,4},{7,6,5}};
    int e4[MAX_RES][2] = {{0,2},{1,1},{2,0},{2,1},{2,2}};
    set_test_case(&test_cases[idx++], 3, 3, h4, e4, 5);
    int h5[MAX_M][MAX_N] = {{10,10,10},{10,1,10},{10,10,10}};
    int e5[MAX_RES][2] = {{0,0},{0,1},{0,2},{1,0},{1,2},{2,0},{2,1},{2,2}};
    set_test_case(&test_cases[idx++], 3, 3, h5, e5, 8);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int res[MAX_RES][2];
        int resSize = pacificAtlantic(test_cases[i].m, test_cases[i].n, test_cases[i].heights, res);
        if (compare_results(res, resSize, test_cases[i].expected, test_cases[i].expectedSize)) {
            printf("Test case %d passed.\n", i+1);
            passed++;
        } else {
            printf("Test case %d failed.\n", i+1);
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
    measure_performance(test_pacificAtlantic);
    return 0;
}
