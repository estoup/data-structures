class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head=None):
    self.head = head
    self.length = 0

  def add(self, data):
    if not self.head:
      new_node = Node(data)
      self.head = new_node
    else:
      previous_node = self.head
      while previous_node.next_node:
        current_node = previous_node.next_node
        previous_node = current_node
      new_node = Node(data)
      previous_node.next_node = new_node
    self.length += 1


  def remove(self, data):
    if self.head.data == data:
      self.head = self.head.next_node
    else:
      previous_node = self.head
      current_node = self.head.next_node
      while current_node.data != data:
        previous_node = current_node
        current_node = current_node.next_node
      previous_node.next_node = current_node.next_node
    self.length -= 1
    

  def get(self, element_to_get):
    current_node = self.head
    for _i in range(0, element_to_get):
      current_node = current_node.next_node
    return current_node.data


# ----- Node ------
class Node:
  
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node=next_node


ll = LinkList()
ll.add(1)
ll.add(2)
ll.add(3)

print(ll.head)
print(ll.head.data)
print(ll.head.next_node.data)
print(ll.head.next_node.next_node.data)
print(ll.length)

# ll.remove(3)

print(ll.head.data)
print(ll.head.next_node.data)
print(ll.length)

print(ll.get(0))

