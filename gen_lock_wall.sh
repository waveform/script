find /home/stawan01/Pictures -type f | shuf -n 1 | xargs -i convert {} -resize 1920x1200^ -gravity center -extent 1920x1200 /home/stawan01/Pictures/lock.png
