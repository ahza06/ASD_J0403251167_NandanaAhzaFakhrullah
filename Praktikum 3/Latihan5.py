class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_end(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    
    def display(self):
        temp=self.head
        elements =[]
        while temp:
           elements.append(str(temp.data))
           temp = temp.next
        print("->".join(elements) + "-> null")
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

input = LinkedList()
input.insert_at_end(7)
input.insert_at_end(8)
input.insert_at_end(9)
input.insert_at_end(10)
input.insert_at_end(100)



print("Linked List Sebelum Dibalik:")
input.display()

print("\nLinked List Sesudah Dibalik:")
input.reverse()
input.display()

