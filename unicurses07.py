import unicurses as curses
#import curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()
  curses.noecho() # no echo, but we still see the cursor
  curses.curs_set(False) #turns off the cursor drawing
  stdscr.keypad(True) # allows special keys and arrow keys
  
  try:

    curses.start_color()

    while True:
      key = stdscr.getch()
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