import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

    def list_to_linked(self, lst):
        dummy = ListNode()
        curr = dummy
        for v in lst:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def linked_to_list(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    def test_addTwoNumbers(self):
        test_cases = [
            ([2,4,3], [5,6,4], [7,0,8]),
            ([0], [0], [0]),
            ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
            ([1], [9,9,9], [0,0,0,1]),
            ([5], [5], [0,1]),
            ([1,8], [0], [1,8]),
            ([1,8], [9], [0,9]),
            ([1,8,9], [9,9,9], [0,8,9,1]),
            ([2,4,3], [5,6,4,9], [7,0,8,9]),
            ([2,4,3,9], [5,6,4], [7,0,8,9]),
            ([9,9,9], [1], [0,0,0,1]),
            ([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [5,6,4], [6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]),
            ([0], [7,3], [7,3]),
            ([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], [1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]),
            ([1,2,3], [4,5,6], [5,7,9]),
            ([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1]),
            ([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]),
            ([1,2,3,4,5,6,7,8,9,0], [9,8,7,6,5,4,3,2,1,0], [0,1,1,1,1,1,1,1,1,1,1]),
            ([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0], [9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0], [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
        ]
        passed = 0
        for idx, (l1, l2, expected) in enumerate(test_cases, 1):
            node1 = self.list_to_linked(l1)
            node2 = self.list_to_linked(l2)
            result = self.linked_to_list(self.addTwoNumbers(node1, node2))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({l1}, {l2}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_addTwoNumbers()

if __name__ == "__main__":
    run_tests()
