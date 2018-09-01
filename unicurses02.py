import unicurses as curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()

  curses.move(5,0)
  stdscr.addstr("Hello World (move)")
  for i in range(50):
  	stdscr.addstr(10, i, "Hello World")
  	curses.getch()
  
  curses.endwin()
  return 0

if __name__ == '__main__':
  main()