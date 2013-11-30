import time
import curses
import pyfiglet

class TimeBox:
    def __init__ ( self, parent, y, x ):
        self.__dict__['win'] = parent.derwin ( 10, 78, y, x )
        self.update()

    def update ( self ):
        self.win.clear()
        self.win.box()
        t = time.time()
        t_string = pyfiglet.figlet_format ( str ( t ), font = "big" )
        for i, line in enumerate ( t_string.rstrip().split('\n') ):
            self.win.addstr ( 1 + i, 2, line )

    def __getattr__ ( self, attr ):
        return getattr ( self.win, attr )

def main ( screen ):
    tBox = TimeBox ( screen, 0, 0 )
    screen.vline ( 0, 78, '|', 80 )
    screen.timeout ( 10 )
    while ( True ):
        myin = screen.getch()
        if myin == curses.ERR:
            tBox.update()
            tBox.refresh()
        else:
            break

if __name__ == "__main__":
    curses.wrapper ( main )
