#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import string
from subprocess import Popen, PIPE
# on ubuntu,  notify-send -u critical ??? "title" "body"
def notify():
    body = "Done!!!"
    title = "Notification"
    subtitle = "Job Control"
    sound = "Glass" #"Frog"
    argc = len(sys.argv)
    if argc > 3:
        print("Usage: notify.py [body [title [subtitle]]]")
        return
    if argc > 1:
        body = sys.argv[1].decode('utf-8')
    if argc > 2:
        title = sys.argv[2].decode('utf-8')
    script = """display notification "%s" with title "%s" sound name "%s" """%(body, title, sound)
    #print script
    p = Popen(['osascript', '-e', script])
    #osascript -e 'display notification "$body" with title "$title" subtitle "$subtitle" sound name "Frog"'
if __name__ == '__main__':
    notify()

