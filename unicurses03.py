import unicurses as curses

def main():
  ## Curses normal init sequence
  stdscr = curses.initscr()
  try:
    while True:
      c = curses.getch()
      if c == 27:
        break

      stdscr.addstr(10,0,"Keycode was %s and the key was %s" % (format(c, '>3'), chr(c)))
      curses.move(0,0)
  except Exception as e:
    stdscr.addstr(0,0,str(e))
    curses.getch()
  finally:

    curses.endwin()
  
  return 0

if __name__ == '__main__':
  main()