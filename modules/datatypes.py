class Rect():
  def __init__(self, x=0, y=0, w=0, h=0):
    self.x, self.y, self.w, self.h = x, y, w, h


class Childs():
  class Node():
    def __init__(self, data=None):
      self.data = data
      self.prev = None
      self.next = None

  def __init__(self, *iterable):
    self.head = self.head.prev = self.head.next = Childs.Node()
    self._len = 0

  def __len__(self):
    return self._len

  def append(self, data=None):
    new_node = Childs.Node(data)
    new_node.prev = self.head
    new_node.next = self.head.next
    self.head.next = self.head.next.prev = new_node
    self._len += 1
    return new_node

  def move_top(self, node):
    node.next.prev = node.prev.next
    node.prev = self.head
    node.next = self.head.next
    self.head.next = self.head.next.prev = node

  def printall(self):
    n = self.head.next
    while not n == self.head:
      print(n.data)
      n = n.next
      
"""
  def __iter__(self):
    return ChildsIterator(self)

class ChildsIterator():
  def __init__(self, childs):
    self.i = 0
    self._childs = childs

  def __iter__(self):
    return self

  def __next__(self):
    pass
"""