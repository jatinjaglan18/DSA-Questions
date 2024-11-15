class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        d = {}
        hand.sort()
        
        for card in hand:
            d[card] = 1 + d.get(card, 0)
            
        for card in hand:
            if d[card] == 0:
                continue
            else:
                for i in range(groupSize):
                    if d.get(card + i, 0) > 0:
                        d[card+i] -= 1
                    else:
                        return False
                    
        
        return True
        
        