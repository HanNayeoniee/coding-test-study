"""
큐로 스택 구현하기
LeetCode #225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    # 큐는 가장 첫번째 요소부터 삭제할 수 있음
    # 가장 첫 번째 요소부터 N-1 까지 삭제, N번째 값을 반환
    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]
    
    def empty(self):
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



"""
큐로 스택 구현하기
LeetCode #232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, x) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0
     

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()