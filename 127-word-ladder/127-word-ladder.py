class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)  # !!!!!
        
        q = deque([beginWord])
        num = 0
        
        while q:
            size = len(q)
            num += 1
            
            for i in range(size):
                cur = q.popleft()
                if cur == endWord:
                    return num
                neighbors = []
                for j in range(len(cur)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        neigh = cur[:j] + c + cur[j+1:]
                        if neigh in wordList:
                            wordList.remove(neigh)  # !!!!!
                            neighbors.append(neigh)
                q.extend(neighbors)
        return 0