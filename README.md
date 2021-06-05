# asusctl-python-gui
A Python GUI for asusctl


Install dependencies:


$ sudo apt install python3 python3-tk

$ echo "deb https://download.opensuse.org/repositories/home:/luke_nukem:/asus/xUbuntu_20.04/ /" > /etc/apt/sources.list.d/asus.list

$ wget -q -O - https://download.opensuse.org/repositories/home:/luke_nukem:/asus/xUbuntu_20.04/Release.key | apt-key add -

$ apt-get update

$ apt-get install asusctl dkms-hid-asus-rog dkms-asus-rog-nb-wmi



Get the GUI:


$ git clone https://github.com/Lun3th/asusctl-python-gui

$ cd git clone https://github.com/Lun3th/asusctl-python-gui



RUN:


$ python3 asusgui.py




Thats an ALPHA-ALPHA stuff. It's only controls the fan speed/profile. Tbh. I think it's useful. Maybe I will implement other features later or I just leave it as it is.
