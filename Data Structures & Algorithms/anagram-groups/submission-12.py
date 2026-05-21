class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        for string in strs:
            changed = False
            if len(final) != 0:
                for item in final:
                    if self.isAnagram(item[0], string):
                        item.append(string)
                        changed = True
            if not changed:
                final.append([string])
        return final
            


    def isAnagram(self, a: str, b: str) -> bool:
        if self.intoMap(a) == self.intoMap(b):
            return True
        else:
            return False
        
    def intoMap(self, word: str):
        freq = {}
        for c in word:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq
        
        