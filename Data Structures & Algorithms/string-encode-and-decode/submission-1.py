# list of strings -> a string -> network -> list of strings

# [Hello, World] -> [HelloWorld] -> [Hello, World]

# cases
# empty string returns it back
# any characters, upper case or lowercase

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = len(string)
            payload = str(length) + "#" + string
            result += (payload)
        return result

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i <= (len(s) - 1):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        
        return decoded
