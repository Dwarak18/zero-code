import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    def list_to_linked(self, lst, pos):
        dummy = ListNode()
        curr = dummy
        nodes = []
        for v in lst:
            node = ListNode(v)
            nodes.append(node)
            curr.next = node
            curr = curr.next
        if pos != -1 and nodes:
            curr.next = nodes[pos]
        return dummy.next

    def test_detectCycle(self):
        test_cases = [
            ([3,2,0,-4], 1, 2),
            ([1,2], 0, 1),
            ([1], -1, None),
            ([1,2,3,4,5], 2, 3),
            ([1,2,3,4,5], -1, None),
            ([1,2], -1, None),
            ([1], 0, 1),
            ([1,2,3], 1, 2),
            ([1,2,3], 2, 3),
            ([1,2,3], -1, None),
            ([1,2,3,4,5,6,7,8,9,10], 5, 6),
            ([1,2,3,4,5,6,7,8,9,10], -1, None),
            ([1,2,3,4,5,6,7,8,9,10], 0, 1),
            ([1,2,3,4,5,6,7,8,9,10], 9, 10),
            ([1,2,3,4,5,6,7,8,9,10], 8, 9),
            ([1,2,3,4,5,6,7,8,9,10], 7, 8),
            ([1,2,3,4,5,6,7,8,9,10], 6, 7),
            ([1,2,3,4,5,6,7,8,9,10], 4, 5),
            ([1,2,3,4,5,6,7,8,9,10], 3, 4),
        ]
        passed = 0
        for idx, (lst, pos, expected) in enumerate(test_cases, 1):
            head = self.list_to_linked(lst, pos)
            result = self.detectCycle(head)
            result_val = result.val if result else None
            if result_val == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({lst}, {pos}), expected={expected}, got={result_val}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_detectCycle()

if __name__ == "__main__":
    run_tests()
