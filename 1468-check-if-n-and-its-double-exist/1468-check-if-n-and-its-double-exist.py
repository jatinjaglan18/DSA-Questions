class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        for i in arr:
            if i == 0:
                continue
            if i % 2 == 0:
                if i // 2 in arr:
                    return True
        return False