import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            val = matrix[i][j]
            res = 1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>val:
                    res = max(res, 1+dfs(ni, nj))
            memo[i][j] = res
            return res
        return max(dfs(i, j) for i in range(m) for j in range(n))

    def test_longestIncreasingPath(self):
        test_cases = [
            ([[9,9,4],[6,6,8],[2,1,1]], 4),
            ([[3,4,5],[3,2,6],[2,2,1]], 4),
            ([[1]], 1),
            ([[1,2]], 2),
            ([[2,1]], 2),
            ([[1],[2]], 2),
            ([[2],[1]], 2),
            ([[1,2,3,4,5]], 5),
            ([[5,4,3,2,1]], 5),
            ([[1,2,3],[6,5,4],[7,8,9]], 9),
            ([[7,8,9],[6,5,4],[1,2,3]], 9),
            ([[1,2,3],[4,5,6],[7,8,9]], 5),
            ([[9,8,7],[6,5,4],[3,2,1]], 5),
            ([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]], 16),
            ([[1,2,3,4,5,6,7,8,9,10]], 10),
            ([[10,9,8,7,6,5,4,3,2,1]], 10),
            ([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]], 20),
            ([[20,19,18,17,16,15,14,13,12,11],[10,9,8,7,6,5,4,3,2,1]], 20),
            ([[1,2,3,4,5,6,7,8,9,10],[20,19,18,17,16,15,14,13,12,11]], 11),
        ]
        passed = 0
        for idx, (matrix, expected) in enumerate(test_cases, 1):
            result = self.longestIncreasingPath(matrix)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={matrix}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_longestIncreasingPath()

if __name__ == "__main__":
    run_tests()
