from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    """
    내 풀이
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        length = len(arr)
        mid = length // 2

        if length%2 == 0:
            if arr == arr[::-1]:
                return True
            else:
                return False
        else:
            if arr[:mid] == arr[mid+1:][::-1]:
                return True
            else:
                return False
            

class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []

        if not head:
            return True
        
        node = head
        # value를 리스트에 넣기
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
    

import collections

class Solution3:
    """
    리스트 대신 데크 사용하기
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()

        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.poplef() != q.pop():
                return False
        return True
    

class Solution4:
    """
    fast pointer, slow pointer 2가지 사용해 풀이
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        rev = None

        # slow pointer로 중간 지점 찾기
        # slow 역순 연결 리스트 rev 만들기
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev