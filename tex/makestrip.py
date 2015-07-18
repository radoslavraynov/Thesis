#!/usr/bin/env python

import fileinput
from sys import argv

def strip(filename):
    filein = open(filename + "-incl.tex", 'w')
    ok_to_write = False
    for line in fileinput.input(filename + ".tex"):
        if line == "%% STRIP END\n":
            ok_to_write = True
            continue
        if line == "%% STRIP BEGIN\n":
            ok_to_write = False
            continue
        if ok_to_write:
            filein.write(line)

strip(argv[1])