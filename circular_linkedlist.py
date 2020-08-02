class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
            temp.next = temp
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            
            cur.next = temp
            temp.next = self.head
    
    def prepend(self, val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
            temp.next = temp
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            temp.next = self.head
            self.head = temp
            cur.next = self.head
    
    def remove(self, val):
        cur = self.head
        if self.head.data == val:
            while cur.next != self.head:
                cur = cur.next
            nxt = self.head.next
            self.head = nxt
            cur.next = self.head
            return 
        else:
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == val:
                    nxt = cur.next
                    prev.next = nxt
                    # cur.next=None
                    cur = cur.next
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
            if cur == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size // 2
        cur = self.head
        count = 0
        prev = None
        while cur and count < mid:
            count +=1
            prev = cur
            cur = cur.next
        prev.next = self.head
        split_list = Circular_linkedlist()
        while cur.next != self.head:
            split_list.append(cur.data)
            cur = cur.next
        split_list.append(cur.data)
        self.printlist()
        print("\n")
        split_list.printlist()

    
    def printlist(self):
        cur = self.head
        while cur.next != self.head:
            print(cur.data)
            cur = cur.next
        print(cur.data)
    
    def is_circular(self):
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        
        if cur.next == self.head:
            return True
        else:
            return False
       

ll = Circular_linkedlist()
ll.append(5)
ll.append(6)
ll.append(7)
ll.prepend(9)
ll.append(8)
# ll.printlist()
# ll.remove(9)
# print("\n")
# ll.printlist()
# ll.split_list()
print(ll.is_circular())
