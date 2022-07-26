class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w
        return [lines, width]
                