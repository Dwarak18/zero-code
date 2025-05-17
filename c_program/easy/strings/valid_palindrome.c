// filepath: d:\coding_challenge\c_program\easy\strings\valid_palindrome.c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
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

// Check if a string is a palindrome (alphanumeric, ignore case)
int isPalindrome(const char* s) {
    int n = strlen(s);
    int l = 0, r = n - 1;
    while (l < r) {
        while (l < r && !isalnum((unsigned char)s[l])) l++;
        while (l < r && !isalnum((unsigned char)s[r])) r--;
        if (l < r) {
            if (tolower((unsigned char)s[l]) != tolower((unsigned char)s[r])) return 0;
            l++;
            r--;
        }
    }
    return 1;
}

typedef struct {
    char s[200];
    int expected;
} TestCase;

void test_is_palindrome() {
    TestCase test_cases[] = {
        {"A man, a plan, a canal: Panama", 1},
        {"race a car", 0},
        {"", 1},
        {"a", 1},
        {"ab", 0},
        {"aba", 1},
        {"abba", 1},
        {"abcba", 1},
        {"abc", 0},
        {"0P", 0},
        {"Able was I ere I saw Elba", 1},
        {"No lemon, no melon", 1},
        {"Was it a car or a cat I saw?", 1},
        {"Red roses run no risk, sir, on Nurse's order.", 1},
        {"Eva, can I see bees in a cave?", 1},
        {"Madam, in Eden, I'm Adam.", 1},
        {"Never odd or even.", 1},
        {"Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.", 1},
        {"Not a palindrome", 0},
        {"palindrome", 0},
    };
    int num_cases = sizeof(test_cases) / sizeof(TestCase);
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        int result = isPalindrome(test_cases[i].s);
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
    measure_performance(test_is_palindrome);
    return 0;
}
