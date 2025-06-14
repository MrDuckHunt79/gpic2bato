#!/bin/bash

SourcePath=https://mrduckhunt79.github.io/gpic2bato

#Remount FS as RW------------------------------------------------

sleep 2s
mount -o remount, rw /boot
mount -o remount, rw /

#Setup directories------------------------------------------------

if [ ! -d /userdata/GPi2C ];
        then
                mkdir /userdata/GPi2C
                echo "Creating directory /userdata/GPi2C"
fi


if [ ! -d /userdata/system/services ];
        then
                mkdir /userdata/system/services
                echo "Creating directory /userdata/system/services"
fi

#Configure variables--------------------------------------------
sleep 2s
script=/userdata/GPi2C/GPic2SS.py
scriptDS=/userdata/GPi2C/GPic2DS.py
controller=/userdata/system/configs/emulationstation/es_input.cfg
es_settings=/userdata/system/configs/es_settings.cfg
SERVICE=/userdata/system/services/GPic2SS
SERVICEDS=/userdata/system/services/GPic2DS

#Remove old files--------------------------------------------------
if [ -f $es_settings ];
        then
                rm $es_settings
fi
if [ -f $script ];
        then
                rm $script
fi
if [ -f $scriptDS ];
        then
                rm $scriptDS
fi
if [ -f $controller ];
        then
                rm $controller
fi
if [ -f $SERVICE ];
        then
                rm $SERVICE
fi
if [ -f $SERVICEDS ];
        then
                rm $SERVICEDS
fi

#Download Python script and controller config----------------------------
echo "Downloading GPic2SS, GPic2DS Python script and controller config from $SourcePath"
wget -O $script "$SourcePath/GPic2SS.py"
wget -O $scriptDS "$SourcePath/GPic2DS.py"
wget -O $controller "$SourcePath/es_input.cfg"



#Create Batocera Service (custom.sh is deprecated since v38)----------
sleep 2s
echo "Creating Batocera service for GPic2SS and GPic2DS"
wget -O $SERVICE "$SourcePath/GPic2SS"
wget -O $SERVICEDS "$SourcePath/GPic2DS"
chmod +x $SERVICE
echo "Service GPic2SS configured, GPic2DS installed."



#Enable the service--------------------------------------------------

batocera-services enable GPic2SS
sleep 2s
#Reboot-----------------------------------------------------------

echo "GPi case 2 Safe Shutdown service installation done. Will now reboot after 3 seconds."
sleep 3
shutdown -r now
#-----------------------------------------------------------
