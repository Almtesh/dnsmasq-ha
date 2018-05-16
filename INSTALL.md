# INSTALLATION GUIDE

This document will explain, step by step, how to install the program.

## Depends

This program requires the Python interpretor, at least version 3.0, to be available in the PATH.  
You also need to install the dnsmasq program and define (if needed because not in default `/opt/sbin/dnsmasq`) the complete path in the configuration.

## Installation

Once the depends installed, you must install the `dnsmasq-ha` folder in `/opt/`.

## Configuration

Use the configuration the example configuration in `etc/dnsmasq-ha.ini` to build you own one.

__IMPORTANT NOTICE__: please generate a proper secret with return of `dd if=/dev/random bs=32 count=1 | base64` or your own secret passphrase.

Once you've put the same configuration on every node of the cluster, put you dnsmasq configuration in `etc/dnsmasq` folder or in the path you can define in the dnsmasq-ha's configuration.