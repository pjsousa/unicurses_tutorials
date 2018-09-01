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

    window = curses.newwin(3, 20, 5, 5)
    window.addstr(1,1,"Hey there!")
    window.box()

    window2 = curses.newwin(3, 20, 4, 4)
    window2.addstr(1,1,"Hey there, again!")
    window2.box()

    panel = curses.new_panel(window)
    panel2 = curses.new_panel(window2)

    #curses.move_panel(panel, 10, 30)

    curses.update_panels()
    curses.doupdate()

    top_p = None

    while True:
      key = curses.getch()
      if key == 27:
        break

      top_p = panel if top_p is panel2 else panel2
      curses.top_panel(top_p)

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