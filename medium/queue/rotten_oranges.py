import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while queue:
            r, c, t = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh -= 1
                    queue.append((nr, nc, t+1))
                    time = t+1
        return time if fresh==0 else -1

    def test_orangesRotting(self):
        test_cases = [
            ([[2,1,1],[1,1,0],[0,1,1]], 4),
            ([[2,1,1],[0,1,1],[1,0,1]], -1),
            ([[0,2]], 0),
            ([[1,2]], 1),
            ([[2,2,2,1,1,1,0,0,0]], 3),
            ([[2,1,1],[1,1,1],[0,1,2]], 2),
            ([[1,1,1],[1,1,1],[1,1,1]], -1),
            ([[2,2,2],[2,2,2],[2,2,2]], 0),
            ([[0,0,0],[0,0,0],[0,0,0]], 0),
            ([[2,1,1],[1,1,0],[0,1,2]], 2),
            ([[2,1,1],[1,1,0],[0,1,1]], 4),
            ([[2,1,1],[0,1,1],[1,0,1]], -1),
            ([[0,2]], 0),
            ([[1,2]], 1),
            ([[2,2,2,1,1,1,0,0,0]], 3),
            ([[2,1,1],[1,1,1],[0,1,2]], 2),
            ([[1,1,1],[1,1,1],[1,1,1]], -1),
            ([[2,2,2],[2,2,2],[2,2,2]], 0),
            ([[0,0,0],[0,0,0],[0,0,0]], 0),
            ([[2,1,1],[1,1,0],[0,1,2]], 2),
        ]
        passed = 0
        for idx, (grid, expected) in enumerate(test_cases, 1):
            import copy
            result = self.orangesRotting(copy.deepcopy(grid))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={grid}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_orangesRotting()

if __name__ == "__main__":
    run_tests()
