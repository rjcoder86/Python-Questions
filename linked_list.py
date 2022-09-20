# linked list implimentation

class Node:
    def __init__(self,item):
        self.item=item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        while self.head!=None:
            print(self.head.item)
            self.head=self.head.next

linked_list=LinkedList()

linked_list.head=Node(1)   #first item head
second=Node(2)    #second item
third=Node(3)     #third item

linked_list.head.next=second
second.next=third

linked_list.print_ll()

# print(linked_list.head.item)
# print(second.item)
# while linked_list.head!=None:
#     print(linked_list.head.item)
#     linked_list.head=linked_list.head.next