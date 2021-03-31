class Rect():
  def __init__(self, x=0, y=0, w=0, h=0):
    self.x, self.y, self.w, self.h = x, y, w, h


class Childs():
  class Node():
    def __init__(self, data=None):
      self.data = data
      self.prev = None
      self.next = None
      self._len = 0

  def __init__(self, *iterable):
    self.head = self.head.prev = self.head.next = Childs.Node()

  def append(self, data=None):
    prev_node = self.head
    next_node = self.next
    new_node = Childs.Node(data)

    prev_node.next = next_node.prev = new_node
    new_node.prev = prev_node
    new_node.next = next_node

    self._len += 1

  def move_top(self, node):
    
      

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
