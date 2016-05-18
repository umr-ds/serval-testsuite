#!/usr/bin/env bash

NEW_BRIDGES=$1
source miniworld_event_hook_vars.sh

new_bridges=( $NEW_BRIDGES )

for new_bridge in ${new_bridges[@]}; do
    # start netmon for new bridge
    echo "./netmon.py $new_bridge >> /tmp/netmon_$new_bridge.csv &" >> $MINIWORLD_EVENT_HOOK_LOG
    ./netmon.py $new_bridge >> /tmp/netmon_$new_bridge.csv &
    PID=$!
    # store netmon pids
    echo " $PID" >> $NETMON_PIDS

done
