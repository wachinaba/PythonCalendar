import datatypes as dt

class BaseContainer():

  STATE_STAY = 0
  STATE_NEEDREDRAW = 1

  def __init__(self, rect: dt.Rect, parent: BaseContainer):
    self.rect = rect
    self.childs = dt.Childs()
    self.state = self.STATE_STAY
    self.parent = parent
    self.node = None

  def send_redraw(self):
    self.state = self.STATE_NEEDREDRAW
    if not self.parent:
      self.parent.send_redraw()

  def append(self, container):
    container.parent = self
    appended_node = self.childs.append(container)
    appended_node.container.node = appended_node

  def detach(self):
    return self.childs.delete(self.node)
