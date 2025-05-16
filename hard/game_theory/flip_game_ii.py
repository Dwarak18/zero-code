import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def canWin(self, s):
        memo = {}
        def can_win(state):
            if state in memo:
                return memo[state]
            for i in range(len(state)-1):
                if state[i:i+2] == '++':
                    next_state = state[:i] + '--' + state[i+2:]
                    if not can_win(next_state):
                        memo[state] = True
                        return True
            memo[state] = False
            return False
        return can_win(s)

    def test_canWin(self):
        test_cases = [
            ("++++", True),
            ("+", False),
            ("++", True),
            ("+++", False),
            ("+++++", True),
            ("++++++", True),
            ("+++++++", False),
            ("++++++++", True),
            ("+++++++++", True),
            ("++++++++++", True),
            ("+++++++++++", False),
            ("++++++++++++", True),
            ("+++++++++++++", True),
            ("++++++++++++++", True),
            ("+++++++++++++++", False),
            ("", False),
            ("-", False),
            ("--", False),
            ("-+", False),
            ("+-", False),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = self.canWin(s)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={s}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_canWin()

if __name__ == "__main__":
    run_tests()
