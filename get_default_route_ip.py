#!/usr/bin/env python
'''Example of getting gateway addr on Linux.'''

from __future__ import print_function

import subprocess


def main():
    print(get_gateway_addr())


def get_gateway_addr():
    ip_cmd_output = subprocess.check_output(
        ['ip', '-4', 'route', 'show', 'to', 'default']).strip()
    gateway_addr = ip_cmd_output.split()[2]
    return gateway_addr

if __name__ == '__main__':
    main()
