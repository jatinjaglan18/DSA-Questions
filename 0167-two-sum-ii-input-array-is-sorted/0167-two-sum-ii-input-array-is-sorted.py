class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''l = []
        for i in range(len(numbers)):
            val = target - numbers[i]
            for j in range(len(numbers)-1,i,-1):
                if numbers[j] == val:
                    return [i+1,j+1]
                elif numbers[j] < val:
                    break'''
        
        r , l = 0, len(numbers)-1
        for i in range(len(numbers)):
            val = numbers[r] + numbers[l]
            if val == target:
                return [r+1, l+1]
            elif val > target:
                l -= 1
            else:
                r  += 1
                
                    