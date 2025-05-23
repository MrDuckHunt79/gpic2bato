# gpic2bato
**A set of scripts/config to use Gpi Case 2 with Batocera 41+**

# Notice
Actually support only Safe Shutdown, hdmi switch for GPi case 2 dock will be added in later releases.

# Info
The GPi Case 2 has only a power switch and a power save button, so why do you need the Safe Shutdown script?
It's a security measure to try to avoid data loss, so when you push the power save button (or automatically after 20 minutes of inactivity) the case enters in power save mode, then if not resumed for 15 minutes the case issues a GPIO event and the shutdown script powers off the system safely.

## Prerequisite:
Already created a Batocera sd card with RPi Imager (o similar software)

## Install:

1)  Copy config.txt to your boot partition of Batocera sd card (Usually labelled BATOCERA)
2) Insert sd card on your GPi case 2 and turn it on.
3) Connect it to WiFi
4) Then connect to it with an SSH client (default user is 'root' and password is 'linux')
5) Run this command:
    wget -O - "https://mrduckhunt79.github.io/gpic2bato/install.sh" | bash

Enjoy your GPi case 2 with Batocera

## Thanks
Retroflag, Batocera Team, Recalbox Team for their work

