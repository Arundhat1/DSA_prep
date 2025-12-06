import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.followee = defaultdict(set)   # follower -> set of followees
        self.posts_by = defaultdict(list)  # user -> list of (time, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # increase time on each post so larger time == newer
        self.time += 1
        self.posts_by[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):

        heap = []   # min-heap keeping at most 10 newest (by time)
        users = set(self.followee[userId])  # safe due to defaultdict
        users.add(userId)

        for u in users:
            for post in self.posts_by[u]:
                # post is (time, tweetId)
                heapq.heappush(heap, post)
                if len(heap) > 10:
                    # remove the smallest time (oldest) — keep newest 10
                    heapq.heappop(heap)

        # heap now contains up to 10 newest posts but in min-heap order (oldest first)
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])  # collect tweetId
        return result[::-1]  # reverse to return newest -> oldest

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)

