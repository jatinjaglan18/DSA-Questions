class StockSpanner:

    def __init__(self):
        self.stack = []
        self.l = []

    def next(self, price: int) -> int:
        count = 1 
        while len(self.stack) != 0 and self.stack[-1] <= price:
            self.stack.pop()
            count += self.l.pop()
            
        self.stack.append(price)
        self.l.append(count)    
        return count
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)