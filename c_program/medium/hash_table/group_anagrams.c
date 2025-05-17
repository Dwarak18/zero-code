// group_anagrams.c
// C implementation of Group Anagrams using hash table and sorting
// Includes test cases and performance measurement
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_STRS 16
#define MAX_LEN 16
#define MAX_GROUPS 16
#define HASH_SIZE 103

// Helper: sort a string in-place
void sort_str(char* s) {
    int len = strlen(s);
    for (int i = 0; i < len-1; ++i) {
        for (int j = i+1; j < len; ++j) {
            if (s[i] > s[j]) {
                char t = s[i]; s[i] = s[j]; s[j] = t;
            }
        }
    }
}

typedef struct Node {
    char str[MAX_LEN+1];
    struct Node* next;
} Node;

typedef struct {
    char key[MAX_LEN+1]; // sorted string
    Node* head;
} Group;

Group groups[MAX_GROUPS];
int group_count;

unsigned int hash(const char* s) {
    unsigned int h = 0;
    while (*s) h = h * 31 + (unsigned char)(*s++);
    return h % HASH_SIZE;
}

// Find group by key, or create new
Group* find_or_create_group(const char* key) {
    for (int i = 0; i < group_count; ++i) {
        if (strcmp(groups[i].key, key) == 0) return &groups[i];
    }
    if (group_count < MAX_GROUPS) {
        strcpy(groups[group_count].key, key);
        groups[group_count].head = NULL;
        return &groups[group_count++];
    }
    return NULL;
}

void clear_groups() {
    for (int i = 0; i < group_count; ++i) {
        Node* n = groups[i].head;
        while (n) {
            Node* tmp = n;
            n = n->next;
            free(tmp);
        }
        groups[i].head = NULL;
    }
    group_count = 0;
}

// Group anagrams, returns number of groups, fills groups[]
int groupAnagrams(char strs[][MAX_LEN+1], int n) {
    clear_groups();
    for (int i = 0; i < n; ++i) {
        char sorted[MAX_LEN+1];
        strcpy(sorted, strs[i]);
        sort_str(sorted);
        Group* g = find_or_create_group(sorted);
        if (g) {
            Node* node = (Node*)malloc(sizeof(Node));
            strcpy(node->str, strs[i]);
            node->next = g->head;
            g->head = node;
        }
    }
    return group_count;
}

// Helper: check if two groups are equal (order-insensitive)
int group_equal(Group* a, Group* b) {
    int ca = 0, cb = 0;
    Node* na = a->head, *nb = b->head;
    char arr_a[MAX_STRS][MAX_LEN+1], arr_b[MAX_STRS][MAX_LEN+1];
    while (na) { strcpy(arr_a[ca++], na->str); na = na->next; }
    while (nb) { strcpy(arr_b[cb++], nb->str); nb = nb->next; }
    if (ca != cb) return 0;
    // Sort arrays for comparison
    for (int i = 0; i < ca-1; ++i) for (int j = i+1; j < ca; ++j) {
        if (strcmp(arr_a[i], arr_a[j]) > 0) { char t[MAX_LEN+1]; strcpy(t, arr_a[i]); strcpy(arr_a[i], arr_a[j]); strcpy(arr_a[j], t); }
        if (strcmp(arr_b[i], arr_b[j]) > 0) { char t[MAX_LEN+1]; strcpy(t, arr_b[i]); strcpy(arr_b[i], arr_b[j]); strcpy(arr_b[j], t); }
    }
    for (int i = 0; i < ca; ++i) if (strcmp(arr_a[i], arr_b[i]) != 0) return 0;
    return 1;
}

typedef struct {
    char strs[MAX_STRS][MAX_LEN+1];
    int n;
    char expected[MAX_GROUPS][MAX_STRS][MAX_LEN+1];
    int expected_group_sizes[MAX_GROUPS];
    int expected_group_count;
} TestCase;

