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

my_linked_list = LinkedList(1)    
my_linked_list.append_item(2)
my_linked_list.append_item(3)
my_linked_list.print_list() 