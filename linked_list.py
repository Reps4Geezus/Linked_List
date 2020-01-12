class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def insertFirst(self, data):
    self.head = Node(data, self.head)
    self.size += 1

  def insertLast(self, data):
    node = Node(data)
    current = None
    if(self.head == None):
      self.head = node
    else:
      current = self.head
      while(current.next):
        current = current.next
      current.next = node
    self.size += 1

  def printList(self):
    current = self.head
    while(current != None):
      print(current.data)
      current = current.next

  def insertAt(self, index, data):
    if(index > 0 & index > self.size):
      return
    if(index == 0):
      self.head = Node(data, self.head)
      return
    node = Node(data)
    previous = None
    current = self.head
    count = 0
    while(count < index):
      previous = current
      count += 1
      current = current.next
    node.next = current
    previous.next = node
    self.size += 1

  def getAt(self, index):
    count = 0
    current = self.head
    if(index < 0 | index > self.size):
      print("Out of bounds!")
      return
    while(current != None):
      if(count == index):
        print(current.data)
        return
      count += 1
      current = current.next
    return None

  def removeAt(self, index):
    if(index < 0 | index > self.size):
      print("Out of bounds")
      return
    current = self.head
    previous = None
    count = 0
    if(index == 0):
      self.head = current.next
    else:
      while(count < index):
        count += 1
        previous = current
        current = current.next
      previous.next = current.next
    self.size -= 1

  def clearList(self):
    self.head = None
    self.size = 0

Llist = LinkedList()

Llist.insertFirst("Hello world")
Llist.insertFirst("I am awesome")

for i in range(10):
  Llist.insertFirst(i)

Llist.insertLast("I am last")
Llist.insertAt(4, "I was inserted")

Llist.printList()
print()
Llist.getAt(Llist.size - 1)
Llist.removeAt(Llist.size - 1)
print()
Llist.printList()
Llist.clearList()
