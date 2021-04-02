import copy

class Rect():
  def __init__(self, x=0, y=0, w=0, h=0):
    self.x, self.y, self.w, self.h = x, y, w, h


class Childs():
  class Node():
    def __init__(self, data=None):
      self.data = data
      self._prev = None
      self._next = None

  def __init__(self, *iterable):
    self.head = Childs.Node()
    self.head._prev = self.head
    self.head._next = self.head
    self._len = 0

  def __len__(self):
    return self._len

  def append(self, data=None):
    new_node = Childs.Node(data)
    new_node._prev = self.head
    new_node._next = self.head._next
    self.head._next._prev = new_node
    self.head._next = new_node
    self._len += 1
    return new_node

  def move_top(self, node):
    node._prev._next = node._next
    node._next._prev = node._prev
    node._prev = self.head
    node._next = self.head._next
    self.head._next._prev = node
    self.head._next = node
    
  def printall(self):
    n = self.head._next
    i=0
    while not n == self.head:
      print(n.data)
      n = n._next
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