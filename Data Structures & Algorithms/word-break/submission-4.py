class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bfs solution
        # at each inflection point, add the word as well as not the word to the queue
        # go until the queue is empty

        queue = deque()
        queue.append(s)

        dictSet = set(wordDict)
        seen = set()

        while queue:
            full_string = queue.popleft()
            if full_string in seen:
                continue
            seen.add(full_string)

            if full_string in dictSet:
                return True
            
            # iterate from the beginning
            # if we see a word, add the remaining substring to the queue
            # red
            pointer = 0
            while pointer <= len(full_string):
                sub = full_string[0:pointer]
                if sub in dictSet and sub not in seen:
                    queue.append(full_string[pointer:])
                pointer += 1
        
        return False

        