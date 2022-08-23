class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:       
        distance = []
        hashmap = {}
        for p in points:
            [x, y] = p
            d = x ** 2 + y ** 2
            distance.append(d)
            if d in hashmap:
                hashmap[d].append(p)
            else:
                hashmap[d] = [p]
            
        distance.sort()
        res = []
        for i in range(k):
            if i > 0 and distance[i] == distance[i-1]:
                continue
            res.extend(hashmap[distance[i]])
        return res
        