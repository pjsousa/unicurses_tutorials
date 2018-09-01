import curses
from player16 import *

def main():

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

    avatar = Player(stdscr, "@", curses.COLOR_RED, curses.COLOR_BLACK, curses.A_BOLD)

    stdscr.attron(curses.color_pair(1))
    stdscr.vline("|", 10)
    stdscr.hline("-", 10)
    stdscr.attroff(curses.color_pair(1))


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