#!/usr/bin/env python

import argparse
import mmap
import os
import re
import sys
import glob

class colors:
  RED='\033[91m'
  GREEN='\033[92m'
  END='\033[0m'

def run_is_complete(run_folder):
  result=True
  nodes=glob.glob(run_folder + "/qemu*.sid")
  contents=glob.glob(run_folder + "/*")
  dirs=filter(os.path.isdir, contents)

  if len(os.listdir(run_folder)) <= 4:
    print colors.RED + run_folder + colors.END
    print "Contains only " + str(len(os.listdir(run_folder))) + " elements: " + ", ".join(os.listdir(run_folder))
    result=False
  for dir in dirs:
    if not os.path.basename(os.path.normpath(dir)) in ["active", "err-log", "pidstat", "netmon"] and len(nodes) != len(os.listdir(dir)):
      if result:
        print colors.RED + run_folder + colors.END
      print "There are elements missing in " + dir + ": got " + str(len(os.listdir(dir))) + ", expected - " + str(len(nodes))
      result=False
  return result

def search_folder(folder, depth, complete):
  dirs=glob.glob(folder + "/*" * (depth))
  incomplete_count=0
  complete_runs=[]
  for dir in dirs:
    if not run_is_complete(dir):
      incomplete_count += 1
    elif complete:
      complete_runs.append(dir)
  print (colors.RED if incomplete_count > 0 else colors.GREEN) + str(incomplete_count) + "/" + str(len(dirs)) + " runs incomplete" + colors.END + "\n"
  if complete:
    print "\n".join(complete_runs)
    print colors.GREEN + str(len(complete_runs)) + "/" + str(len(dirs)) + " runs complete" + colors.END + "\n"

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("folder", help="the log folder to analyze")
  parser.add_argument("depth", type=int, help="the relative depth of the run folders")
  parser.add_argument("--complete", help="also show all completed runs", action="store_true")
  return parser.parse_args()
  
if __name__=='__main__':
  args=parse_args()
  search_folder(**vars(args))
