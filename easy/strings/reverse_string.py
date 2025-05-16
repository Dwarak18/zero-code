import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def test_reverse_string(self):
        test_cases = [
            (list("hello"), list("olleh")),
            (list("Hannah"), list("hannaH")),
            (list("a"), list("a")),
            (list("ab"), list("ba")),
            (list("racecar"), list("racecar")),
            (list(""), list("")),
            (list("abcde"), list("edcba")),
            (list("12345"), list("54321")),
            (list("!@#$%"), list("%$#@!")),
            (list("madam"), list("madam")),
            (list("level"), list("level")),
            (list("noon"), list("noon")),
            (list("python"), list("nohtyp")),
            (list("openai"), list("ianepo")),
            (list("race"), list("ecar")),
            (list("data"), list("atad")),
            (list("science"), list("ecneics")),
            (list("reverse"), list("esrever")),
            (list("string"), list("gnirts")),
            (list("test"), list("tset")),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            arr = s[:]
            self.reverseString(arr)
            if arr == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {arr}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_reverse_string()

if __name__ == "__main__":
    run_tests()
