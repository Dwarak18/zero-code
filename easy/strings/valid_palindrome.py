import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]

    def test_is_palindrome(self):
        test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            ("", True),
            ("a", True),
            ("ab", False),
            ("aba", True),
            ("abba", True),
            ("abcba", True),
            ("abc", False),
            ("0P", False),
            ("Able was I ere I saw Elba", True),
            ("No lemon, no melon", True),
            ("Was it a car or a cat I saw?", True),
            ("Red roses run no risk, sir, on Nurse's order.", True),
            ("Eva, can I see bees in a cave?", True),
            ("Madam, in Eden, I'm Adam.", True),
            ("Never odd or even.", True),
            ("Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.", True),
            ("Not a palindrome", False),
            ("palindrome", False),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = self.isPalindrome(s)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_is_palindrome()

if __name__ == "__main__":
    run_tests()
