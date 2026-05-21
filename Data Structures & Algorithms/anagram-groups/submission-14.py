# anagrams - only check characters
# dictionary problem
# output order doesnt matter
# use sum of ascii as key

# cases
# only lowercase
# initial list of strs is empty

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: any word, values: list of indices
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())
        


        