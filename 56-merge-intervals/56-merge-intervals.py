class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[1] >= cur[0]:
                left = min(prev[0], cur[0])
                right = max(prev[1], cur[1])
                prev = [left, right]
            else:
                res.append(prev)
                prev = cur
        res.append(prev)
        return res