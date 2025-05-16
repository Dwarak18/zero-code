import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        # Build graph
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        # Topological sort
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return "".join(res) if len(res) == len(indegree) else ""

    def test_alienOrder(self):
        test_cases = [
            (["wrt","wrf","er","ett","rftt"], "wertf"),
            (["z","x"], "zx"),
            (["z","x","z"], ""),
            (["abc","ab"], ""),
            (["ab","adc"], "bacd"),
            (["abc","bcd","cde"], "abcde"),
            (["a","b","c"], "abc"),
            (["ba","bc","ac","cab"], "bac"),
            (["a","b","ca","cc"], "abc"),
            (["abc","abx","abf","abq"], "abxcfq"),
            (["x","z","x"], ""),
            (["za","zb","ca","cb"], "zacb"),
            (["abc","ab"], ""),
            (["abc","bca","cab"], "abc"),
            (["a","b","c","d"], "abcd"),
            (["wrt","wrf","er","ett","rftt"], "wertf"),
            (["z","x","z"], ""),
            (["abc","ab"], ""),
            (["ab","adc"], "bacd"),
            (["abc","bcd","cde"], "abcde"),
        ]
        passed = 0
        for idx, (words, expected) in enumerate(test_cases, 1):
            result = self.alienOrder(words)
            # Accept any valid topological order for ambiguous cases
            if expected == "":
                if result == "":
                    print(f"Test case {idx} passed.")
                    passed += 1
                else:
                    print(f"Test case {idx} failed: input={words}, expected='', got={result}")
            else:
                # Check if result is a valid topological order
                def is_valid(order, words):
                    pos = {c: i for i, c in enumerate(order)}
                    for i in range(len(words)-1):
                        w1, w2 = words[i], words[i+1]
                        for a, b in zip(w1, w2):
                            if a != b:
                                if pos[a] > pos[b]:
                                    return False
                                break
                        else:
                            if len(w1) > len(w2):
                                return False
                    return set(order) == set(''.join(words))
                if is_valid(result, words):
                    print(f"Test case {idx} passed.")
                    passed += 1
                else:
                    print(f"Test case {idx} failed: input={words}, expected valid order, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_alienOrder()

if __name__ == "__main__":
    run_tests()
