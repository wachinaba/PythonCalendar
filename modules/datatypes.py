import copy

class Childs():
  class Node():
    def __init__(self, container=None):
      self.container = container
      self._prev = None
      self._next = None

  def __init__(self, *iterable):
    self._head = Childs.Node()
    self._head._prev = self._head
    self._head._next = self._head
    self._len = 0

  def __len__(self):
    return self._len

  def append(self, container=None):
    new_node = Childs.Node(container)
    new_node._prev = self._head
    new_node._next = self._head._next
    self._head._next._prev = new_node
    self._head._next = new_node
    self._len += 1
    return new_node

  def delete(self, node):
    node._prev._next = node._next
    node._next._prev = node._prev
    self._len -= 1

  def move_top(self, node):
    node._prev._next = node._next
    node._next._prev = node._prev
    node._prev = self._head
    node._next = self._head._next
    self._head._next._prev = node
    self._head._next = node
    
  def printall(self):
    n = self._head._next
    i=0
    while not n == self._head:
      print(n.container)
      n = n._next
      i += 1
      if i == self._len : break

  def __iter__(self):
    return Childs.Iterator(self)

  def __reversed__(self):
    return Childs.ReversedIterator(self)

  class Iterator():
    def __init__(self, childs):
      self._childs = childs
      self._next_node = self._childs._head

    def __iter__(self):
      return self

    def __next__(self):
      self._next_node = self._next_node._next
      if not self._next_node == self._childs._head:
        return self._next_node
      else:
        raise StopIteration

  class ReversedIterator(Iterator):
    def __init__(self, childs):
      super().__init__(childs)
    
    def __next__(self):
      self._next_node = self._next_node._prev
      if not self._next_node == self._childs._head:
        return self._next_node
      else:
        raise StopIteration
    
      