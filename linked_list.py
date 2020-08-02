class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
    
    def append_to_head(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return 
        temp.next = self.head
        self.head = temp
    
    def remove_dups(self):
        buffer = []
        cur = self.head
        prev = None
        while cur:
            if cur.val in buffer:
                prev.next = cur.next
                cur = None
            else:
                buffer.append(cur.val)
                prev = cur
            cur = prev.next
    
    def get_nth_to_last_node(self,pos):
        cur = self.head
        length = 0
        while cur.next:
            # print(cur.val)
            cur = cur.next
            length +=1
        cur = self.head
        print(length)
        for i in range(length-pos+1):
            cur = cur.next
            # print(cur.val)
        
        return cur.val
    
    def count_occr(self, data):
        cur = self.head
        buffer = dict()
        while cur:
            if cur.val == data and cur.val in buffer:
                buffer[cur.val] = buffer[cur.val]+1
            elif cur.val == data and cur.val not in buffer:
                buffer[cur.val] = 1
           
            cur = cur.next
        
        return buffer[data]
    def rotate(self, pos):
        p = self.head
        q = self.head
        for i in range(1,pos):
            p=p.next
            q=q.next
        print(p.val)
        print(q.val)
        while q.next:
            q=q.next
        print(q.val)
        q.next = self.head
        nxt = p.next
        p.next =None
        self.head = nxt
    
    def head_to_tail(self):
        # p = self.head
        # prev = None
        # first = p.val
        # while p.next:
        #     prev = p
        #     p = p.next
        # p = prev
        # last = p.next.val
        # p.next.val = first
        # self.head.val = last
        p = self.head
        prev = None
        while p.next:
            prev = p
            p = p.next
        p.next = self.head
        prev.next = None
        self.head = p
    
    def sum_two_list(self, second_list):
        p = self.head
        q = second_list.head
        carry = 0
        sum_linked_list = linked_list()
        while p or q:
            
          
       






       
        


                      
        


ll = linked_list()
ll.append_to_head(5)
ll.append_to_head(6)
ll.append_to_head(3)
ll2 = linked_list()
ll2.append_to_head(8)
ll2.append_to_head(4)
ll2.append_to_head(2)
ll.sum_two_list(ll2)
# ll.append_to_head("F")
# ll.append_to_head("E")
# ll.append_to_head("D")
# ll.append_to_head("C")
# ll.append_to_head("B")
# ll.append_to_head("A")
# ll.append_to_head(11)
# ll.append_to_head(9)
# ll.append_to_head(7)
# ll.append_to_head(5)
# ll.append_to_head(5)
# ll.print_list()
# # ll.remove_dups()
# print("<---------------->")
# # ll.print_list()
# print(ll.get_nth_to_last_node(4))
# print(ll.count_occr(5))
# ll.rotate(2)
# print("--------------")
# ll.print_list()
# ll.print_list()
# print("----------------------")
# ll.head_to_tail()
# ll.print_list()



