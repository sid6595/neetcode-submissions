class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)

        for char_s in list_s:
            try:
                list_t.remove(char_s)
            except:
                return False
        
        if len(list_t) == 0:
            return True
        else:
            return False