import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)
        for s in strings:
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i-1])) % 26
                key.append(diff)
            groups[tuple(key)].append(s)
        return list(groups.values())

    def test_groupStrings(self):
        test_cases = [
            (["abc","bcd","acef","xyz","az","ba","a","z"], [["abc","bcd","xyz"],["acef"],["az","ba"],["a","z"]]),
            (["a"], [["a"]]),
            (["ab","bc","cd","de","ef","fg","gh","hi","ij","jk","kl","lm","mn","no","op","pq","qr","rs","st","tu","uv","vw","wx","xy","yz","za"], [["ab","bc","cd","de","ef","fg","gh","hi","ij","jk","kl","lm","mn","no","op","pq","qr","rs","st","tu","uv","vw","wx","xy","yz","za"]]),
            (["abc","def","ghi","jkl","mno","pqr","stu","vwx","yz"], [["abc"],["def"],["ghi"],["jkl"],["mno"],["pqr"],["stu"],["vwx"],["yz"]]),
            (["az","ba","a","z"], [["az","ba"],["a","z"]]),
            (["abc","bcd","cde","def","efg","fgh","ghi","hij","ijk","jkl","klm","lmn","mno","nop","opq","pqr","qrs","rst","stu","tuv","uvw","vwx","wxy","xyz"], [["abc","bcd","cde","def","efg","fgh","ghi","hij","ijk","jkl","klm","lmn","mno","nop","opq","pqr","qrs","rst","stu","tuv","uvw","vwx","wxy","xyz"]]),
            (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], [["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"],["m"],["n"],["o"],["p"],["q"],["r"],["s"],["t"],["u"],["v"],["w"],["x"],["y"],["z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef"], [["abc","bcd","xyz"],["acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz"], [["abc","bcd","xyz","xyz"],["acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc"], [["abc","bcd","xyz","xyz","abc"],["acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd"], [["abc","bcd","xyz","xyz","abc","bcd"],["acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd","acef"], [["abc","bcd","xyz","xyz","abc","bcd"],["acef","acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd","acef","xyz"], [["abc","bcd","xyz","xyz","abc","bcd","xyz"],["acef","acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd","acef","xyz","abc"], [["abc","bcd","xyz","xyz","abc","bcd","xyz","abc"],["acef","acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd","acef","xyz","abc","bcd"], [["abc","bcd","xyz","xyz","abc","bcd","xyz","abc","bcd"],["acef","acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd","acef","xyz","abc","bcd","acef"], [["abc","bcd","xyz","xyz","abc","bcd","xyz","abc","bcd"],["acef","acef","acef","acef"],["az","ba"],["a","z"]]),
            (["abc","bcd","acef","xyz","az","ba","a","z","acef","xyz","abc","bcd","acef","xyz","abc","bcd","acef","xyz"], [["abc","bcd","xyz","xyz","abc","bcd","xyz","abc","bcd","xyz"],["acef","acef","acef","acef"],["az","ba"],["a","z"]]),
        ]
        passed = 0
        for idx, (strings, expected) in enumerate(test_cases, 1):
            result = self.groupStrings(strings)
            # Order-insensitive comparison
            result_set = set(frozenset(g) for g in result)
            expected_set = set(frozenset(g) for g in expected)
            if result_set == expected_set:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={strings}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_groupStrings()

if __name__ == "__main__":
    run_tests()
