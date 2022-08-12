class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ''' Method 1: same as merge interval, O(nlogn)
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:  # no overlap
                merged.append(interval)
            else:   # overlap
                merged[-1][0] = min(merged[-1][0], interval[0])
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        '''
        
        '''Method 2: O(n)'''
        res = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        res.append(newInterval)
        return res