# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import os.path
import requests

#############
# VARIABLES #
#############

api = 'https://check.torproject.org/api/ip'
helpMsg = """Phort v0.1beta
The Python + GNU/Linux Tor router CLI

Command         Description
-------   -----------------------
setup     Set up your environment
start     Starts Tor routing
stop      Stops Tor routing
restart   Restarts Phort
status    Shows connection status

Developed by Noah Altunian (github.com/naltun)
Adapted from https://github.com/GouveaHeitor/nipe
Licensed under the terms of the Mozilla Public License 2.0
"""

#############
# FUNCTIONS #
#############

def checkConn():
    """Checks to see if the device's IP address is tunneled through Tor.
    checkip will return the device's Tor connection status and IP address.
    """
    
    req = requests.get(api)
    if req.status_code == requests.codes.ok:
        json = req.json()
        if json['IsTor']:
            print("\033[1;32m[*]\033[1;37m Connected: {}".format(json['IsTor']))
            print("\033[1;32m[*]\033[1;37m IP: {}\033[0m".format(json['IP']))
        else:
            print("\033[0;31m[!]\033[1;37m Connected: {}".format(json['IsTor']))
            print("\033[0;31m[!]\033[1;37m IP: {}\033[0m".format(json['IP']))

    else:
        print('\033[31m[!]\033[1;37m ERROR: sorry, it was not possible to establish a connection to the server.\033[0m')


def cli():
    """Handles Phort's CLI interface."""
    
    pass


def createEnv():
    """Creates the user's phort environment by interacting with the user's
    operating system. This method is invoked via the 'setup' CLI command.
    """
    
    opsys = getOpSys()
    print("Setting up environment...\nMaking /etc/tor")
    os.system('sudo mkdir -p /etc/tor')
    if opsys == 'arch':
        os.system('sudo pacman -S tor iptables')
        os.system('sudo cp ../config/arch-torrc /etc/tor/torrc')
    elif opsys == 'centos':
        os.system('sudo yum install epel-release tor iptables')
        os.system('sudo cp ../config/centos-torrc /etc/tor/torrc')
    elif opsys == 'debian':
        os.system('sudo apt install tor iptables')
        os.system('sudo cp ../config/debian-torrc /etc/tor/torrc')
    elif opsys == 'fedora':
        os.system('sudo dnf install tor iptables')
        os.system('sudo cp ../config/fedora-torrc /etc/tor/torrc')
    else:
        print('Unknown operating system. Exiting')
        exit(1)
    
    os.system('sudo chmod 644 /etc/tor/torrc')
    


def getOpSys():
    """Determines which Linux OS the user is using. This function will be used
    elsewhere in Phort.
    """
    
    opsys = os.popen("awk -F= '$1==\"ID_LIKE\" { print $2 ;}' /etc/os-release").read().rstrip()
    if opsys == 'Archlinux' or opsys == 'archlinux':
        return 'arch'
    elif opsys == 'Centos' or opsys == 'centos':
        return 'centos'
    elif opsys == 'Debian' or opsys == 'debian' or opsys == 'Ubuntu' or opsys == 'ubuntu':
        return 'debian'
    elif opsys == 'Fedora' or opsys == 'fedora':
        return 'fedora'
    else:
        print('Unknown operating system. Exiting')
        exit(1)


def getUser():
    """Determines which Linux OS the user is using. This function will be used
    elsewhere in Phort.
    """
    
    opsys = os.popen("awk -F= '$1==\"ID_LIKE\" { print $2 ;}' /etc/os-release").read().rstrip()
    if opsys == 'Archlinux' or opsys == 'archlinux':
        return 'tor'
    elif opsys == 'Debian' or opsys == 'debian':
        return 'debian-tor'
    elif opsys == 'Fedora' or opsys == 'fedora' or opsys == 'Centos' or opsys == 'centos':
        return 'toranon'
    elif opsys == 'Ubuntu' or opsys == 'ubuntu':
        return 'tor'
    else:
        return 'tor'


def help():
    """Prints Phort's help message to standard output."""
    
    print(helpMsg)    


def start():
    """Starts Phort's tunneling through Tor."""
    
    pass


def stop():
    """Stops Phort's tunneling through Tor."""
    
    tables = ['nat', 'filter']
    for table in tables:
        os.system("sudo iptables -t {} -F OUTPUT".format(table))

    if os.path.isfile('/etc/init.d/tor'):
        os.system('sudo /etc/init.d/tor stop > /dev/null')
    else:
        os.system('sudo systemctl stop tor')
    
    # return true
