import curses
import serial
import time
ser = serial.Serial("/dev/ttyUSB0",9600,timeout=1)
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
def driveMotor(drct1,drct2):
        valList =[str(drct1), str(drct2)]
        sendStr = ','.join(valList)
        ser.write(sendStr.encode('utf-8'))
        time.sleep(0.1)
try:
        while True:
                char=screen.getch()
                if char==ord('q'):
                        break
                elif char==curses.KEY_UP:
                        drct1=1
                        drct2=1
                        print('Adelante')
                elif char==curses.KEY_LEFT:
                        drct1=1
                        drct2=-1
                        print('Izquierda')
                elif char==curses.KEY_RIGHT:
                        drct1=-1
                        drct2=-1
                        print('Derecha')
                elif char==curses.KEY_DOWN:
                        drct1=-1
                        drct2=1
                        print('Atras')
                elif char==ord('p'):
                        drct1=0
                        drct2=0
                        print('Detenido')
            driveMotor(drct1,drct2)
finally:
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
