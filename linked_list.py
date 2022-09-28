# linked list implimentation

class Node:
    def __init__(self,item):
        self.item=item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data)  #created node
        node.next=self.head  #asigned next value of this node as current head
        self.head=node # now assign head to the newly created node

    def insert_at_last(self,data): 
        t=self.head #assign first node to t
        while t.next: # traverse a nodes till the last node whose next value will be null
            t=t.next  # save value of next node into t 

        node=Node(data) #create a node
        t.next=node # asign new node next value of last node 

    def print(self):
        while self.head!=None:
            print(self.head.item)
            self.head=self.head.next

linked_list=LinkedList()

linked_list.head=Node(1)   #first item head
second=Node(2)    #second item
third=Node(3)     #third item

linked_list.head.next=second
second.next=third
linked_list.insert_at_begining(5)
linked_list.insert_at_last(9)

linked_list.print()
