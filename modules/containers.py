import datatypes as dt
import pygame.rect as rect

class BaseContainer():

  STATE_STAY = 0
  STATE_NEEDREDRAW = 1

  def __init__(self, rect: rect.Rect):
    self.rect = rect
    self.childs = dt.Childs()
    self.state = self.STATE_STAY
    self.parent = None
    self.node = None

  def send_redraw(self):
    self.state = self.STATE_NEEDREDRAW
    if self.parent:
      self.parent.send_redraw()

  def append(self, container):
    container.parent = self
    appended_node = self.childs.append(container)
    appended_node.container.node = appended_node

  def detach(self):
    self.parent = None
    self.node = None
    return self.childs.delete(self.node)

  def process_callback(self):
    pass

  def draw_callback(self):
    pass

  def process(self):
    self.process_callback()
    for n in self.childs:
      n.container.process()

  def draw(self):
    self.draw_callback()
    for n in reversed(self.childs):
      if n.container.state and self.STATE_NEEDREDRAW:
        n.container.draw()

