# You are tasked with implementing a basic data structure: a singly linked list.

# To accomplish this, you will create two classes, Node and LinkedList.

# The Node class will represent an individual node within the linked list, while the LinkedList class will manage the overall list structure.

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        pass 

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next ##to the next node
        print('end of the list!')    
    def append_item(self,value):
        new_node = Node(value)
        if self is not None:
            self.tail.next = new_node
            self.tail = new_node 
        else:
           self.tail = new_node
           self.head = new_node   
        self.length += 1     
        return True
    def pop_last_item(self):
        temp = self.head 
        pre = self.head 
        if self.length == 0:
            return None 
        if self.length == 1: 
            self.tail = None 
            self.head = None
            self.length = self.length - 1
            return self
        while (temp.next):
                pre = temp
                temp = temp.next      
                # if temp.next is not None:
                #     self.temp = self.pre
        self.tail = pre
        self.tail.next = None
        self.length = self.length - 1
        return temp
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
    def add(self, item):
        node = Node(item)
        if self is None:
            self.head = Node 
            self.tail = Node 
        else:    
            self.head.next = node  
            self.tail.next = node  
            self.tail = node
            self.length = self.length + 1
        return self
    def prepend(self,item):
        node = Node(item)
        if self.length == 0:
            self.head = node
            self.tail = node
        node.next = self.head
        self.head = node 
        self.length = self.length + 1
    def popFirst(self):
        if self.length == 0 or self.length == 1:
            self.head = None 
            self.tail = None 
        else:    
            first_node = self.head.next 
            self.head = first_node
            self.length = self.length - 1
            return first_node
    def get(self,index):
        if (index > self.length):
            message = 'index out of bound'
            print(message)
            return message
        elif(self.length == 0):
            message = 'linked list is empty!'
            return message
        else:
            my_node = self.head
            position = 0
        while(position != index):
            position = position + 1
            my_node = my_node.next 
        print(my_node.value)
        return my_node    



my_linked_list = LinkedList(1)    
my_linked_list.append_item(2)
my_linked_list.append_item(3)
my_linked_list.append_item(4) 
my_linked_list.get(10)
# my_linked_list.pop_last_item()
# my_linked_list.pop_last_item()
# my_linked_list.pop_last_item()
# my_linked_list.pop()
# my_linked_list.print_list() 
# my_linked_list.prepend(5)
# my_linked_list.popFirst()
# my_linked_list.print_list() 
# my_linked_list.popFirst()
# my_linked_list.print_list() 
# my_linked_list.popFirst()
# my_linked_list.print_list() 
# my_linked_list.popFirst()
# my_linked_list.print_list() 
# my_linked_list.popFirst()
# my_linked_list.print_list() 
# my_linked_list.popFirst()
# my_linked_list.print_list() 
# my_linked_list.append_item(2)
# my_linked_list.print_list() 
# my_linked_list.pop()
# my_linked_list.print_list() 
# my_linked_list.append_item(1)