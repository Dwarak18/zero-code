
#include <stdio.h>








#include <windows.h>
#include <psapi.h>
#include <time.h>

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

// maxProfit function
int maxProfit(int* prices, int pricesSize) {
    int max_profit = 0;
    int min_price = 2147483647; // INT_MAX
    for (int i = 0; i < pricesSize; ++i) {
        if (prices[i] < min_price) {
            min_price = prices[i];
        } else if (prices[i] - min_price > max_profit) {
            max_profit = prices[i] - min_price;
        }
    }
    return max_profit;
}

typedef struct {
    int prices[20];
    int pricesSize;
    int expected;
} TestCase;

void test_max_profit() {
    TestCase test_cases[] = {
        {{7,1,5,3,6,4}, 6, 5},
        {{7,6,4,3,1}, 5, 0},
        {{1,2,3,4,5}, 5, 4},
        {{2,4,1}, 3, 2},
        {{3,3,5,0,0,3,1,4}, 8, 4},
        {{1,2}, 2, 1},
        {{2,1,2,1,0,1,2}, 7, 2},
        {{1,2,4,2,5,7,2,4,9,0}, 10, 8},
        {{2,1,4}, 3, 3},
        {{1,2,3,4,5,6,7,8,9,10}, 10, 9},
        {{10,9,8,7,6,5,4,3,2,1}, 10, 0},
        {{1,1,1,1,1,1,1,1,1,1}, 10, 0},
        {{1,2,1,2,1,2,1,2,1,2}, 10, 1},
        {{2,4,1,7}, 4, 6},
        {{1,2,3,2,1,0,1,2,3,4}, 10, 4},
        {{3,2,6,5,0,3}, 6, 4},
        {{1,7,5,3,6,4,8,2,5}, 9, 7},
        {{2,1,2,0,1}, 5, 1},
        {{1,2,3,4,5,0,1,2,3,4}, 10, 4},
        {{1,2,3,4,5,6,7,8,9,10,1}, 11, 9},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = maxProfit(test_cases[i].prices, test_cases[i].pricesSize);
        if (result == test_cases[i].expected) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got %d, expected %d\n", i + 1, result, test_cases[i].expected);
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
    measure_performance(test_max_profit);
    return 0;
}
