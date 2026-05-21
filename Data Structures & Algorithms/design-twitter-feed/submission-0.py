class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followee = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # add all initial tweets to a list
        res = []
        lastTweets = []

        self.followee[userId].add(userId)

        for user in self.followee[userId]:
            if user in self.tweets:
                index = len(self.tweets[user]) - 1
                count, tweetId = self.tweets[user][index]
                lastTweets.append([count, tweetId, user, index - 1])
        
        heapq.heapify(lastTweets) # O(n)

        while lastTweets and len(res) < 10:
            count, tweetId, user, index = heapq.heappop(lastTweets)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[user][index]
                heapq.heappush(lastTweets, [count, tweetId, user, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)
        
