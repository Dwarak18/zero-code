import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def bfs(starts, visited):
            queue = deque(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and heights[nx][ny] >= heights[x][y]:
                        visited.add((nx,ny))
                        queue.append((nx,ny))
        pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atlantic_starts = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)
        return sorted(list(pacific & atlantic))

    def test_pacificAtlantic(self):
        test_cases = [
            (
                [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
                sorted([(0,4),(1,3),(1,4),(2,2),(3,0),(3,1),(4,0)])
            ),
            (
                [[2,1],[1,2]],
                sorted([(0,0),(0,1),(1,0),(1,1)])
            ),
            (
                [[1]],
                sorted([(0,0)])
            ),
            (
                [[1,2,3],[8,9,4],[7,6,5]],
                sorted([(0,2),(1,1),(2,0),(2,1),(2,2)])
            ),
            (
                [[10,10,10],[10,1,10],[10,10,10]],
                sorted([(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)])
            ),
            (
                [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]],
                sorted([(0,4),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(4,1),(4,0),(3,0),(2,0),(1,0),(0,0),(0,1),(0,2),(0,3)])
            ),
            (
                [[1,2,3],[4,5,6],[7,8,9]],
                sorted([(0,2),(1,2),(2,0),(2,1),(2,2)])
            ),
            (
                [[1,1],[1,1]],
                sorted([(0,0),(0,1),(1,0),(1,1)])
            ),
            (
                [[1,2],[4,3]],
                sorted([(0,1),(1,0),(1,1)])
            ),
            (
                [[1,2,3],[8,9,4],[7,6,5]],
                sorted([(0,2),(1,1),(2,0),(2,1),(2,2)])
            ),
            (
                [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
                sorted([(0,4),(1,3),(1,4),(2,2),(3,0),(3,1),(4,0)])
            ),
            (
                [[2,1],[1,2]],
                sorted([(0,0),(0,1),(1,0),(1,1)])
            ),
            (
                [[1]],
                sorted([(0,0)])
            ),
            (
                [[1,2,3],[8,9,4],[7,6,5]],
                sorted([(0,2),(1,1),(2,0),(2,1),(2,2)])
            ),
            (
                [[10,10,10],[10,1,10],[10,10,10]],
                sorted([(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)])
            ),
            (
                [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]],
                sorted([(0,4),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(4,1),(4,0),(3,0),(2,0),(1,0),(0,0),(0,1),(0,2),(0,3)])
            ),
            (
                [[1,2,3],[4,5,6],[7,8,9]],
                sorted([(0,2),(1,2),(2,0),(2,1),(2,2)])
            ),
            (
                [[1,1],[1,1]],
                sorted([(0,0),(0,1),(1,0),(1,1)])
            ),
            (
                [[1,2],[4,3]],
                sorted([(0,1),(1,0),(1,1)])
            ),
        ]
        passed = 0
        for idx, (heights, expected) in enumerate(test_cases, 1):
            result = sorted(self.pacificAtlantic(heights))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={heights}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_pacificAtlantic()

if __name__ == "__main__":
    run_tests()
