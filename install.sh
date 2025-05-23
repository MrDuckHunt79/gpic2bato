#!/bin/bash

SourcePath=https://mrduckhunt79.github.io/gpic2bato/

#Remount FS as RW------------------------------------------------

sleep 2s
mount -o remount, rw /boot
mount -o remount, rw /

#Download Python script-----------------------------
mkdir /userdata/GPi2C
sleep 2s
script=/userdata/GPi2C/GPic2SS.py

wget -O  $script "$SourcePath/GPic2SS.py"


#Create Batocera Service (custom.sh is deprecated since v38)----------

sleep 2s
DIR=/userdata/system/services/GPic2SS

if grep -q "python $script &" "$DIR";
        then
                if [ -x "$DIR" ];
                        then
                                echo "Service GPic2SS configured. Doing nothing."
                        else
                                chmod +x $DIR
                fi
        else
                echo "python $script &" >> $DIR
                chmod +x $DIR
                echo "Service GPic2SS configured."
fi
#Reboot-----------------------------------------------------------

echo "GPi case 2 Safe Shutdown service installation done. Will now reboot after 3 seconds."
sleep 3
shutdown -r now
#-----------------------------------------------------------
