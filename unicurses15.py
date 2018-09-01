import unicurses as curses
from functions import *
from player14 import *

def main():

  if not curses.has_colors():
    print("Your terminal emulator needs to have colors.")
    return 0

  ## Curses normal init sequence
  stdscr = curses.initscr()
  curses.noecho() # no echo, but we still see the cursor
  curses.curs_set(False) #turns off the cursor drawing
  stdscr.keypad(True) # allows special keys and arrow keys
  
  try:
    curses.start_color()  

    avatar = Player(stdscr, "@", curses.COLOR_RED, curses.COLOR_BLACK, curses.A_BOLD)

    curses.attron(curses.color_pair(1))
    curses.vline("|", 10)
    curses.hline("-", 10)
    curses.attroff(curses.color_pair(1))


    while True:
      key = curses.getch()

      avatar.move(key)

      if key == 27:
        break


      curses.update_panels()
      curses.doupdate()

  except Exception as e:
    stdscr.addstr(0,0,str(e))
    stdscr.getch()
  finally:
    
    curses.endwin()
  
  return 0

if __name__ == '__main__':
  main()