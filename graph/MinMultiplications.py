from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        q = deque()
        q.append((start, 0))

        dist = [int(1e9)] * 100000
        dist[start] = 0
        mod = 100000

        while q:
            node, steps = q.popleft()

            # Try multiplying node with each element in arr
            for factor in arr:
                num = (factor * node) % mod

                # If this path is better (fewer steps), update and enqueue
                if steps + 1 < dist[num]:
                    dist[num] = steps + 1

                    # If we reached the target, return the number of steps
                    if num == end:
                        return steps + 1
                    
                    q.append((num, steps + 1))

        # Return -1 if unreachable
        return -1
