import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def findWords(self, board, words):
        res = set()
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word
        m, n = len(board), len(board[0]) if board else 0
        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return
            nxt = node[c]
            word = nxt.pop('#', False)
            if word:
                res.add(word)
            board[i][j] = None
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n and board[ni][nj] is not None:
                    dfs(ni, nj, nxt)
            board[i][j] = c
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return list(res)

    def test_findWords(self):
        test_cases = [
            ([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oath","pea","eat","rain"], sorted(["oath","eat"])),
            ([['a','b'],['c','d']], ["abcb"], []),
            ([['a']], ["a"], ["a"]),
            ([['a','b'],['c','d']], ["abcd"], []),
            ([['a','b'],['c','d']], ["acdb"], []),
            ([['a','b'],['c','d']], ["ab","cd","ad","bc"], sorted(["ab","cd"])),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abc","cfi","beh","defi","gh"], sorted(["abc","cfi","beh","gh"])),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["aei","ceg","adg","gda"], sorted(["aei","ceg","adg"])),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["a","b","c","d","e","f","g","h","i"], sorted(["a","b","c","d","e","f","g","h","i"])),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcdefghi"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghi"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedg"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedgh"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghi"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghij"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghijk"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghijkl"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghijklm"], []),
            ([['a','b','c'],['d','e','f'],['g','h','i']], ["abcfedghijklmn"], []),
        ]
        passed = 0
        for idx, (board, words, expected) in enumerate(test_cases, 1):
            result = sorted(self.findWords([row[:] for row in board], words))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({board}, {words}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findWords()

if __name__ == "__main__":
    run_tests()
