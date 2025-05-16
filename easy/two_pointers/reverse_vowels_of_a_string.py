import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from measure_performance import measure_performance

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)

    @measure_performance
    def test_reverseVowels(self):
        test_cases = [
            ("hello", "holle"),
            ("leetcode", "leotcede"),
            ("aA", "Aa"),
            ("aeiou", "uoiea"),
            ("", ""),
            ("bcd", "bcd"),
            ("race car", "rece car"),
            ("Euston saw I was not Sue.", ".euston saw I was not SuE"),
            ("Why?", "Why?"),
            ("AEIOUaeiou", "uoieaUOIEA"),
            ("The quick brown fox", "Tho qeick brown fux"),
            ("Programming", "Prigrammong"),
            ("Vowel", "Vowel"),
            ("Swap vowels", "Swep vawols"),
            ("Try again", "Try again"),
            ("A man a plan a canal Panama", "a man a plan a canal PanamA"),
            ("Palindrome", "Polindrame"),
            ("aei", "iea"),
            ("uoiea", "aeiou"),
            ("xyz", "xyz"),
        ]
        passed = 0
        for i, (inp, expected) in enumerate(test_cases):
            result = self.reverseVowels(inp)
            if result == expected:
                print(f"Test case {i+1} passed.")
                passed += 1
            else:
                print(f"Test case {i+1} failed: input={inp}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

if __name__ == "__main__":
    Solution().test_reverseVowels()
