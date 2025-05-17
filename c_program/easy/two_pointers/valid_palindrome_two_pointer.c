// valid_palindrome_two_pointer.c
// C implementation of valid palindrome (two pointer) with test cases and performance measurement
#include <stdio.h>
#include <string.h>
#include <ctype.h>
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

int isPalindrome(const char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        if (tolower(s[left]) != tolower(s[right])) return 0;
        left++;
        right--;
    }
    return 1;
}

typedef struct {
    char input[200];
    int expected;
} TestCase;

void set_test_case(TestCase* tc, const char* input, int expected) {
    strncpy(tc->input, input, 199);
    tc->input[199] = '\0';
    tc->expected = expected;
}

void test_is_palindrome() {
    TestCase test_cases[20];
    int idx = 0;
    set_test_case(&test_cases[idx++], "A man, a plan, a canal: Panama", 1);
    set_test_case(&test_cases[idx++], "race a car", 0);
    set_test_case(&test_cases[idx++], "", 1);
    set_test_case(&test_cases[idx++], " ", 1);
    set_test_case(&test_cases[idx++], "0P", 0);
    set_test_case(&test_cases[idx++], "a", 1);
    set_test_case(&test_cases[idx++], "ab", 0);
    set_test_case(&test_cases[idx++], "aba", 1);
    set_test_case(&test_cases[idx++], "Able was I ere I saw Elba", 1);
    set_test_case(&test_cases[idx++], "No lemon, no melon", 1);
    set_test_case(&test_cases[idx++], "Was it a car or a cat I saw?", 1);
    set_test_case(&test_cases[idx++], "Red roses run no risk, sir, on Nurse's order.", 1);
    set_test_case(&test_cases[idx++], "Eva, can I see bees in a cave?", 1);
    set_test_case(&test_cases[idx++], "12321", 1);
    set_test_case(&test_cases[idx++], "1231", 0);
    set_test_case(&test_cases[idx++], ".,", 1);
    set_test_case(&test_cases[idx++], "Madam In Eden, I'm Adam", 1);
    set_test_case(&test_cases[idx++], "Never odd or even", 1);
    set_test_case(&test_cases[idx++], "palindrome", 0);
    set_test_case(&test_cases[idx++], "1a2", 0);

    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = isPalindrome(test_cases[i].input);
        if (result == test_cases[i].expected) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got %d, expected %d\n", i + 1, result, test_cases[i].expected);
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
    measure_performance(test_is_palindrome);
    return 0;
}
