# input: array of strings
# output: array of array of anagrams

# examples
# [act, pots] -> [[act], [pots]]
# [] -> Constraint
# [""] -> [[""]]

# approach
# create a dictionary, each key is the 'identifier' for each anagram
# at each word, we check the dictionary to see if the key for that word exists
# if it does, we'll add our word to the values for this key
# if not, we create a new key, our word is the first value
# return a list of all the values in the dictionary

# [aac]
# [2 0 1 0 0 0 ....] : [aac, caa, aca]
# return dictionary.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for string in strs:
            # initialize key array
            base = [0] * 26
            
            # populate key array
            for char in string:
                val = ord(char) - ord('a')
                base[val] += 1
            
            # convert key to tuple
            base_convert = tuple(base)
            
            # check for key in our dictionary
            dictionary[base_convert].append(string)
        
        return list(dictionary.values())






        