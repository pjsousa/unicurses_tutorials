import unicurses as curses
#import curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()
  try:
    stdscr.addstr("Hello ")
    curses.attron(curses.A_BOLD)
    stdscr.addstr("World! (Bold)")
    curses.attroff(curses.A_BOLD)

    stdscr.addstr("\nHello ")
    curses.attron(curses.A_REVERSE)
    stdscr.addstr("World! (Reverse)")
    curses.attroff(curses.A_REVERSE)

    stdscr.addstr("\nHello World! (Inline Bold)", curses.A_BOLD)
    stdscr.addstr("\nHello World! (Inline Reverse)", curses.A_REVERSE)

    stdscr.addstr("\nHello World! (Inline Underline)", curses.A_UNDERLINE)
    stdscr.addstr("\nHello World! (Inline BLINK!)", curses.A_BLINK)
    stdscr.addstr("\nHello World! (Inline RED)", curses.COLOR_RED)

    stdscr.getch()
  except Exception as e:
    stdscr.addstr(0,0,str(e))
    stdscr.getch()
  finally:

    curses.endwin()
  
  return 0

if __name__ == '__main__':
  main()