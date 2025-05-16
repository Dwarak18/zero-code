import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]

    def test_minDistance(self):
        test_cases = [
            ("horse", "ros", 3),
            ("intention", "execution", 5),
            ("", "", 0),
            ("a", "", 1),
            ("", "a", 1),
            ("abc", "abc", 0),
            ("abc", "def", 3),
            ("kitten", "sitting", 3),
            ("flaw", "lawn", 2),
            ("gumbo", "gambol", 2),
            ("algorithm", "altruistic", 6),
            ("", "abcdef", 6),
            ("abcdef", "", 6),
            ("abcdef", "azced", 3),
            ("sunday", "saturday", 3),
            ("park", "spake", 3),
            ("", "a", 1),
            ("a", "", 1),
            ("", "", 0),
            ("a", "a", 0),
        ]
        passed = 0
        for idx, (word1, word2, expected) in enumerate(test_cases, 1):
            result = self.minDistance(word1, word2)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({word1}, {word2}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minDistance()

if __name__ == "__main__":
    run_tests()
