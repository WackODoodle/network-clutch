#!/usr/bin/python3

import sys
import sniffer
from spoofer import Spoofer


class Controller:
    def testSpoofer(self):
        testspoofer = Spoofer("test")
        testspoofer.disassociate("test")

    def __init__(self, limit, penalty_time):
        self.bandwidth_limit = limit
        self.penalty_time = penalty_time
        self.testSpoofer()


def main(argv):
    Controller(sys.argv[0], sys.argv[1])


if __name__ == "__main__":
    main(sys.argv)
