#!/usr/bin/python
import sys
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def countdown(total):
    total *= 60
    total -= 1
    while total>=0:
        if total>5*60:
            step = 5
            color = bcolors.OKGREEN
        else:
            step = 1
            color = bcolors.WARNING
        minutes = total/60
        seconds = total%60
        remains = (total%(60*step))/step
        bar = remains*"#"+(60-remains)*" "
        print " %s%02d:%02d %s%s\r" % (color, minutes, seconds, bar, bcolors.ENDC),
        sys.stdout.flush()
        time.sleep(step)
        total -= step

    ending = time.strftime("%H:%M:%S", time.localtime())
    print "%s%s%s\n"%(bcolors.FAIL, "Time's Up!!!  "+ending, bcolors.ENDC);

def helper():
    print "countdown.py minutes"

if __name__ == "__main__":
    if len(sys.argv)<2: helper()
    else: countdown(int(sys.argv[1]))

