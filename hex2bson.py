#!/usr/bin/env python
# hex2bson.py
import binascii
import bson
import sys
import pprint
while True:
    line = sys.stdin.readline()
    if not line:
        print("No data section")
        sys.exit(1)
    line = line.strip()
    if line == 'Data':
        break
while True:
    key = sys.stdin.readline()
    if not key:
        break
    key = key.strip()
    value = sys.stdin.readline().strip()
    print('Key:\t0x%s / Possible Rid: %d' % (key.upper(), int(key, 16) - 49088))
    byt = binascii.a2b_hex(value)
    obj = bson.decode(byt)
    print('Value:\n\t%s' % (pprint.pformat(obj, indent=1).replace('\n', '\n\t'),))

