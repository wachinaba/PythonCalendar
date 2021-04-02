import datatypes as dt

class BaseContainer():
  def __init__(self, rect: dt.Rect):
    self.rect = rect
    self.childs = dt.Childs()

  def append(self, child):
    self.childs.append(child)

  

