class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:       
        def distance(p):
            [x, y] = p
            return x**2 + y**2
        
        def partition(l, r):
            p = randint(l, r)
            d = distance(points[p])
            points[r], points[p] = points[p], points[r]
            bound = l
            for i in range(l, r):
                if distance(points[i]) <= d:
                    points[bound], points[i] = points[i], points[bound]
                    bound += 1
            points[bound], points[r] = points[r], points[bound]
            return bound
        
        l, r = 0, len(points)-1
        while l <= r:
            mid = partition(l, r)
            if mid+1 == k:
                return points[:mid+1]
            elif mid+1 < k:
                l = mid+1
            else:
                r = mid-1