#!/usr/bin/python3

import sys
import sniffer.py
import spoofer.py

def main(argv):
 Controller(sys.argv[0], sys.argv[1])

if __name__ == "__main__":
 main(sys.argv)

class Controller:
 self.bandwidth_limit
 self.penalty_time
 self.users = []

 def __init__(self, limit, penalty_time):
  self.bandwidth_limit = limit
  self.penalty_time = penalty_time



