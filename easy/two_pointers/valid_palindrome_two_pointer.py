import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from measure_performance import measure_performance

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    @measure_performance
    def test_isPalindrome(self):
        test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            ("", True),
            (" ", True),
            ("0P", False),
            ("a", True),
            ("ab", False),
            ("aba", True),
            ("Able was I ere I saw Elba", True),
            ("No lemon, no melon", True),
            ("Was it a car or a cat I saw?", True),
            ("Red roses run no risk, sir, on Nurse's order.", True),
            ("Eva, can I see bees in a cave?", True),
            ("12321", True),
            ("1231", False),
            (".,", True),
            ("Madam In Eden, I'm Adam", True),
            ("Never odd or even", True),
            ("palindrome", False),
            ("1a2", False),
        ]
        passed = 0
        for i, (inp, expected) in enumerate(test_cases):
            result = self.isPalindrome(inp)
            if result == expected:
                print(f"Test case {i+1} passed.")
                passed += 1
            else:
                print(f"Test case {i+1} failed: input={inp}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

if __name__ == "__main__":
    Solution().test_isPalindrome()
