class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = {}
        for i in range(len(edges)):
            if edges[i] not in score:
                score[edges[i]] = i
            else:
                score[edges[i]] += i
        
        max_score = 0
        res = len(edges)
        for key, val in score.items():
            if val > max_score:
                res = key
                max_score = val
            elif val == max_score:
                res = min(res, key)
                
        return res