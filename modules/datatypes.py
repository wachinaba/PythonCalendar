import copy

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
    self.head.next = new_node
    self.head.next.prev = new_node
    self._len += 1
    return new_node

  def move_top(self, node):
    print("node id:", id(node))
    print("org node:", id(node.prev), " - ", node.data, " - ", id(node.next))
    node.prev.next = copy.copy(node.next)
    node.next.prev = copy.copy(node.prev)
    print("n, p:", id(node.next.prev), id(node.prev.next))
    node.prev = self.head
    node.next = self.head.next
    self.head.next = self.head.next.prev = node

  def printall(self):
    print("head:", id(self.head))
    n = self.head.next
    i=0
    while not n == self.head:
      print(id(n.prev), " - ", n.data, "(", id(n), ")", " - ", id(n.next))
      n = n.next
      i += 1
      if i == self._len : break

      
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