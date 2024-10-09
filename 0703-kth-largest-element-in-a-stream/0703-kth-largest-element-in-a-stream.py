class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k =  k
        self.num = sorted(nums)

    def add(self, val: int) -> int:
        self.num.append(val)
        self.num.sort()
        return self.num[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)