#!/usr/bin/env python

from subprocess import check_output
import os
from pprint import pprint

os.system("./miniworld-execute-all /usr/bin/date +%s%3N | tail -n +2 | grep -v '# HOST' > qemu_dates.txt")

#times = check_output('./miniworld-execute-all /usr/bin/date +%s%3N | ')

with open("qemu_dates.txt", "r") as f:
	times = f.read()
	times = times.split("\n")[:-1]
	print "times from qemu nodes: \n%s" % times

def get_pairwise_time_diff():
	print "time diff:"
	pprint(map(lambda (cnt, (x, y)): ("%s,%s" % (cnt, cnt+1), int(y)-int(x)), enumerate(zip(times, times[1:]), 1)))

get_pairwise_time_diff()
