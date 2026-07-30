# list of strings -> string -> list of strings
# any ascii characters

# [hello, world] -> [5/hello5/world] -> [hello, world]
# [3/a, world] -> [3/3/a5/world] -> [3/a, world]

# cases
# consider upper and lower case letters
# consider multi digit length

# n - number of strings in strs
# m - number of total characters 

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            str_length = len(string)
            payload = str(str_length) + "/" + string
            result += payload
        
        return result

    def decode(self, s: str) -> List[str]:
        # 2 pointers, 1 
        # one pointer at beginning, other increments until we hit slash
        # once we do, assign length, retrieve string 
        result = []
        i = 0 
        j = 0

        while i < len(s):
            j += 1
            if s[j] == '/':
                length = int(s[i:j])
                i = j + 1
                result.append(s[i:i+length])
                i = i + length
                j = i

        return result