    
class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
        

class LinkedList():
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.heads
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_with_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    def display(self):
        current_node = self.head
        print("Linked List: ",end=" ")
        while current_node is not None:
            print(current_node.data,end=" ")
            current_node = current_node.next
        print()
    
    
    
    
    
    
ll = LinkedList()
ll.append(1)
ll.append(5)
ll.append(7)
ll.append(5)
ll.append(8)
ll.display()
ll.delete_with_value(1)
ll.append(9)
ll.prepend(4)
ll.append(7)
ll.display()
ll.delete_with_value(5)
ll.display()
