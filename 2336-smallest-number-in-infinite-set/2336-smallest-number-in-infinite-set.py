class SmallestInfiniteSet:

    def __init__(self):
        self.arr = list(range(1,1001))
        print(self.arr)
    def popSmallest(self) -> int:
        self.swap(0,len(self.arr)-1)
        val = self.arr.pop()
        self.downheapify(0)
        return val
        
    def downheapify(self,parent):
        idx = parent
        child1 = (2*parent) + 1
        child2 = (2*parent) + 2
        
        if child1 < len(self.arr) and self.arr[child1] < self.arr[idx]:
            idx = child1
        if child2 < len(self.arr) and self.arr[child2] < self.arr[idx]:
            idx = child2
        
        if idx != parent:
            self.swap(parent,idx)
            self.downheapify(idx)
        
    
    def swap(self,s,d):
        self.arr[s],self.arr[d] = self.arr[d],self.arr[s] 
        
    def addBack(self, num: int) -> None:
        if num not in self.arr:
            self.arr.append(num)
            self.upheapify(len(self.arr)-1)
        
    def upheapify(self,child):
        if child == 0:
            return
        parent = (child - 1) // 2
        if self.arr[child] < self.arr[parent]:
            self.swap(child,parent)
            self.upheapify(parent)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)