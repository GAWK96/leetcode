class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
##test!
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def insert(self,index,value):
     if(index != 0 and index < self.length):
        new_node = Node(value) 
        temp = self.head
        pre = self.head
        count = 0
        while(count < index):
            pre = temp
            temp = temp.next 
            count = count + 1 
        pre.next = new_node 
        new_node.next = temp
        return new_node
     else:
        print('value cant be added')
    def set_value(self, index, value):
        temp = self.head
        count = 0
        if(self.length < index):
            print("can't insert value!")    
            return None
        if(self.length < index):
          while(index > count):
            temp = temp.next
            count = count + 1 
        temp.value = value
        return temp
    def remove(self,index):
        # temp = self.head 
        if(index > self.length):
            print('index not found in the list!')
            return None
        pre = self.head 
        temp = self.head
        count = 0
        while(count < index):
            pre = temp
            temp = temp.next
            count = count + 1
        pre.next = temp.next
        print(temp.next)
        return temp    
    def reverse(self):
        temp = self.head
        old_head = self.head 
        pre = None
        count  = 0
        while(temp):
            next = temp.next
            temp.next = pre
            pre = temp
            temp = next
            count = count + 1
        self.tail = old_head 
        self.head = pre 
        return self
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
print('____________')
my_linked_list.reverse()
# my_linked_list.insert(2,6)
# my_linked_list.remove(4) 
# my_linked_list.print_list()
# my_linked_list.print_list()
# my_linked_list.set_value(2,2)
# my_linked_list.print_list()
# my_linked_list.set_value(13, 13)
# my_linked_list.remove(2) 
my_linked_list.print_list()