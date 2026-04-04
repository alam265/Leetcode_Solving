class Twitter:

    def __init__(self):
        self.tweet = {} 
        self.follower = {} 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweet: 
            self.tweet[userId] = [(self.time,tweetId)] 
        else: 
            self.tweet[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = [] 
        if userId in self.tweet:
            for twtId in self.tweet[userId]:
                feed.append(twtId) 

        if userId in self.follower:
            for followeeId in self.follower[userId]:
                if followeeId in self.tweet:
                    for twtId in self.tweet[followeeId]:
                        feed.append(twtId) 

        feed.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return   
        if followerId not in self.follower: 
            self.follower[followerId] = set()
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower:
            self.follower[followerId].discard(followeeId)
        
