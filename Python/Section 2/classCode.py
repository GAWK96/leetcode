# O(2n)
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)          
#O(n) + O(n)
# O(n²)
def print_items2(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#0(n)
    for k in range(n):
     print(k)

print_items2(10)     

def add_items(n):
    return n + n
#1 OPERATION: O(1)
 
def add_items2(n):
    return n + n + n
#2 OPERATIONS, BUT STILL O(2)

#DIFFERENT TERMS FOR INPUTS

def print_items(a,b):
    for i in range(a):
        print(i)
#O(a)
    for j in range(b):
        print(j)
#O(b)

#O(a +b)

def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)
#O(a * b)

