// word_ladder.c
// C implementation of Word Ladder (BFS) with test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_WORDS 32
#define MAX_WORD_LEN 8
#define MAX_QUEUE 128

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

int is_one_letter_diff(const char* a, const char* b) {
    int diff = 0;
    for (int i = 0; a[i] && b[i]; ++i) {
        if (a[i] != b[i]) diff++;
        if (diff > 1) return 0;
    }
    return diff == 1;
}

int ladderLength(const char* beginWord, const char* endWord, char wordList[MAX_WORDS][MAX_WORD_LEN], int wordListSize) {
    int used[MAX_WORDS] = {0};
    int queue[MAX_QUEUE];
    int dist[MAX_QUEUE];
    char words[MAX_QUEUE][MAX_WORD_LEN];
    int front = 0, rear = 0;
    strcpy(words[rear], beginWord);
    dist[rear] = 1;
    queue[rear++] = -1; // -1 means beginWord
    while (front < rear) {
        int idx = queue[front];
        int d = dist[front];
        char* curr = (idx == -1) ? (char*)beginWord : wordList[idx];
        front++;
        if (strcmp(curr, endWord) == 0) return d;
        for (int i = 0; i < wordListSize; ++i) {
            if (!used[i] && is_one_letter_diff(curr, wordList[i])) {
                used[i] = 1;
                strcpy(words[rear], wordList[i]);
                dist[rear] = d + 1;
                queue[rear++] = i;
            }
        }
    }
    return 0;
}

typedef struct {
    char beginWord[MAX_WORD_LEN];
    char endWord[MAX_WORD_LEN];
    char wordList[MAX_WORDS][MAX_WORD_LEN];
    int wordListSize;
    int expected;
} TestCase;

void set_test_case(TestCase* tc, const char* beginWord, const char* endWord, char wordList[MAX_WORDS][MAX_WORD_LEN], int wordListSize, int expected) {
    strncpy(tc->beginWord, beginWord, MAX_WORD_LEN-1); tc->beginWord[MAX_WORD_LEN-1] = '\0';
    strncpy(tc->endWord, endWord, MAX_WORD_LEN-1); tc->endWord[MAX_WORD_LEN-1] = '\0';
    for (int i = 0; i < wordListSize; ++i) {
        strncpy(tc->wordList[i], wordList[i], MAX_WORD_LEN-1); tc->wordList[i][MAX_WORD_LEN-1] = '\0';
    }
    tc->wordListSize = wordListSize;
    tc->expected = expected;
}

void test_ladderLength() {
    TestCase test_cases[20];
    int idx = 0;
    char wl1[MAX_WORDS][MAX_WORD_LEN] = {"hot","dot","dog","lot","log","cog"};
    set_test_case(&test_cases[idx++], "hit", "cog", wl1, 6, 5);
    char wl2[MAX_WORDS][MAX_WORD_LEN] = {"hot","dot","dog","lot","log"};
    set_test_case(&test_cases[idx++], "hit", "cog", wl2, 5, 0);
    char wl3[MAX_WORDS][MAX_WORD_LEN] = {"a","b","c"};
    set_test_case(&test_cases[idx++], "a", "c", wl3, 3, 2);
    char wl4[MAX_WORDS][MAX_WORD_LEN] = {"ted","tex","red","tax","tad","den","rex","pee"};
    set_test_case(&test_cases[idx++], "red", "tax", wl4, 8, 4);
    char wl5[MAX_WORDS][MAX_WORD_LEN] = {"most","fist","lost","cost","fish"};
    set_test_case(&test_cases[idx++], "lost", "cost", wl5, 5, 2);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        int result = ladderLength(test_cases[i].beginWord, test_cases[i].endWord, test_cases[i].wordList, test_cases[i].wordListSize);
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
    measure_performance(test_ladderLength);
    return 0;
}
