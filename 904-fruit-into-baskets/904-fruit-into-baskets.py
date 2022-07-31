class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        res = 0
        tree = {fruits[0]: 0}
        while right < len(fruits):
            if fruits[right-1] != fruits[right]:
                tree[fruits[right]] = right
            if len(tree) > 2:
                left = tree[fruits[right-1]]
                for key in tree.keys():
                    if key != fruits[right] and key != fruits[right-1]:
                        del tree[key]
                        break
            if len(tree) <= 2:
                res = max(res, right-left+1)
            right += 1
        return res