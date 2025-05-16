import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head
        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        # Merge two halves
        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        return head

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

    def test_reorderList(self):
        test_cases = [
            ([1,2,3,4], [1,4,2,3]),
            ([1,2,3,4,5], [1,5,2,4,3]),
            ([1], [1]),
            ([1,2], [1,2]),
            ([1,2,3], [1,3,2]),
            ([1,2,3,4,5,6], [1,6,2,5,3,4]),
            ([1,2,3,4,5,6,7], [1,7,2,6,3,5,4]),
            ([1,2,3,4,5,6,7,8], [1,8,2,7,3,6,4,5]),
            ([1,2,3,4,5,6,7,8,9], [1,9,2,8,3,7,4,6,5]),
            ([1,2,3,4,5,6,7,8,9,10], [1,10,2,9,3,8,4,7,5,6]),
            ([1,2,3,4,5,6,7,8,9,10,11], [1,11,2,10,3,9,4,8,5,7,6]),
            ([1,2,3,4,5,6,7,8,9,10,11,12], [1,12,2,11,3,10,4,9,5,8,6,7]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13], [1,13,2,12,3,11,4,10,5,9,6,8,7]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [1,14,2,13,3,12,4,11,5,10,6,9,7,8]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,15,2,14,3,13,4,12,5,11,6,10,7,9,8]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,16,2,15,3,14,4,13,5,12,6,11,7,10,8,9]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], [1,17,2,16,3,15,4,14,5,13,6,12,7,11,8,10,9]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], [1,18,2,17,3,16,4,15,5,14,6,13,7,12,8,11,9,10]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], [1,19,2,18,3,17,4,16,5,15,6,14,7,13,8,12,9,11,10]),
        ]
        passed = 0
        for idx, (lst, expected) in enumerate(test_cases, 1):
            head = self.list_to_linked(lst)
            self.reorderList(head)
            result = self.linked_to_list(head)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={lst}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_reorderList()

if __name__ == "__main__":
    run_tests()
