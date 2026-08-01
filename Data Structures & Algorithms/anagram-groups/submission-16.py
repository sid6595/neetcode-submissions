# group together
# use a dictionary, create some key

# key will be an array of len 26, each is a char

# TC: O(n * m) - n is the number of strs, m is the avg number of chars
# SC: O(n) - number of strings + keys (max can be number of strings) 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            base = [0] * 26

            # go through each char
            for i in range(len(s)):
                # get index
                index = ord(s[i]) - ord('a')
                base[index] += 1
            
            anagrams[tuple(base)].append(s)
        
        return list(anagrams.values())

        