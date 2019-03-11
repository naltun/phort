# Phort
### The Python + GNU/Linux Tor router CLI

_**Currently in beta!**_

#### What is it?
Phort is the Tor router CLI for Python + GNU/Linux. Phort is a one stop shop for configuring your device to routing all of its traffic through the Tor network. With a simple, intuitive command-line interface, Phort will help keep you anonymous and more secure on the Internet.

###### DISCLAIMER
Phort is a Python adaptation of [Nipe](https://github.com/GouveaHeitor/nipe). Nipe is a wonderful piece of software written by [Heitor Gouvêa](https://github.com/GouveaHeitor).

#### HOWTO
This is subject to change.
```bash
$ python3 phort.py <command>

$ python3 phort.py help
Phort v0.1beta
The Python + GNU/Linux Tor router CLI

Command         Description
-------   -----------------------
setup     Set up your environment
start     Starts Tor routing
stop      Stops Tor routing
restart   Restarts Phort
status    Shows connection status
help      Shows help message

Developed by Noah Altunian (github.com/naltun)
Adapted from Nipe (github.com/GouveaHeitor/nipe)
Source code subject to the terms of the Mozilla Public License, v. 2.0
```

#### Installation
###### Requirements
* requests 2.21.0

###### Installing
Simply execute `pip install -r requirements.txt` in the `phort` top-level directory.

#### License
Love your Free/Libre Software. Phort is subject to the terms of the Mozilla Pubic License, v. 2.0.

For more information on the MPL, or if a copy was not distributed with this file, please visit [Mozilla](http://mozilla.org/MPL/2.0/).

For more information on Free/Open Source Software, please visit [Wikipedia](https://en.wikipedia.org/wiki/Free_software_movement).
