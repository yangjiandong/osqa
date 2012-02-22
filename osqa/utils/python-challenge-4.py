#!/usr/bin/envs python
#-*- coding: utf-8 -*-#
import urllib, re, time

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing_rep = "and the next nothing is (\d+)"
nothing = "12345" # You'll later be asked to change this
                  # to "46059" and re-run the script.

while True:
    try:
        source = urllib.urlopen(uri % nothing).read()
        nothing = re.search(nothing_rep, source).group(1)
    except:
        break

    print nothing