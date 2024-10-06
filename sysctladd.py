import os
maindir = os.getcwd()
print("TTYloop adding to systemctl program")

print("Making autorun.sh ...")
try:
    auto = open('autorun.sh', 'w')
    auto.write(f"#!/bin/bash\ncd {maindir}\npython3 ttyloop.py")
    auto.close()
    print("Done.")
except:
    print("Can't make autorun.sh\nAre you root?")

print('Making TTYloop.service in /etc/systemd/system..')
try:
    sys = open('/etc/systemd/system/TTYloop.service', 'w')
    sys.write(f"[Unit]\nDescription=TTYloop autorun service\n\n[Service]\nExecStart={maindir}/autorun.sh\n\n[Install]\nWantedBy=multi-user.target")
    print("Done!")
    print("Run post installation commands to enable TTYloop.service to start with system startup:\nsudo chmod -R 777 [TTYloop directory] <== without this permissions will not work\nsudo systemctl enable TTYloop <== enables on system startup\nsudo systemctl start TTYloop <== Optional\nsudo systemctl daemon-reload <== if you're running this command second time\n\nREMEBER about Reading/Executing permissions for others!!!")
except:
    print("Can't create service file!\nAre you root?")