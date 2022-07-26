class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1: return 1
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformation = set()
        for word in words:
            concat = []
            for ch in word:
                concat.append(code[ord(ch) - ord('a')])
            transformation.add(''.join(concat))
        return len(transformation)