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
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print('null')

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

Delete=LinkedList()
Delete.insert_at_end(1)
Delete.insert_at_end(1)
Delete.insert_at_end(2)
Delete.insert_at_end(3)
Delete.insert_at_end(5)

Deletion = int(input("Masukan data yang ingin dihapus "))

Delete.delete_node(Deletion)
Delete.display()


