import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return count == numCourses

    def test_canFinish(self):
        test_cases = [
            (2, [[1,0]], True),
            (2, [[1,0],[0,1]], False),
            (3, [[1,0],[2,1]], True),
            (3, [[1,0],[2,1],[0,2]], False),
            (4, [[1,0],[2,1],[3,2]], True),
            (4, [[1,0],[2,1],[3,2],[0,3]], False),
            (5, [[1,0],[2,1],[3,2],[4,3]], True),
            (5, [[1,0],[2,1],[3,2],[4,3],[0,4]], False),
            (6, [[1,0],[2,1],[3,2],[4,3],[5,4]], True),
            (6, [[1,0],[2,1],[3,2],[4,3],[5,4],[0,5]], False),
            (1, [], True),
            (2, [], True),
            (3, [], True),
            (4, [], True),
            (5, [], True),
            (6, [], True),
            (7, [], True),
            (8, [], True),
            (9, [], True),
            (10, [], True),
        ]
        passed = 0
        for idx, (numCourses, prerequisites, expected) in enumerate(test_cases, 1):
            result = self.canFinish(numCourses, prerequisites)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({numCourses}, {prerequisites}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_canFinish()

if __name__ == "__main__":
    run_tests()
