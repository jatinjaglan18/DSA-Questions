class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.d = {}
        self.l = []
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
            return self.d[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.l.remove(key)
            self.l.append(key)
            self.d[key] = value
        
        elif key not in self.d.keys() and len(self.d) < self.size:
            self.l.append(key)
            self.d[key] = value
        
        else:
            k = self.l.pop(0)
            del self.d[k]
            self.l.append(key)
            self.d[key] = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)