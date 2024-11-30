#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2013 Ole Martin Bjorndalen <ombdalen@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
List available PortMidi ports.
"""

import os

import mido


def print_ports(heading, port_names):
    print(heading)
    for name in port_names:
        print(f"    '{name}'")
    print()


def main():
    print_ports('Available input Ports:', mido.get_input_names())
    print_ports('Available output Ports:', mido.get_output_names())
    print(f'Using backend {mido.backend.name}.')


if __name__ == '__main__':
    main()
