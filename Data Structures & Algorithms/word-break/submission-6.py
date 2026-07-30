class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bfs solution
        # at each inflection point, add the word as well as not the word to the queue
        # go until the queue is empty

        queue = deque()
        queue.append(0)

        total = len(s)

        dictSet = set(wordDict)
        seen = set()

        while queue:
            full_string = queue.popleft()
            if full_string in seen:
                continue
            seen.add(full_string)

            if full_string == total:
                return True
            
            # iterate from the beginning
            # if we see a word, add the remaining substring to the queue
            # red
            remaining = full_string + 1
            while remaining <= total:
                sub = s[full_string:remaining]
                if sub in dictSet and remaining not in seen:
                    queue.append(remaining)
                remaining += 1
        
        return False

        