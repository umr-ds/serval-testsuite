#! /bin/bash
if [ "$1" = "-h" ]; then
    echo "usage: $0 [...]"
    echo "watches servald on every miniworld node, and fires errors"
fi

NODE_CNT=`find /tmp/MiniWorld/ 2> /dev/null | grep "qemu.*sock" | wc -l`

SSH_OPTIONS="-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=QUIET -o User=root"

sudo ifconfig miniworld_tap 172.21.254.1

NODE_CNT_MOD=$(($NODE_CNT/4))
LINES=$(tput lines)
LINES_TO_FILL=$(($LINES - $NODE_CNT_MOD - 3))
while true; do
    OUTPUT=""
    for N in `seq 0 $NODE_CNT_MOD`; do
	N_new=$(($N*4))
        for i in `seq 1 4`;do
            CUR_NODE=$(($N_new+$i))
            if [ $CUR_NODE -le 64 ]; then
                NODE="172.21.0.$CUR_NODE"
                CUR_FILE_CNT=$(ssh $SSH_OPTIONS $NODE ". .profile; servald rhizome list | grep :file: | wc -l")
                if [ $CUR_NODE -le 9 ];then
                    CUR_OUTPUT=" $CUR_NODE:  ["
                else
                    CUR_OUTPUT=" $CUR_NODE: ["
                fi
                for n in `seq 1 $CUR_FILE_CNT`; do
                    CUR_OUTPUT+="|"
                done
                spaces=$((5-$CUR_FILE_CNT))
                for n in `seq 1 $spaces`; do
                    CUR_OUTPUT+=" "
                done
                CUR_OUTPUT+="]        "
                OUTPUT+="$CUR_OUTPUT"
            fi
        done
        OUTPUT+="\n"
    done
    for i in `seq 1 $LINES_TO_FILL`; do
        OUTPUT+="\n"
    done
    echo -e "$OUTPUT"
done

