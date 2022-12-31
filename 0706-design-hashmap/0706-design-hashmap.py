class MyHashMap:

    def __init__(self):
        self.mapp=[]
        

    def put(self, key: int, value: int) -> None:
        
        for i in range(0,len(self.mapp)):
            if self.mapp[i][0] == key:
                self.mapp[i][0] = key
                self.mapp[i][1] = value
                return
        self.mapp.append([key,value])

    def get(self, key: int) -> int:
        
        for i in self.mapp:
            if i[0] == key:
                return i[1]
        
        return -1
        
        
    def remove(self, key: int) -> None:
        
        for i in self.mapp:
            if i[0] == key:
                self.mapp.remove(i)
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)