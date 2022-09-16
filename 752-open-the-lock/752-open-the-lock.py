class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        depth = -1
        q = deque(['0000'])
        visited = set(deadends)
        
        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                cur = q.popleft()
                if cur in visited:
                    continue
                if cur == target:
                    return depth
                else:
                    nbs = self.neighbors(cur)
                    q.extend(nbs)
                    visited.add(cur)
            
        return -1
    
    def neighbors(self, cur):
        res = []
        for i in range(len(cur)):
            num = int(cur[i])
            res.append(cur[:i] + str((num-1) % 10) + cur[i+1:])
            res.append(cur[:i] + str((num+1) % 10) + cur[i+1:])
        return res
        