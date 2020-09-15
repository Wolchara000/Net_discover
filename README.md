# SIMPLE PYTHON Net Discover

For this to work you need to install scapy module (https://scapy.readthedocs.io/en/latest/)

```
pip install --pre scapy[basic]
```

How to use:
```
Usage: net_discover.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET, --target=TARGET
                        Specify the target or range in format IP/mask
```

Usage example:
```
python3 net_discover.py -t 192.168.1.1/24

############### Simple Net_Discover by Wolchara000 ###############
IP                      MAC address                     STATUS
--------------------------------------------------------------------
192.168.1.1             60:38:e0:79:c4:d9               HOST IS UP
192.168.1.117           9c:b6:d0:6c:f8:47               HOST IS UP
192.168.1.121           00:15:5d:01:8a:2e               HOST IS UP
192.168.1.138           04:92:26:d7:39:9a               HOST IS UP
192.168.1.118           9c:e3:3f:d0:56:5f               HOST IS UP
192.168.1.113           3c:6a:a7:82:2e:77               HOST IS UP
192.168.1.122           68:ec:c5:4b:73:64               HOST IS UP
192.168.1.142           68:ec:c5:4b:73:64               HOST IS UP
192.168.1.110           9c:b6:d0:6d:6c:9f               HOST IS UP
192.168.1.114           9c:b6:d0:6d:6c:9f               HOST IS UP
192.168.1.130           f8:87:f1:71:4b:2e               HOST IS UP
192.168.1.119           24:fd:52:a1:78:e3               HOST IS UP
192.168.1.106           64:eb:8c:87:c2:12               HOST IS UP

```

This program discovers live hosts in the network by using ARP ping method.
