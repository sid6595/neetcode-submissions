class Solution:
    def checkPerm(self, s1, s2):
        seen = defaultdict(int)
        seen2 = defaultdict(int)

        for char in s1:
            seen[char] += 1
        
        for char in s2:
            seen2[char] += 1
        
        return seen == seen2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)

        while r <= len(s2):
            if self.checkPerm(s1, s2[l:r]):
                return True
            l += 1
            r += 1
        
        return False


        