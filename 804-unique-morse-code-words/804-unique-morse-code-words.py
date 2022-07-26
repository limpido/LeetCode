class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1: return 1
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformation = set()
        for word in words:
            concat = ''
            for ch in word:
                concat += code[ord(ch)-97]
            transformation.add(concat)
        return len(transformation)