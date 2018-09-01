import unicurses as curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()
  stdscr.addstr("Hello World\n")
  curses.getch()
  curses.endwin()
  return 0

if __name__ == '__main__':
  main()