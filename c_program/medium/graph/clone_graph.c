// clone_graph.c
// C implementation of clone graph (undirected, with neighbors list)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>
#include <time.h>

#define MAX_NODES 100

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

typedef struct Node {
    int val;
    int num_neighbors;
    struct Node** neighbors;
} Node;

Node* create_node(int val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->val = val;
    node->num_neighbors = 0;
    node->neighbors = NULL;
    return node;
}

// Helper: queue for BFS
typedef struct {
    Node* data[MAX_NODES];
    int front, rear;
} Queue;

void queue_init(Queue* q) { q->front = q->rear = 0; }
int queue_empty(Queue* q) { return q->front == q->rear; }
void queue_push(Queue* q, Node* n) { q->data[q->rear++] = n; }
Node* queue_pop(Queue* q) { return q->data[q->front++]; }

// Hash map for node pointer mapping (simple array for small graphs)
typedef struct { Node* old_node; Node* new_node; } NodeMap;

Node* cloneGraph(Node* node) {
    if (!node) return NULL;
    NodeMap map[MAX_NODES];
    int map_size = 0;
    Queue q; queue_init(&q);
    queue_push(&q, node);
    Node* new_root = create_node(node->val);
    map[map_size++] = (NodeMap){node, new_root};
    while (!queue_empty(&q)) {
        Node* curr = queue_pop(&q);
        Node* curr_clone = NULL;
        for (int i = 0; i < map_size; ++i) if (map[i].old_node == curr) curr_clone = map[i].new_node;
        curr_clone->num_neighbors = curr->num_neighbors;
        curr_clone->neighbors = (Node**)malloc(sizeof(Node*) * curr->num_neighbors);
        for (int i = 0; i < curr->num_neighbors; ++i) {
            Node* neigh = curr->neighbors[i];
            Node* neigh_clone = NULL;
            int found = 0;
            for (int j = 0; j < map_size; ++j) {
                if (map[j].old_node == neigh) { neigh_clone = map[j].new_node; found = 1; break; }
            }
            if (!found) {
                neigh_clone = create_node(neigh->val);
                map[map_size++] = (NodeMap){neigh, neigh_clone};
                queue_push(&q, neigh);
            }
            curr_clone->neighbors[i] = neigh_clone;
        }
    }
    return new_root;
}

// Build graph from adjacency list (adj[i] is array of neighbor indices for node i+1)
Node* build_graph(int adj[][MAX_NODES], int adj_sizes[], int n) {
    Node* nodes[MAX_NODES];
    for (int i = 0; i < n; ++i) nodes[i] = create_node(i+1);
    for (int i = 0; i < n; ++i) {
        nodes[i]->num_neighbors = adj_sizes[i];
        nodes[i]->neighbors = (Node**)malloc(sizeof(Node*) * adj_sizes[i]);
        for (int j = 0; j < adj_sizes[i]; ++j) {
            int idx = adj[i][j] - 1;
            nodes[i]->neighbors[j] = nodes[idx];
        }
    }
    return nodes[0];
}

// Compare two graphs by BFS traversal (structure and values)
int compare_graphs(Node* a, Node* b, int n) {
    if (!a && !b) return 1;
    if (!a || !b) return 0;
    int visited_a[MAX_NODES] = {0}, visited_b[MAX_NODES] = {0};
    Queue qa, qb; queue_init(&qa); queue_init(&qb);
    queue_push(&qa, a); queue_push(&qb, b);
    while (!queue_empty(&qa) && !queue_empty(&qb)) {
        Node* na = queue_pop(&qa);
        Node* nb = queue_pop(&qb);
        if (na->val != nb->val || na->num_neighbors != nb->num_neighbors) return 0;
        visited_a[na->val-1] = 1; visited_b[nb->val-1] = 1;
        for (int i = 0; i < na->num_neighbors; ++i) {
            if (!visited_a[na->neighbors[i]->val-1]) queue_push(&qa, na->neighbors[i]);
            if (!visited_b[nb->neighbors[i]->val-1]) queue_push(&qb, nb->neighbors[i]);
        }
    }
    return 1;
}

void free_graph(Node* node, int n) {
    if (!node) return;
    int visited[MAX_NODES] = {0};
    Queue q; queue_init(&q); queue_push(&q, node);
    while (!queue_empty(&q)) {
        Node* curr = queue_pop(&q);
        if (visited[curr->val-1]) continue;
        visited[curr->val-1] = 1;
        for (int i = 0; i < curr->num_neighbors; ++i) {
            if (!visited[curr->neighbors[i]->val-1]) queue_push(&q, curr->neighbors[i]);
        }
        free(curr->neighbors);
        free(curr);
    }
}

void test_clone_graph() {
    // Test cases: adjacency lists
    int adj1[4][MAX_NODES] = {{2,4},{1,3},{2,4},{1,3}}; int sz1[4] = {2,2,2,2};
    int adj2[1][MAX_NODES] = {{}}; int sz2[1] = {0};
    int adj3[2][MAX_NODES] = {{2},{1}}; int sz3[2] = {1,1};
    int adj4[3][MAX_NODES] = {{2,3},{1,3},{1,2}}; int sz4[3] = {2,2,2};
    int* adjs[] = {(int*)adj1, (int*)adj2, (int*)adj3, (int*)adj4};
    int* szs[] = {sz1, sz2, sz3, sz4};
    int ns[] = {4,1,2,3};
    int num_cases = 4;
    int passed = 0;
    for (int i = 0; i < num_cases; ++i) {
        Node* g = build_graph((int(*)[MAX_NODES])adjs[i], szs[i], ns[i]);
        Node* clone = cloneGraph(g);
        if (compare_graphs(g, clone, ns[i])) {
            printf("Test case %d passed.\n", i+1);
            passed++;
        } else {
            printf("Test case %d failed.\n", i+1);
        }
        free_graph(g, ns[i]);
        free_graph(clone, ns[i]);
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
    measure_performance(test_clone_graph);
    return 0;
}