void set_test_case(TestCase* tc, char arr[][MAX_LEN+1], int n, char exp[][MAX_STRS][MAX_LEN+1], int* exp_sizes, int exp_count) {
    for (int i = 0; i < n; ++i) strcpy(tc->strs[i], arr[i]);
    tc->n = n;
    for (int i = 0; i < exp_count; ++i) {
        for (int j = 0; j < exp_sizes[i]; ++j) strcpy(tc->expected[i][j], exp[i][j]);
        tc->expected_group_sizes[i] = exp_sizes[i];
    }
    tc->expected_group_count = exp_count;
}

int group_set_equal(TestCase* tc) {
    // For each expected group, find a matching group in groups[]
    int matched[MAX_GROUPS] = {0};
    for (int i = 0; i < tc->expected_group_count; ++i) {
        Group temp;
        temp.head = NULL;
        for (int j = 0; j < tc->expected_group_sizes[i]; ++j) {
            Node* node = (Node*)malloc(sizeof(Node));
            strcpy(node->str, tc->expected[i][j]);
            node->next = temp.head;
            temp.head = node;
        }
        int found = 0;
        for (int k = 0; k < group_count; ++k) {
            if (!matched[k] && group_equal(&temp, &groups[k])) { matched[k] = 1; found = 1; break; }
        }
        Node* n = temp.head; while (n) { Node* t = n; n = n->next; free(t); }
        if (!found) return 0;
    }
    return 1;
}

void test_groupAnagrams() {
    TestCase tests[5];
    int idx = 0;
    // Test 1
    char arr1[6][MAX_LEN+1] = {"eat","tea","tan","ate","nat","bat"};
    char exp1[3][MAX_STRS][MAX_LEN+1] = {{"eat","tea","ate"},{"tan","nat"},{"bat"}};
    int exp1_sizes[3] = {3,2,1};
    set_test_case(&tests[idx++], arr1, 6, exp1, exp1_sizes, 3);
    // Test 2
    char arr2[1][MAX_LEN+1] = {""};
    char exp2[1][MAX_STRS][MAX_LEN+1] = {{""}};
    int exp2_sizes[1] = {1};
    set_test_case(&tests[idx++], arr2, 1, exp2, exp2_sizes, 1);
    // Test 3
    char arr3[1][MAX_LEN+1] = {"a"};
    char exp3[1][MAX_STRS][MAX_LEN+1] = {{"a"}};
    int exp3_sizes[1] = {1};
    set_test_case(&tests[idx++], arr3, 1, exp3, exp3_sizes, 1);
    // Test 4
    char arr4[6][MAX_LEN+1] = {"abc","bca","cab","bac","acb","cba"};
    char exp4[1][MAX_STRS][MAX_LEN+1] = {{"abc","bca","cab","bac","acb","cba"}};
    int exp4_sizes[1] = {6};
    set_test_case(&tests[idx++], arr4, 6, exp4, exp4_sizes, 1);
    // Test 5
    char arr5[3][MAX_LEN+1] = {"abc","def","ghi"};
    char exp5[3][MAX_STRS][MAX_LEN+1] = {{"abc"},{"def"},{"ghi"}};
    int exp5_sizes[3] = {1,1,1};
    set_test_case(&tests[idx++], arr5, 3, exp5, exp5_sizes, 3);
    int passed = 0;
    for (int i = 0; i < idx; ++i) {
        groupAnagrams(tests[i].strs, tests[i].n);
        if (group_count == tests[i].expected_group_count && group_set_equal(&tests[i])) {
            printf("Test case %d passed.\n", i+1);
            passed++;
        } else {
            printf("Test case %d failed.\n", i+1);
        }
    }
    printf("Passed %d/%d test cases.\n", passed, idx);
}

void measure_performance() {
    char arr[MAX_STRS][MAX_LEN+1];
    for (int i = 0; i < MAX_STRS; ++i) {
        for (int j = 0; j < MAX_LEN; ++j) arr[i][j] = 'a' + (j % 3);
        arr[i][MAX_LEN] = '\0';
    }
    clock_t start = clock();
    for (int i = 0; i < 10000; ++i) {
        groupAnagrams(arr, MAX_STRS);
    }
    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Performance test: 10000 runs on %d strings took %.3f seconds.\n", MAX_STRS, elapsed);
}

int main() {
    test_groupAnagrams();
    measure_performance();
    return 0;
}
