#!/bin/bash

SourcePath=https://mrduckhunt79.github.io/gpic2bato/

#Remount FS as RW------------------------------------------------

sleep 2s
mount -o remount, rw /boot
mount -o remount, rw /

#Download Python script and controller config----------------------------
mkdir /userdata/GPi2C
sleep 2s
script=/userdata/GPi2C/GPic2SS.py
controller=/userdata/system/configs/emulationstation/es_input.cfg
es_settings=/userdata/system/configs/es_settings.cfg


wget -O  $script "$SourcePath/GPic2SS.py"
wget -O  $controller "$SourcePath/es_input.cfg"


if [ -f $es_settings ];
        then
                rm $es_settings
fi

#Create Batocera Service (custom.sh is deprecated since v38)----------
if [ ! -d /userdata/system/services ];
        then
                mkdir /userdata/system/services
fi

sleep 2s

SERVICE=/userdata/system/services/GPic2SS

if [ -f $SERVICE ];
        then
         echo "Service GPic2SS already there. Doing nothing."
        else 
          wget -O $SERVICE "$SourcePath/GPic2SS"
fi

if [ -x "$SERVICE" ];
        then
          echo "Service GPic2SS alreadyconfigured. Doing nothing."
        else
          chmod +x $SERVICE
          echo "Service GPic2SS configured."
fi


#Enable the service--------------------------------------------------

batocera-services enable GPic2SS
sleep 2s
#Reboot-----------------------------------------------------------

echo "GPi case 2 Safe Shutdown service installation done. Will now reboot after 3 seconds."
sleep 3
shutdown -r now
#-----------------------------------------------------------
