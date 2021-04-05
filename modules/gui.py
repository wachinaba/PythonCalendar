import datatypes as dt

class BaseContainer():

  STATE_STAY = 0
  STATE_NEEDREDRAW = 1

  def __init__(self, rect: dt.Rect):
    self.rect = rect
    self.childs = dt.Childs()
    self.state = 
    self.parent = None

  def send_update

  def append(self, container):
    container.parent = self
    return self.childs.append(container)

  def delete(self, node):
    return self.childs.delete(node)

  

  

