import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def restoreIpAddresses(self, s):
        res = []
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            for l in range(1, 4):
                if start + l > len(s):
                    break
                part = s[start:start+l]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(start + l, path + [part])
        backtrack(0, [])
        return res

    def test_restoreIpAddresses(self):
        test_cases = [
            ("25525511135", sorted(["255.255.11.135","255.255.111.35"])),
            ("0000", ["0.0.0.0"]),
            ("1111", ["1.1.1.1"]),
            ("010010", sorted(["0.10.0.10","0.100.1.0"])),
            ("101023", sorted(["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])),
            ("123456789", []),
            ("255255255255", ["255.255.255.255"]),
            ("255255255256", []),
            ("", []),
            ("1", []),
            ("12", []),
            ("123", []),
            ("1234", ["1.2.3.4"]),
            ("000256", []),
            ("256256256256", []),
            ("192168011", sorted(["19.216.80.11","192.16.80.11","192.168.0.11"])),
            ("10101010", sorted(["1.0.10.1010","1.0.101.010","1.0.101.10","1.0.1010.10","1.0.1010.1","1.0.10.10","1.0.10.1","1.0.1.10","1.0.1.1","1.0.1.1010","1.0.1.101","1.0.1.10","1.0.1.1","1.0.1.1010","1.0.1.101","1.0.1.10","1.0.1.1"])),
            ("11111111", sorted(["1.1.1.111","1.1.11.11","1.1.111.1","1.11.1.11","1.11.11.1","1.111.1.1","11.1.1.11","11.1.11.1","11.11.1.1","111.1.1.1"])),
            ("22222222", sorted(["2.2.2.222","2.2.22.22","2.2.222.2","2.22.2.22","2.22.22.2","2.222.2.2","22.2.2.22","22.2.22.2","22.22.2.2","222.2.2.2"])),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = sorted(self.restoreIpAddresses(s))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={s}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_restoreIpAddresses()

if __name__ == "__main__":
    run_tests()
