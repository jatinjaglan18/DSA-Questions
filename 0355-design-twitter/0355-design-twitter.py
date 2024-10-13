from collections import deque
import heapq
class Twitter:

    def __init__(self):
        self.tweets = {}    # key -> userID, value -> tweetID
        self.flowee = {}    #key -> userID, value -> flowee
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1 
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.time, tweetId])
        
        if userId not in self.flowee:
            self.flowee[userId] = set()
            self.flowee[userId].add(userId)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweets and userId not in self.flowee:
            return []
        
        f = []
        some = []
        for i in self.flowee[userId]:
            if i in self.tweets:
                some += self.tweets[i]
        feed = sorted(some, key=itemgetter(0))
        for i in feed[:10]:
            f.append(i[1])
        
        return f

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.flowee:
            self.flowee[followerId] = set()
            self.flowee[followerId].add(followerId)
        self.flowee[followerId].add(followeeId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.flowee[followerId]:
            self.flowee[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)