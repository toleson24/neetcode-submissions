class DynamicArray:
    dyn_arr = None
    capacity = -1
    size = -1
    
    def __init__(self, capacity: int):
        self.dyn_arr = [0] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.dyn_arr[i]


    def set(self, i: int, n: int) -> None:
        if not self.dyn_arr[i]:
            self.size += 1
        
        self.dyn_arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        
        self.dyn_arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        elem = self.dyn_arr.pop(self.size - 1)
        self.size -= 1

        return elem
 

    def resize(self) -> None:
        self.dyn_arr.extend([0] * self.capacity)
        self.capacity *= 2 


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
