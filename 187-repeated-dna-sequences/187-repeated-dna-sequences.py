class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        all_seq = set()
        for i in range(len(s)-9):
            if s[i:i+10] in all_seq:
                res.add(s[i:i+10])
            else:
                all_seq.add(s[i:i+10])
                
        return list(res)