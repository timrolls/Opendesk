#!/usr/bin/python

import re
import sys

n=0.0
com = [0.0,0.0]
pgn = []

for line in sys.stdin:
  line = line.strip()
  if len(line) == 0:
    if n>0:
      print com[0]/n, com[1]/n

    n=0
    com = [0.0,0.0]
    pgn=[]
    print line
    continue
  if line[0] == '#':
    print line
    continue

  parts = re.split('[ \t]*', line)

  com[0] += float(parts[0])
  com[1] += float(parts[1])
  n += 1.0

if n>0:
  print com[0]/n, com[1]/n

