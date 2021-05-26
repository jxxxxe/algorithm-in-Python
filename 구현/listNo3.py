class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node(None)
        self.tail=self.head

    def add(self,data):
        if self.head.next==None:
            newNode=Node(data)
            self.head.next=newNode
            self.tail=newNode
        else:
            newNode=Node(data)
            self.tail.next=newNode
            self.tail=newNode
            
    def delete(self,node):
       nextNode=node.next
       node.data=nextNode.data
       node.next=nextNode.next
       del nextNode
       

def printing(mylist):
    current=mylist.head.next
    while current!=None:
        print("{} ".format(current.data),end="")
        current=current.next
    print("")



listNo3=LinkedList()

listNo3.add("a")
listNo3.add("b")
listNo3.add("c")
deleteNode=listNo3.tail
listNo3.add("d")
listNo3.add("e")

printing(listNo3)


listNo3.delete(deleteNode)

printing(listNo3)