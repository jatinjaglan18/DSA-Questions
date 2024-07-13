class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(numbers)):
            val = target - numbers[i]
            for j in range(len(numbers)-1,i,-1):
                if numbers[j] == val:
                    return [i+1,j+1]
                elif numbers[j] < val:
                    break
                    