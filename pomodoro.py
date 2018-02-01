import time
import easygui
import sys
from subprocess import Popen, PIPE
from Tkinter import Tk

eg = easygui
sys.path.append('/usr/local/lib/python2.7/site-packages')
from pync import Notifier


def pomodoro():
    #On MacOS, these 3 lines are necessary to get the Tkinter gui window
    #(also used by easygui) to come to the front, which 
    t = Tk()
    t.destroy()
    Popen(['osascript', '-e', 'tell application "Python" to activate'])


    msg = "How long?"
    title = "Pomodoro!"

    mins = 0
    limit = eg.integerbox(msg, title)

    if limit != None:	
            while mins != limit:
                    print ">>>>>>>>>", mins
                    time.sleep(60)
                    mins += 1
            t = Tk()
            t.destroy()
            Popen(['osascript', '-e', 'tell application "Python" to activate'])
            #this pops up a terminal notification message, which is only slightly better than nothing
            #I used this before getting the gui working properly, now it's just supplemental 
            Notifier.notify("Time's up!")
            eg.msgbox("Time's up! Go stretch!", title="Pomodoro!")
    else:
	sys.exit(0)	

def main():
    pomodoro()

if name == '__main__':
    main()

