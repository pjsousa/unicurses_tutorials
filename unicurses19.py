import curses
from functions_curses import *
from player18 import *
from room import Room

def main():
  global instances
  ## Curses normal init sequence
  stdscr = curses.initscr()

  if not curses.has_colors():
    print("Your terminal emulator needs to have colors.")
    return 0

  curses.noecho() # no echo, but we still see the cursor
  curses.curs_set(False) #turns off the cursor drawing
  stdscr.keypad(True) # allows special keys and arrow keys
  
  try:
    curses.start_color()

    stdscr_h, stdscr_w = stdscr.getmaxyx()
    world = Room(0, 0, stdscr_h, stdscr_w, "~", curses.COLOR_BLACK, curses.COLOR_BLACK)
    level_room = Room(2,3, 30, 10, "~", curses.COLOR_BLACK, curses.COLOR_BLUE, curses.A_BOLD)
    level_room2 = Room(8,10, 50, 10, "~", curses.COLOR_YELLOW, curses.COLOR_MAGENTA, curses.A_BOLD)
    avatar = Player(stdscr, "@", curses.COLOR_RED, curses.COLOR_BLACK, curses.A_BOLD)

    instances += [world, avatar, level_room, level_room2]

    avatar.correct_background()




    while True:
      key = stdscr.getch()

      avatar.move(key)

      if key == 27:
        break

  except Exception as e:
    stdscr.addstr(0,0,str(e))
    stdscr.getch()
  finally:
    
    curses.endwin()
  
  return 0

if __name__ == '__main__':
  main()