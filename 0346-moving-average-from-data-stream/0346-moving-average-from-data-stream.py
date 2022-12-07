class MovingAverage:

    def __init__(self, size: int):
        self.size = size         
        self.numbers=[]
        
        

    def next(self, val: int) -> float:
        
        
        self.numbers.append(val)
        
        if len(self.numbers)> self.size:
            self.numbers.pop(0)
            
            avg=sum(self.numbers) / self.size
            
            
            
            return avg 
        
        else:
            avg=sum(self.numbers) / len(self.numbers)
            return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)