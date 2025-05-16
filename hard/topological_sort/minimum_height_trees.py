import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

    def test_findMinHeightTrees(self):
        test_cases = [
            (4, [[1,0],[1,2],[1,3]], [1]),
            (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3,4]),
            (1, [], [0]),
            (2, [[0,1]], [0,1]),
            (3, [[0,1],[1,2]], [1]),
            (5, [[0,1],[0,2],[0,3],[3,4]], [0,3]),
            (7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]], [1,2]),
            (8, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7]], [1,2,3]),
            (9, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]], [2,3,4,5]),
            (10, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9]], [4,5]),
            (11, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10]], [5]),
            (12, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11]], [5,6]),
            (13, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12]], [6]),
            (14, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13]], [6,7]),
            (15, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14]], [7]),
            (16, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15]], [7,8]),
            (17, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15],[14,16]], [8]),
            (18, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15],[14,16],[15,17]], [8,9]),
            (19, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15],[14,16],[15,17],[16,18]], [9]),
        ]
        passed = 0
        for idx, (n, edges, expected) in enumerate(test_cases, 1):
            result = sorted(self.findMinHeightTrees(n, edges))
            if result == sorted(expected):
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({n}, {edges}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findMinHeightTrees()

if __name__ == "__main__":
    run_tests()
