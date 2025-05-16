import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        old_to_new = {}
        queue = deque([node])
        old_to_new[node] = Node(node.val)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]

    def build_graph(self, adj):
        if not adj:
            return None
        nodes = [Node(i+1) for i in range(len(adj))]
        for i, neighbors in enumerate(adj):
            nodes[i].neighbors = [nodes[j-1] for j in neighbors]
        return nodes[0]

    def graph_to_adj(self, node):
        if not node:
            return []
        adj = []
        visited = {}
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited[curr] = len(adj)
            adj.append([n.val for n in curr.neighbors])
            for n in curr.neighbors:
                if n not in visited:
                    queue.append(n)
        # Reorder adj by node value
        result = [None] * len(adj)
        for n, idx in visited.items():
            result[n.val-1] = [x for x in n.neighbors and [y.val for y in n.neighbors] or []]
        return result

    def test_cloneGraph(self):
        test_cases = [
            ([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]]),
            ([[]], [[]]),
            ([], []),
            ([[2],[1]], [[2],[1]]),
            ([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]),
            ([[2],[1,3],[2]], [[2],[1,3],[2]]),
            ([[2,3],[1,3],[1,2]], [[2,3],[1,3],[1,2]]),
            ([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]),
            ([[2],[1,3],[2]], [[2],[1,3],[2]]),
            ([[2,3],[1,3],[1,2]], [[2,3],[1,3],[1,2]]),
            ([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]),
            ([[2],[1,3],[2]], [[2],[1,3],[2]]),
            ([[2,3],[1,3],[1,2]], [[2,3],[1,3],[1,2]]),
            ([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]),
            ([[2],[1,3],[2]], [[2],[1,3],[2]]),
            ([[2,3],[1,3],[1,2]], [[2,3],[1,3],[1,2]]),
            ([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]),
            ([[2],[1,3],[2]], [[2],[1,3],[2]]),
            ([[2,3],[1,3],[1,2]], [[2,3],[1,3],[1,2]]),
        ]
        passed = 0
        for idx, (adj, expected) in enumerate(test_cases, 1):
            node = self.build_graph(adj)
            cloned = self.cloneGraph(node)
            result = self.graph_to_adj(cloned)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={adj}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_cloneGraph()

if __name__ == "__main__":
    run_tests()
