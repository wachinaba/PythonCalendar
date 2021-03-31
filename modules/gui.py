import types

class BaseContainer():
  def __init__(self, rect: Rect):
    self.rect = rect
    self.childs = list()

  def append(self, child):
    self.childs.append(child)

  def delete(self, child):