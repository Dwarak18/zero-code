import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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

    def test_removeNthFromEnd(self):
        test_cases = [
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1], 1, []),
            ([1,2], 1, [1]),
            ([1,2], 2, [2]),
            ([1,2,3], 3, [2,3]),
            ([1,2,3], 2, [1,3]),
            ([1,2,3], 1, [1,2]),
            ([1,2,3,4,5], 5, [2,3,4,5]),
            ([1,2,3,4,5], 4, [1,3,4,5]),
            ([1,2,3,4,5], 3, [1,2,4,5]),
            ([1,2,3,4,5], 1, [1,2,3,4]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 2, [1,2,3,5]),
        ]
        passed = 0
        for idx, (lst, n, expected) in enumerate(test_cases, 1):
            head = self.list_to_linked(lst)
            result = self.linked_to_list(self.removeNthFromEnd(head, n))
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({lst}, {n}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_removeNthFromEnd()

if __name__ == "__main__":
    run_tests()
