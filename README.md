# TTY-loop
"Funny" Script

Creates autorun.sh and adds it to systemctl.<br>
autorun.sh turns on python script that loops tX.sh files changing actual terminals (TTY) in Linux without GUI.<br>
Maybe also works with GUI but i didn't checked this.<br>
Every Instructions what to do next after running sysctladd.py you'll see in-script ("print()" responses).<br>

REMEMBER!
I recommend to put this files into main directory (eg. /nohome  or  /TTYloop) with 777 permissions in chmod (after creating autorun.sh).

Program uses root permissions:
- chmod files (chmod -R 777 /directory)
- adding TTYloop.service in systemd directory (see sysctladd.py)
