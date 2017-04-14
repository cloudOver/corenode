#!/usr/bin/python

"""
Copyright (C) 2014-2017 cloudover.io ltd.
This file is part of the CloudOver.org project

Licensee holding a valid commercial license for this software may
use it in accordance with the terms of the license agreement
between cloudover.io ltd. and the licensee.

Alternatively you may use this software under following terms of
GNU Affero GPL v3 license:

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version. For details contact
with the cloudover.io company: https://cloudover.io/


This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.


You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import django
import os
import sys
import random
import subprocess

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corenode.settings")
django.setup()

from corenetwork.driver_interface import DriverInterface

drivers = DriverInterface.get_all_drivers()


hook_type = sys.argv[1]

name = sys.argv[2]
action = sys.argv[3]
state = sys.argv[4]

if hook_type == 'qemu':
    if action == 'prepare':
        for driver in drivers:
            driver.prepare_vm(name)
    elif action == 'started':
        for driver in drivers:
            driver.startup_vm(name)
    elif action == 'release':
        for driver in drivers:
            driver.release_vm(name)

elif hook_type == 'network':
    if action == 'start':
        for driver in drivers:
            driver.start_network(name)
    elif action == 'stopped':
        for driver in drivers:
            driver.stop_network(name)
