import os
import pandas as pd
##import ipaddress as IP_ADDR
ip_address = pd.read_csv('Ip_addr.csv')
processes = pd.read_csv('process.csv')
netstat = pd.read_csv('netstat.csv')
print(netstat.head(3))
print(ip_address.loc[ip_address['id'] == 'App1'])