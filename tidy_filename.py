#!/usr/bin/python

import sys
import re

padding = 3
prefix = "qemu"
if len(sys.argv) == 1:
    print("Usage: %s <logfilename> [padding] [prefix]" % sys.argv[0])
    printf(" Default padding = 3 digits")
    printf(" Default prefix = 'qemu'")
    sys.exit(1)
elif len(sys.argv) == 3:
    padding = int(sys.argv[2])

if len(sys.argv) == 4:
    prefix = sys.argv[3]

orig_fname = sys.argv[1]

m = re.search("(%s[0-9]+)" % prefix, orig_fname)
if m:
    number = int(m.group(0)[len(prefix):])
    newnumber = format(number, "0%d" % padding)
    new_fname = orig_fname.replace(prefix+str(number), prefix+newnumber)
    print new_fname
else:
    print orig_fname
