from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)   # Always get the smallest card
        
        while min_heap:
            first = min_heap[0]   # smallest card available
            
            # Try to build group of consecutive cards
            for card in range(first, first + groupSize):
                if count[card] == 0:
                    return False
                
                count[card] -= 1
                if count[card] == 0:
                    if card != min_heap[0]:
                        # If a middle card becomes zero, heap ordering breaks
                        return False
                    heapq.heappop(min_heap)
        
        return True
