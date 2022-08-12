class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] == prev[0] or cur[0] < prev[1]:  # overlap
                count += 1
                if cur[1] < prev[1]:
                    prev = cur
            elif cur[0] >= prev[1]:   # no overlap
                prev = cur
        return count