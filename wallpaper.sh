#!/bin/sh
find /home/stan/Pictures -type f | shuf -n 1 | xargs feh --bg-scale
