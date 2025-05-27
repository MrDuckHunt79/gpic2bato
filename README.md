# gpic2bato
**A set of scripts/config to use Gpi Case 2 with Batocera 41+**  

## About
In this project I have tried to merge and review scripts and configs taken from the repository of Retroflag, and even from the customized ones of Batocera and Recalbox, to get a config.txt and a service script that fit for Batocera 41+

## What those script do:

1) config.txt is configured to boot up Rpi4 Batocera image on Retrofalg GPi case 2 (Without it lcd isn't recognized)
2) Install and enable Safe Shutdown service to prevent dataloss (Name of the service "GPic2SS" )
3) Install a modified controller map to fit GPi case 2 Controller (thanks to Recalbox team)
4) Install EXPERIMENTAL Docking Station service but don't enable it, you must do it yourself in Batocera menu (Name of the service "GPic2DS" )
   
## EXPERIMENTAL Docking Station service
It's working but isn't hotswap, every time you change from docked to handheld and vicevesa Batocera reboot to init the correct display, so you can't continue playing while changing.  
Service in not enabled by default you must press "start" -> "system options" -> "Services" -> "GPic2DS" 
> [!TIP]
> If you don't have a docking station, or if you use it only as charging station, does not enable the "GPi 2DS" service, is useless and reboot your GPi case 2 when you use the docking for charging.

> [!WARNING]
> When GPi case 2 is doked, automatically disable the onboard controller.

## Prerequisite:
Already created a Batocera sd card with RPi Imager (o similar software) see instruction on Batocera website.
> [!CAUTION]
> Use the image for Raspberry Pi 4 B ! Don't get the one for GPi Case! Because is for another model based on Rasberry Pi 0!  
> ![OK](https://github.com/MrDuckHunt79/gpic2bato/blob/main/imgs/RPI4.png) ![WRONG](https://github.com/MrDuckHunt79/gpic2bato/blob/main/imgs/gpi1.png)


## Install:
> [!CAUTION]
> ISTALLATION MUST BE DONE IN HANDHELD MODE DON'T USE THE DOCKING STATION  

1)  Copy [config.txt](https://github.com/MrDuckHunt79/gpic2bato/blob/main/config.txt) to your boot partition of Batocera sd card (Usually labelled BATOCERA)
2) Insert sd card on your GPi case 2 and turn it on.
3) Connect it to WiFi
4) Then connect to it with an SSH client (default user is 'root' and password is 'linux', you can follow official guide [HERE](https://wiki.batocera.org/access_the_batocera_via_ssh) )
5) Run this command:  
    wget -O - "https://mrduckhunt79.github.io/gpic2bato/install.sh" | bash
6) Enjoy your GPi case 2 with Batocera

> [!WARNING]
> During the first boot, and even after the first reboot triggered by install.sh it is very likely that sound doesn't work, just power off batocera and switch off the power switch, then sound will work correctly.

## Update:

 Just run again:  wget -O - "https://mrduckhunt79.github.io/gpic2bato/install.sh" | bash

## To Do
- [X] Rewrite config.txt
- [X] Adapt python script for Safe Shutdown.
- [X] Write and test the first version of the install script.
- [X] Added controller configuration.
- [X] Write a better service script to handle correctly the service.
- [X] Review the install script
- [X] EXPERIMENTAL script for GPi Case 2 Docking station.

## Thanks
Retroflag, Batocera Team, Recalbox Team for their work  

> [!TIP]
> The GPi Case 2 has only a power switch and a power save button, so why do you need the Safe Shutdown script?  
> It's a security measure to try to avoid data loss, so when you push the power save button (or automatically after 15 minutes of inactivity) the case enters in power save mode, then if not resumed for 20 minutes the case issues a GPIO event and the shutdown script powers off the system safely.

