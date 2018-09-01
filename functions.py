import unicurses as curses

global_color_number = 1
def make_color(foreground, background):
  global global_color_number

  color_number = global_color_number

  curses.init_pair(color_number, foreground, background)

  global_color_number += 1

  return color_number