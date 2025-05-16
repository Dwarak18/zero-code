import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]

    def list_to_random_linked(self, nodes, random_indices):
        node_objs = [Node(val) for val in nodes]
        for i in range(len(node_objs) - 1):
            node_objs[i].next = node_objs[i+1]
        for i, rand_idx in enumerate(random_indices):
            node_objs[i].random = node_objs[rand_idx] if rand_idx is not None else None
        return node_objs[0] if node_objs else None

    def random_linked_to_list(self, head):
        vals, randoms = [], []
        node_to_idx = {}
        curr = head
        idx = 0
        while curr:
            node_to_idx[curr] = idx
            vals.append(curr.val)
            curr = curr.next
            idx += 1
        curr = head
        while curr:
            if curr.random is not None:
                randoms.append(node_to_idx[curr.random])
            else:
                randoms.append(None)
            curr = curr.next
        return vals, randoms

    def test_copyRandomList(self):
        test_cases = [
            ([7,13,11,10,1], [None,0,4,2,0]),
            ([1,2], [1,0]),
            ([3,3,3], [None,0,None]),
            ([], []),
            ([1], [None]),
            ([1,2,3,4,5], [4,3,2,1,0]),
            ([1,2,3,4,5], [None,1,2,3,4]),
            ([1,2,3,4,5], [None,None,None,None,None]),
            ([1,2,3,4,5], [0,1,2,3,4]),
            ([1,2,3,4,5], [4,4,4,4,4]),
            ([1,2,3,4,5], [0,0,0,0,0]),
            ([1,2,3,4,5], [1,2,3,4,None]),
            ([1,2,3,4,5], [None,0,1,2,3]),
            ([1,2,3,4,5], [3,2,1,0,None]),
            ([1,2,3,4,5], [None,3,2,1,0]),
            ([1,2,3,4,5], [2,2,2,2,2]),
            ([1,2,3,4,5], [None,2,2,2,2]),
            ([1,2,3,4,5], [None,1,2,3,None]),
            ([1,2,3,4,5], [None,None,2,3,4]),
            ([1,2,3,4,5], [None,1,None,3,4]),
        ]
        passed = 0
        for idx, (vals, randoms) in enumerate(test_cases, 1):
            head = self.list_to_random_linked(vals, randoms)
            copied = self.copyRandomList(head)
            vals2, randoms2 = self.random_linked_to_list(copied)
            if vals2 == vals and randoms2 == randoms:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({vals}, {randoms}), expected=({vals}, {randoms}), got=({vals2}, {randoms2})")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_copyRandomList()

if __name__ == "__main__":
    run_tests()
