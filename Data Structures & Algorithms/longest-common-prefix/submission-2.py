class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        pointer = 0

        res = ""

        while pointer < len(strs[0]):
            current_char = strs[0][pointer]
            for s in strs:
                if pointer == len(s) or s[pointer] != current_char:
                    return res
            res += current_char
            pointer += 1
        
        return res