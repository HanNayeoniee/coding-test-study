# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 출력할 Linked List 초기화
        tail = dummy  # 첫번째 노드를 가리키는 노드 필요

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        # list1만 남은 경우
        if list1:
            dummy.next = list1
        # list2만 남은 경우
        elif list2:
            dummy.next = list2
                 
        return tail.next