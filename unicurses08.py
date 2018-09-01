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

    window = curses.newwin(2, 25, 3, 5)
    window.addstr(0,0,"Hello, World!")

    # this window will now be displayed. Since we are doing getch
    # on window, that one is brought to front, window 2 isn't.
    # We can tackle this with panels. Or, explicitly call window2.refresh()
    window2 = curses.newwin(2, 25, 3, 50)
    window2.addstr(0,0,"Hello, World again!")
    
    while True:
      key = window.getch()
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