class TimeMap:

    def __init__(self):
        self.dict = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict.keys():
            self.dict[key].append([value,timestamp])
        else:
            self.dict[key] = [[value,timestamp]]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict.keys():
            return ''
        else:
            arr = self.dict[key]
            l = 0
            r = len(arr)-1
            ans = ''
            while l <= r:
                m = (l+r) // 2
                
                if arr[m][1] <= timestamp:
                    ans = arr[m][0]
                    l = m + 1
                else:
                    r = m - 1
            
            return ans
                    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)