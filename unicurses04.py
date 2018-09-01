import unicurses as curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()
  try:
    max_y, max_x = curses.getmaxyx(stdscr)
    coords = str((max_y, max_x))
    stdscr.addstr(max_y//2, max_x//2 - len(coords) // 2, coords)
    curses.move(max_y-1, max_x-1)
    curses.getch()
  except Exception as e:
    stdscr.addstr(0,0,str(e))
    curses.getch()
  finally:

    curses.endwin()
  
  return 0

if __name__ == '__main__':
  main()