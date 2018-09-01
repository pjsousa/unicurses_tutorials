import curses
import curses.panel
from functions_curses import *

class Player:
  def __init__(self, stdscr, body, foreground=None, background=None, attribute=0):
    self.max_x = stdscr.getmaxyx()[1] - 1
    self.max_y = stdscr.getmaxyx()[0] - 1

    self.x = self.max_x // 2
    self.y = self.max_y // 2

    self.body = body

    del stdscr

    # CREATE --------------------------------
    self.window = curses.newwin(1,1,self.y, self.x)
    #self.window.addstr(self.body)
    self.window.bkgd(self.body)
    #self.panel = curses.new_panel(self.window)
    self.panel = curses.panel.new_panel(self.window)

    self.foreground = foreground
    self.background = background

    self.color = 0
    self.attribute = attribute

    if foreground is not None and background is not None:
      self.set_colors(foreground, background)


    self.show_changes()

  def set_colors(self, foreground, background):
    self.color = make_color(foreground, background)
    self.foreground = foreground
    self.background = background

    #self.window.addstr(self.body, curses.color_pair(self.color) + self.attribute)
    self.window.bkgd(self.body, curses.color_pair(self.color) + self.attribute)

    self.show_changes()

  def move(self, key, motion=1):
    moved = False

    if key == curses.KEY_UP:
      if not self.y - motion < 0:
        moved = True
        self.y -= motion
    if key == curses.KEY_DOWN:
      if not self.y + motion > self.max_y:
        moved = True
        self.y += motion
    if key == curses.KEY_LEFT:
      if not self.x - motion < 0:
        moved = True
        self.x -= motion
    if key == curses.KEY_RIGHT:
      if not self.x + motion > self.max_x:
        moved = True
        self.x += motion

    if moved:
      self.panel.move(self.y, self.x)
      self.show_changes()
      

  def show_changes(self):
    curses.panel.update_panels()
    curses.doupdate()
