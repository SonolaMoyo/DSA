"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current = self.head
        self.head = new_element
        self.head.next = current
        return

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        current = self.head
        self.head = current.next
        return

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        current = self.ll.head
        self.ll.head = new_element
        self.ll.head.next = current
        return

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        current = self.ll.head
        if current:
            self.ll.head = current.next
            return current
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)