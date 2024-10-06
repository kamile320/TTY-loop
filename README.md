# TTY-loop
"Funny" Script

Creates autorun.sh and adds it to systemctl.
autorun.sh turns on python script that loops tX.sh files changing actual terminals (TTY) in Linux without GUI
Maybe also works with GUI but i didn't checked this.

REMEMBER!
I recommend to put this files into main directory (eg. /nohome  or  /TTYloop) with 777 permissions in chmod (after creating autorun.sh).

Program uses root permissions:
- chmod files (chmod -R 777 /directory)
- adding TTYloop.service in systemd directory (see sysctladd.py)
