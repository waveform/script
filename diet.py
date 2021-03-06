#!/usr/bin/env python

import re
import os
import sys
import operator
import shutil

history_file = os.path.expanduser("~/.zsh_history")
backup_file = os.path.expanduser("~/.zsh_history.backup")
diet_file = os.path.expanduser("~/.zsh_history_diet")
pattern = r"^: (\d+):\d+;(.*)$"
new_list = []
line_num = 0

lut = {}
with open(history_file, "r") as f:
    for line in f:
        line_num = line_num + 1
        mo = re.match(pattern, line)
        if not mo: print >> sys.stderr, "[ILL FMT]: ", line_num, line,; continue
        time = mo.group(1)
        cmd = mo.group(2)
        lut[cmd] = time
    new_list = sorted(lut.items(), key=operator.itemgetter(1))

print("squash history file from %d line to %d line." % (line_num, len(new_list)))

with open(diet_file, "w") as f:
    for t in new_list:
        f.write(": %s:0;%s\n" % (t[1], t[0]))

shutil.copyfile(history_file, backup_file)
shutil.copyfile(diet_file, history_file)


