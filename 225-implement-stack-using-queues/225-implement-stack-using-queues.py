class MyStack:

    def __init__(self):
        self.queue = deque()
        self.top_el = None

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_el = x

    def pop(self) -> int:
        for i in range(len(self.queue)-1):
            if i == len(self.queue)-2:
                self.top_el = self.queue.popleft()
                self.push(self.top_el)
            else: self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.top_el

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()