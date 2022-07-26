class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if width + w > 100:
                lines += 1
                width = w
                continue
            width += w
        return [lines, width]
                