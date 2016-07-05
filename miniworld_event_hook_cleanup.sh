#!/usr/bin/env bash

source miniworld_event_hook_vars.sh

# kill netmons
cat $NETMON_PIDS | xargs kill -9
rm $NETMON_PIDS
rm /tmp/netmon*
rm $MINIWORLD_EVENT_HOOK_LOG

