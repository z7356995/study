#!/usr/bin/python
# -*- coding=utf-8 -*-

import re

data_file = 'ip_list.dat'

ip_re_mode = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}-\d{1,3}'
ip_re = None
def parse_current_ip(line):
    try:
        global ip_re
        if not ip_re:
            ip_re = re.compile(ip_re_mode)
        return ip_re.search(line).group()
    except AttributeError, er:
        return None

def read_from_file():
    ip_list = []
    try:
        for line in open(data_file):
            cur_ip = parse_current_ip(line)
            if cur_ip:
                ip_list.append(cur_ip)
    except IOError, er:
        print "Error: ip_list.dat file not found!"
    return ip_list 

if __name__ == '__main__':
    ip_list = read_from_file()
    print ip_list

