class Twitter:

    def __init__(self):
        self.time = 0
        self.followHashSet = defaultdict(set)
        self.tweets = defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followHashSet[userId].add(userId)

        for followeeId in self.followHashSet[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId])-1
                timer,tweetId = self.tweets[followeeId][index]
                minHeap.append([timer,tweetId,followeeId,index-1])
        heapq.heapify(minHeap)

        while minHeap and len(res)<10:
            timer,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                timer,tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap,[timer,tweetId,followeeId,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followHashSet[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followHashSet[followerId]:
            self.followHashSet[followerId].remove(followeeId)
