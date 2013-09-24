flower-pi
=========

An automation system for growing pants and flowers based on Raspberry Pi.


Requirements
-------------------------
* Raspberry Pi 
* Raspbian wheezy distribution
* Installed upstart
* Python packages: RPIO, astral, pytz


Installation
-------------------------

1. In order to install upstart the system must be up to date, so run:

        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install upstart
        
2. There is no need to install required python packages manually. The system
will install all required packages automatically.

        tar -xzf flower-pi-0.1.tar.gz
        cd flower-pi-0.1/
        sudo python setup.py install
        
        
Operation
-------------------------
FlowerPi runs as an upstart service at system start up.

It can be stopped:

        sudo service flower-pi stop

started:

        sudo service flower-pi start

restarted:

        sudo service flower-pi restart
  
or checked the status:

        sudo service flower-pi status
