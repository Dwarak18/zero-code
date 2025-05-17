// course_schedule.c
// C implementation of Course Schedule (canFinish) with test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_COURSES 20
#define MAX_PREREQS 40

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

// BFS Topological Sort
int canFinish(int numCourses, int prereqs[][2], int prereqSize) {
    int graph[MAX_COURSES][MAX_COURSES] = {0};
    int indegree[MAX_COURSES] = {0};
    for (int i = 0; i < prereqSize; ++i) {
        int a = prereqs[i][0], b = prereqs[i][1];
        graph[b][a] = 1;
        indegree[a]++;
    }
    int queue[MAX_COURSES], front = 0, rear = 0;
    for (int i = 0; i < numCourses; ++i) {
        if (indegree[i] == 0) queue[rear++] = i;
    }
    int count = 0;
    while (front < rear) {
        int node = queue[front++];
        count++;
        for (int nei = 0; nei < numCourses; ++nei) {
            if (graph[node][nei]) {
                indegree[nei]--;
                if (indegree[nei] == 0) queue[rear++] = nei;
            }
        }
    }
    return count == numCourses;
}

typedef struct {
    int numCourses;
    int prereqs[MAX_PREREQS][2];
    int prereqSize;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, int numCourses, int prereqs[][2], int prereqSize, int expected) {
    tc->numCourses = numCourses;
    tc->prereqSize = prereqSize;
    for (int i = 0; i < prereqSize; ++i) {
        tc->prereqs[i][0] = prereqs[i][0];
        tc->prereqs[i][1] = prereqs[i][1];
    }
    tc->expected = expected;
}

void test_canFinish() {
    TestCase test_cases[20];
    int idx = 0;
    int a1[][2] = {{1,0}};
    set_test_case(&test_cases[idx++], 2, a1, 1, 1);
    int a2[][2] = {{1,0},{0,1}};
    set_test_case(&test_cases[idx++], 2, a2, 2, 0);
    int a3[][2] = {{1,0},{2,1}};
    set_test_case(&test_cases[idx++], 3, a3, 2, 1);
    int a4[][2] = {{1,0},{2,1},{0,2}};
    set_test_case(&test_cases[idx++], 3, a4, 3, 0);
    int a5[][2] = {{1,0},{2,1},{3,2}};
    set_test_case(&test_cases[idx++], 4, a5, 3, 1);
    int a6[][2] = {{1,0},{2,1},{3,2},{0,3}};
    set_test_case(&test_cases[idx++], 4, a6, 4, 0);
    int a7[][2] = {{1,0},{2,1},{3,2},{4,3}};
    set_test_case(&test_cases[idx++], 5, a7, 4, 1);
    int a8[][2] = {{1,0},{2,1},{3,2},{4,3},{0,4}};
    set_test_case(&test_cases[idx++], 5, a8, 5, 0);
    int a9[][2] = {{1,0},{2,1},{3,2},{4,3},{5,4}};
    set_test_case(&test_cases[idx++], 6, a9, 5, 1);
    int a10[][2] = {{1,0},{2,1},{3,2},{4,3},{5,4},{0,5}};
    set_test_case(&test_cases[idx++], 6, a10, 6, 0);
    set_test_case(&test_cases[idx++], 1, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 2, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 3, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 4, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 5, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 6, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 7, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 8, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 9, NULL, 0, 1);
    set_test_case(&test_cases[idx++], 10, NULL, 0, 1);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = canFinish(test_cases[i].numCourses, test_cases[i].prereqs, test_cases[i].prereqSize);
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
    measure_performance(test_canFinish);
    return 0;
}
