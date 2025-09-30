
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 5
def find_kth_from_end(ll: LinkedList, k):  
  fast = ll.head
  slow = ll.head
  count = 0
  while(count < k):
    if(fast):
      fast = fast.next
      count = count + 1
    else:
        return None
  while(fast):
    fast = fast.next
    slow = slow.next      

  return slow

result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4


# def find_kth_from_end(ll: LinkedList, k):  
#   fast = ll.head
#   slow = ll.head
#   count = 0
#   while(fast and fast.next):
#    while(count < k):
#     if(fast and fast.next):
#       fast = fast.next
#       count = count + 1
#     else:
#        count = k  
#   slow = slow.next    
#   return slow