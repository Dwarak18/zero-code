import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []

    def test_findOrder(self):
        test_cases = [
            (2, [[1,0]], [0,1]),
            (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),
            (1, [], [0]),
            (2, [[1,0],[0,1]], []),
            (3, [[1,0],[1,2],[0,1]], []),
            (3, [[1,0]], [0,1,2]),
            (3, [[1,0],[2,1]], [0,1,2]),
            (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),
            (5, [[1,0],[2,0],[3,1],[3,2],[4,3]], [0,1,2,3,4]),
            (6, [[1,0],[2,1],[3,2],[4,3],[5,4]], [0,1,2,3,4,5]),
            (3, [[1,0],[2,0]], [0,1,2]),
            (3, [[1,0],[2,1]], [0,1,2]),
            (3, [[1,0],[2,1],[0,2]], []),
            (4, [[1,0],[2,1],[3,2],[0,3]], []),
            (4, [[1,0],[2,1],[3,2]], [0,1,2,3]),
            (5, [[1,0],[2,1],[3,2],[4,3]], [0,1,2,3,4]),
            (5, [[1,0],[2,1],[3,2],[4,3],[0,4]], []),
            (6, [[1,0],[2,1],[3,2],[4,3],[5,4]], [0,1,2,3,4,5]),
            (6, [[1,0],[2,1],[3,2],[4,3],[5,4],[0,5]], []),
            (7, [[1,0],[2,1],[3,2],[4,3],[5,4],[6,5]], [0,1,2,3,4,5,6]),
        ]
        passed = 0
        for idx, (numCourses, prerequisites, expected) in enumerate(test_cases, 1):
            result = self.findOrder(numCourses, prerequisites)
            # Accept any valid topological order for ambiguous cases
            def is_valid(order, numCourses, prerequisites):
                if len(order) != numCourses:
                    return False
                pos = {c: i for i, c in enumerate(order)}
                for dest, src in prerequisites:
                    if pos[src] > pos[dest]:
                        return False
                return True
            if expected == []:
                if result == []:
                    print(f"Test case {idx} passed.")
                    passed += 1
                else:
                    print(f"Test case {idx} failed: input=({numCourses}, {prerequisites}), expected=[], got={result}")
            else:
                if is_valid(result, numCourses, prerequisites):
                    print(f"Test case {idx} passed.")
                    passed += 1
                else:
                    print(f"Test case {idx} failed: input=({numCourses}, {prerequisites}), expected valid order, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findOrder()

if __name__ == "__main__":
    run_tests()
