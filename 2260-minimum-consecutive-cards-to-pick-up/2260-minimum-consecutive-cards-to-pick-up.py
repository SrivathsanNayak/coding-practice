class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        seen = {}
        minLen = float('inf')
        
        #does not contain pair of matching cards
        if len(set(cards)) == len(cards):
            return -1
        
        for i, n in enumerate(cards):
            if minLen == 1:
                return minLen
            if n in seen:
                if i - seen[n] + 1 < minLen:
                    minLen = i - seen[n] + 1
            seen[n] = i
            
        return minLen