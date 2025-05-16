import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
import heapq

class Solution:
    def prim(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))
        visited = [False] * n
        min_heap = [(0, 0)]
        total_cost = 0
        mst_edges = []
        while min_heap and len(mst_edges) < n - 1:
            w, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += w
            if w != 0:
                mst_edges.append((prev, u, w))
            for weight, v in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))
                    prev = u
        return mst_edges

    def test_prim(self):
        test_cases = [
            (4, [(0,1,1),(1,2,2),(0,2,3),(2,3,4)], 3),
            (3, [(0,1,1),(1,2,2),(0,2,3)], 2),
            (2, [(0,1,1)], 1),
            (5, [(0,1,1),(1,2,2),(2,3,3),(3,4,4),(4,0,5)], 4),
            (4, [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)], 3),
            (3, [(0,1,1),(1,2,1),(0,2,2)], 2),
            (4, [(0,1,1),(1,2,1),(2,3,1),(3,0,1)], 3),
            (3, [(0,1,2),(1,2,2),(0,2,1)], 2),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4)], 3),
            (5, [(0,1,1),(1,2,2),(2,3,3),(3,4,4),(4,0,5),(1,3,1)], 4),
            (2, [(0,1,2)], 1),
            (3, [(0,1,1),(1,2,1),(0,2,1)], 2),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5)], 3),
            (3, [(0,1,1),(1,2,2),(0,2,3),(2,0,1)], 2),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5),(1,3,1)], 4),
            (2, [(0,1,1),(1,0,1)], 1),
            (3, [(0,1,1),(1,2,2),(0,2,3),(2,0,1)], 2),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5),(1,3,1),(2,0,1)], 4),
            (3, [(0,1,1),(1,2,2),(0,2,3),(2,0,1),(1,0,1)], 2),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5),(1,3,1),(2,0,1),(3,1,1)], 4),
        ]
        passed = 0
        for idx, (n, edges, expected_edges) in enumerate(test_cases, 1):
            result = self.prim(n, edges)
            if len(result) == expected_edges:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({n}, {edges}), expected edges={expected_edges}, got={len(result)}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_prim()

if __name__ == "__main__":
    run_tests()
