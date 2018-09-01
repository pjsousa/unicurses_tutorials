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

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)

    dude = curses.newwin(1, 1, 10, 30)
    curses.waddstr(dude,"@", curses.color_pair(2) + curses.A_BOLD)
    dude_panel = curses.new_panel(dude)

    grass = curses.newwin(10, 50, 5, 5)
    grass.bkgd(" ", curses.color_pair(1))
    grass_panel = curses.new_panel(grass)

    
    curses.top_panel(dude_panel)

    

    curses.update_panels()
    curses.doupdate()

    while True:
      key = curses.getch()
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