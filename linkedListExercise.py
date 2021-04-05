class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def PrintList(self): 
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def AtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head 
        self.head = newNode

    def AtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=newNode

    def InBetween(self, middleNode, data):
        if middleNode is None:
            print("Please mention the node")
            return
        newNode = Node(data)
        newNode.next = middleNode.next
        middleNode.next = newNode

    def RemoveNode(self, removeKey):
        head = self.head
        if (head is not None):
            if (head.data == removeKey):
                self.head = head.next
                head = None
                return
        while (head is not None):
            if head.data == removeKey:
                break
            previous = head
            head = head.next
        if (head == None):
            return
        previous.next = head.next
        head = None

print("The expected end product of the following executions are the day, Mon to Fri.")
print("Create linked list, then")
list = SLinkedList()
list.PrintList()
print("Add a head node to the list:")
list.head = Node("Mon") 
list.PrintList()
print("Define nodes e2 and e3 as Wed and Thu, then")
e2 = Node("Wed")
e3 = Node("Thu")
print("Link the head node to node e2:")
list.head.next = e2
list.PrintList()
print("Link the the second node, e2 to node e3:")
e2.next = e3
list.PrintList()
print("""Add "Sun" to the beginning of the list:""")
list.AtBeginning("Sun")
list.PrintList()
print("""Add "Fri" to the end of the list:""")
list.AtEnd("Fri")
list.PrintList()
print("""Add "Tue" (In Between) after the head node:""")
list.InBetween(list.head.next,"Tue")
list.PrintList()
print("""Remove "Sun" from the list:""")
list.RemoveNode("Sun")
list.PrintList()