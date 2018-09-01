import unicurses as curses
#import curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()
  try:
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    stdscr.addstr("Hello World!", curses.color_pair(1))
    stdscr.addstr("\nHello World!", curses.color_pair(2) + curses.A_BLINK)
    stdscr.addstr("\nHello World!", curses.color_pair(1) + curses.A_REVERSE)
    stdscr.getch()
  except Exception as e:
    stdscr.addstr(0,0,str(e))
    stdscr.getch()
  finally:

    curses.endwin()
  
  return 0

if __name__ == '__main__':
  main()