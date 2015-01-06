#!/usr/bin/python
# -*- coding=utf-8 -*-

import re
import sys
import os
import subprocess

def fetch_text(text):
    text_re = re.compile(r'[\w_\-.]+')
    return text_re.search(text).group()

def check_result(result_text):
    lost_re = re.compile(r'(\d{1,3})% packet loss')
    lost_result = lost_re.search(result_text)
    if lost_result.group(1) == '0':
        avg_re = re.compile(r'\/(\d{1,3}\.\d{3})')
        avg_result = avg_re.search(result_text)
        delay = float(avg_result.group(1))
        return delay
    return False

def do_ping_test(ipaddr):
    try:
        result = subprocess.check_output(['ping', '-c 5', ipaddr])
        return check_result(result)
    except subprocess.CalledProcessError, er:
        return False

