find /home/stan/Pictures -type f | shuf -n 1 | xargs -i convert {} -resize 1920x1200^ -gravity center -extent 1920x1200 /home/stan/Pictures/lock.png
