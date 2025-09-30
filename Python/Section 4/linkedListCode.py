head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# print(head['next']['next']['value'])

class LinkedList:
    def __init__(self, value):  # value: initialize the first node when start the constructor
        pass

    def append(self, value):  # create a new node
        pass

    def prepend(self, value):  # create a new node
        pass

    def insert(self, index, value):  # create a new node
        pass

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
        pass 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1           

my_linked_list = LinkedList(4) ##head and tail: new node 4. The length will be 1
print(my_linked_list.head.value)