class LinkedList:
    class Node:
        val = None
        next = None

        def __init__(self, value):
            self.val = value


    dummy = None
    
    def __init__(self):
        self.dummy = self.Node(-1)

    
    def get(self, index: int) -> int:
        i = 0
        curr = self.dummy.next
        while curr and i < index:
            curr = curr.next
            i += 1
        
        return curr.val if curr else -1
        

    def insertHead(self, val: int) -> None:
        newHead = self.Node(val)
        newHead.next = self.dummy.next
        self.dummy.next = newHead
        

    def insertTail(self, val: int) -> None:
        node = self.Node(val)
        
        curr = self.dummy
        while curr.next:
            curr = curr.next
        
        curr.next = node
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.dummy
        while curr.next and i < index:
            curr = curr.next
            i += 1

        if curr.next:
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        vals = []

        curr = self.dummy.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        return vals
