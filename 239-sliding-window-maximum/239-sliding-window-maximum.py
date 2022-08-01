class MyQueue:
    def __init__(self):
        self.queue = deque()
    
    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()
    
    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)
        
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MyQueue()
        res = []
        
        for i in range(k):
            q.push(nums[i])
        res.append(q.front())
        for i in range(k, len(nums)):
            q.pop(nums[i-k])
            q.push(nums[i])
            res.append(q.front())
        return res
            
