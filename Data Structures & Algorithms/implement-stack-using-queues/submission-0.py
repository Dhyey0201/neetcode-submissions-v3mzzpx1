class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft()) # This will insert removed 
            #element back to the queue but in the right side as we've 
            #already declared the length to be the till second last element, 
            #thus the value till second last element will be removed and 
            #insert back to the queue again.
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()