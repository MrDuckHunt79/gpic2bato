# gpic2bato
**A set of scripts/config to use Gpi Case 2 with Batocera 41+**  
In this project I have tried to merge and review scripts and configs taken from the repository of Retroflag, Batocera and Recalbox, to get a config.txt and a service script that fit for Batocera 41+

>[!NOTE]
>Actually the installer activate only service that support Safe Shutdown feature, hdmi switch for GPi case 2 dock will be added in later releases.  
>I'm working on this on my spare time, so develpment could take a little.


## Prerequisite:
Already created a Batocera sd card with RPi Imager (o similar software)

## Install:

1)  Copy [config.txt](https://github.com/MrDuckHunt79/gpic2bato/blob/main/config.txt) to your boot partition of Batocera sd card (Usually labelled BATOCERA)
2) Insert sd card on your GPi case 2 and turn it on.
3) Connect it to WiFi
4) Then connect to it with an SSH client (default user is 'root' and password is 'linux')
5) Run this command:  
    wget -O - "https://mrduckhunt79.github.io/gpic2bato/install.sh" | bash
6) Enjoy your GPi case 2 with Batocera

> [!WARNING]
> During the first boot, and even after the first reboot triggered by install.sh it is very likely that sound doesn't work, just power off batocera and switch off the power switch, then sound will work correctly.

> [!TIP]
> The GPi Case 2 has only a power switch and a power save button, so why do you need the Safe Shutdown script?  
> It's a security measure to try to avoid data loss, so when you push the power save button (or automatically after 15 minutes of inactivity) the case enters in power save mode, then if not resumed for 20 minutes the case issues a GPIO event and the shutdown script powers off the system safely.

## To Do
- [X] Rewrite config.txt
- [X] Adapt python script for Safe Shutdown.
- [X] Write and test the first version of the install script.
- [ ] Write a better service script to handle correctly the service.
- [ ] Review the install script
- [ ] Rewrite python script to use gpiod istead of rpi.gpio
- [ ] Start working on a script for GPi Case 2 Docking station.

## Thanks
Retroflag, Batocera Team, Recalbox Team for their work

