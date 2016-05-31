#!/usr/bin/env python

from __future__ import print_function
import argparse
import mmap
import os
import re
import sys

def parameterlist_is_valid():
  return len(sys.argv) == 2

def search_folder(folder, depth):
  for subdir, dirs, files in os.walk(folder):
    for dir in dirs:
      dirpath=os.path.join(subdir, dir)
      if len(os.listdir(dirpath)) == 4:
        print(dirpath)
    if subdir[len(folder) + len(os.path.sep):].count(os.path.sep) == depth:
      break

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("folder", default=argparse.SUPPRESS)
  parser.add_argument("-f", "--folder", dest="folder")
  parser.add_argument("depth", type=int)
  return parser.parse_args()
  
if __name__=='__main__':
  args=parse_args()
  search_folder(**vars(args))
