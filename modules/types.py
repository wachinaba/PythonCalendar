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
    new = Childs.Node()
    self.head = new
    self.head.prev = self.head.next = new

  def __iter__(self):
    return ChildsIterator(self)

class ChildsIterator():
  def __init__(self, ll):
    self.i = 0
    self._ll = ll

  def __iter__(self):
    return self

  def __next__(self):
    pass
