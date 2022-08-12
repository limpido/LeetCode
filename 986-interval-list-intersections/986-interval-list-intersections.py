class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            if first[1] < second[0]:
                i += 1
            elif second[1] < first[0]:
                j += 1
            else:
                merged = [max(first[0], second[0]), min(first[1], second[1])]
                res.append(merged)
                if first[1] < second[1]:
                    i += 1
                else:
                    j += 1
        return res
                