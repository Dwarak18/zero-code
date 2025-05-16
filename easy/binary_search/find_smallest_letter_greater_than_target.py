import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if target >= letters[-1]:
            return letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left % len(letters)]

    def test_next_greatest_letter(self):
        test_cases = [
            (["c","f","j"], "a", "c"),
            (["c","f","j"], "c", "f"),
            (["c","f","j"], "d", "f"),
            (["c","f","j"], "g", "j"),
            (["c","f","j"], "j", "c"),
            (["c","f","j"], "k", "c"),
            (["a","b"], "z", "a"),
            (["a","b"], "a", "b"),
            (["a","b"], "b", "a"),
            (["a","b","c"], "b", "c"),
            (["a","b","c"], "c", "a"),
            (["a","b","c"], "a", "b"),
            (["e","e","e","e","e","e","n","n","n"], "e", "n"),
            (["e","e","e","e","e","e","n","n","n"], "n", "e"),
            (["e","e","e","e","e","e","n","n","n"], "m", "n"),
            (["e","e","e","e","e","e","n","n","n"], "z", "e"),
            (["a"], "a", "a"),
            (["a"], "z", "a"),
            (["a","b","c","d"], "d", "a"),
            (["a","b","c","d"], "c", "d"),
        ]
        passed = 0
        for idx, (letters, target, expected) in enumerate(test_cases, 1):
            result = self.nextGreatestLetter(letters, target)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_next_greatest_letter()

if __name__ == "__main__":
    run_tests()
