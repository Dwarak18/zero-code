import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, org, seqs):
        if not org or not seqs:
            return False
        graph = defaultdict(set)
        indegree = defaultdict(int)
        nodes = set()
        for seq in seqs:
            for num in seq:
                nodes.add(num)
        for seq in seqs:
            for i in range(1, len(seq)):
                if seq[i] not in graph[seq[i-1]]:
                    graph[seq[i-1]].add(seq[i])
                    indegree[seq[i]] += 1
                if seq[i-1] not in indegree:
                    indegree[seq[i-1]] = 0
        if set(org) != nodes:
            return False
        queue = deque([x for x in org if indegree[x] == 0])
        res = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res == org

    def test_sequenceReconstruction(self):
        test_cases = [
            ([1,2,3], [[1,2],[1,3]], False),
            ([1,2,3], [[1,2]], False),
            ([1,2,3], [[1,2],[1,3],[2,3]], True),
            ([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]], True),
            ([1], [[1]], True),
            ([1], [[]], False),
            ([1,2,3], [[1,2],[2,3],[1,3]], True),
            ([1,2,3], [[1,2],[2,3],[1,3],[3,2]], False),
            ([1,2,3], [[1,2],[2,3],[3,1]], False),
            ([1,2,3], [[1,2],[2,3],[3,4]], False),
            ([1,2,3], [[1,2],[2,3],[1,3],[3,2]], False),
            ([1,2,3,4], [[1,2],[2,3],[3,4]], True),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[2,4]], True),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[4,2]], False),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[4,1]], False),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[1,3]], True),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[1,4]], True),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[2,1]], False),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[3,2]], False),
            ([1,2,3,4], [[1,2],[2,3],[3,4],[4,3]], False),
        ]
        passed = 0
        for idx, (org, seqs, expected) in enumerate(test_cases, 1):
            result = self.sequenceReconstruction(org, seqs)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({org}, {seqs}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_sequenceReconstruction()

if __name__ == "__main__":
    run_tests()
