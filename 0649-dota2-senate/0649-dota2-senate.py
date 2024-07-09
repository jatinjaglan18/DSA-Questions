class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = []
        dire = []
        
        for i in range(len(senate)):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dire.append(i)
                
        i = 0
        while len(rad) != 0 and len(dire) != 0:
            if rad[0] < dire[0]:
                rad.pop(0)
                dire.pop(0)
                rad.append(len(senate) + i)
                i += 1
            else:
                rad.pop(0)
                dire.pop(0)
                dire.append(len(senate) + i)
                
        if len(rad)  != 0:
            return 'Radiant'
        else:
            return 'Dire'
            
                