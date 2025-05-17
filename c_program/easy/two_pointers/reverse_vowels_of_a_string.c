// reverse_vowels_of_a_string.c
// C implementation of reverse vowels of a string with test cases and performance measurement
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

int is_vowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

void reverseVowels(char* s, char* out) {
    int n = strlen(s);
    strcpy(out, s);
    int left = 0, right = n - 1;
    while (left < right) {
        while (left < right && !is_vowel(out[left])) left++;
        while (left < right && !is_vowel(out[right])) right--;
        if (left < right) {
            char tmp = out[left];
            out[left] = out[right];
            out[right] = tmp;
            left++;
            right--;
        }
    }
}

typedef struct {
    char input[100];
    char expected[100];
} TestCase;

void set_test_case(TestCase* tc, const char* input, const char* expected) {
    strncpy(tc->input, input, 99);
    tc->input[99] = '\0';
    strncpy(tc->expected, expected, 99);
    tc->expected[99] = '\0';
}

void test_reverse_vowels() {
    TestCase test_cases[20];
    int idx = 0;
    set_test_case(&test_cases[idx++], "hello", "holle");
    set_test_case(&test_cases[idx++], "leetcode", "leotcede");
    set_test_case(&test_cases[idx++], "aA", "Aa");
    set_test_case(&test_cases[idx++], "aeiou", "uoiea");
    set_test_case(&test_cases[idx++], "", "");
    set_test_case(&test_cases[idx++], "bcd", "bcd");
    set_test_case(&test_cases[idx++], "race car", "rece car");
    set_test_case(&test_cases[idx++], "Euston saw I was not Sue.", ".euston saw I was not SuE");
    set_test_case(&test_cases[idx++], "Why?", "Why?");
    set_test_case(&test_cases[idx++], "AEIOUaeiou", "uoieaUOIEA");
    set_test_case(&test_cases[idx++], "The quick brown fox", "Tho qeick brown fux");
    set_test_case(&test_cases[idx++], "Programming", "Prigrammong");
    set_test_case(&test_cases[idx++], "Vowel", "Vowel");
    set_test_case(&test_cases[idx++], "Swap vowels", "Swep vawols");
    set_test_case(&test_cases[idx++], "Try again", "Try again");
    set_test_case(&test_cases[idx++], "A man a plan a canal Panama", "a man a plan a canal PanamA");
    set_test_case(&test_cases[idx++], "Palindrome", "Polindrame");
    set_test_case(&test_cases[idx++], "aei", "iea");
    set_test_case(&test_cases[idx++], "uoiea", "aeiou");
    set_test_case(&test_cases[idx++], "xyz", "xyz");

    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        char result[100];
        reverseVowels(test_cases[i].input, result);
        if (strcmp(result, test_cases[i].expected) == 0) {
            printf("Test case %d passed.\n", i + 1);
            passed++;
        } else {
            printf("Test case %d failed: got '%s', expected '%s'\n", i + 1, result, test_cases[i].expected);
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
    measure_performance(test_reverse_vowels);
    return 0;
}
