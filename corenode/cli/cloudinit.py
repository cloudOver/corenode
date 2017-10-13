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

from corenetwork.cli.cli_base import CommandLineBase
from corenetwork.api_mixin import ApiMixin
from corenetwork.utils import config
import hashlib
import random
import sys

class Cmd(CommandLineBase):
    actions = {
        'get_userdata': {
            'help': 'List api functions',
        },
    }

    def get_userdata(self, vm_address):
        apim = ApiMixin()
        core_ip = apim._get_core_address()

        auth_seed = hashlib.sha256(str(random.random())).hexdigest()
        auth_hash = apim._calc_hash(config.get('node', 'AUTH_TOKEN'), auth_seed)
        sys.stdout.write("http://%s:8600/%s/%s/%s/" % (core_ip, auth_hash, auth_seed, vm_address))
