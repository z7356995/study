#!/usr/bin/python
# -*- coding=utf-8 -*-

import re
import sys
import os
import subprocess
import random
import Queue
import threading
import time

import ip_getter
import ip_ping_checker
import ssl_info_checker

k_max_thread_count = 30

class Ip():
    def __init__(self, addr, delay):
        self.delay = delay
        self.addr = addr

    def info(self):
        return (self.addr, self.delay)

    def __cmp__(self, other):
        return cmp(self.delay, other.delay)

ip_scope_re_mode = r'(\d{1,3})-(\d{1,3})'
ip_scope_re = None
def get_random_ip_from_list(ip_list):
    global ip_scope_re
    if not ip_scope_re:
        ip_scope_re = re.compile(ip_scope_re_mode)

    random_index = random.randrange(0, len(ip_list))
    current_ip_range = ip_list[random_index]
    scope_result = ip_scope_re.search(current_ip_range)
    lower_bound = scope_result.group(1)
    upper_bound = scope_result.group(2)

    random_forth_part = random.randrange(int(lower_bound), int(upper_bound))
    last_dot_index = current_ip_range.rfind('.')

    return current_ip_range[:last_dot_index+1] + str(random_forth_part)

def do_test(addr, result_queue):
    delay = ip_ping_checker.do_ping_test(addr)
    if delay:
        if ssl_info_checker.ssl_check(addr):
            print '%s found!' % addr
            result_queue.put(Ip(addr, delay)) 
    return

def run(target_amount):
    if target_amount < 1:
        target_amount = 10

    ip_list = ip_getter.read_from_file()
    if len(ip_list) < 1:
        return

    result_queue = Queue.PriorityQueue()
    while(result_queue.qsize() < target_amount):
        cur_ip = get_random_ip_from_list(ip_list)
        print 'checking %s...' % cur_ip
        threading.Thread(target=do_test, args=(cur_ip, result_queue)).start()
        while(threading.active_count() > k_max_thread_count):
            time.sleep(2)

    while(threading.active_count() > 1):
        time.sleep(2)
    
    result_list = []
    while not result_queue.empty():
        c_ip = result_queue.get()
        c_info = c_ip.info()
        result_list.append(c_info[0])
        print "ip:%s delay:%d" % (c_info[0], c_info[1])

    for i in result_list:
        sys.stdout.write(i+'|')

if __name__ == '__main__':
    ip_amount = 20
    if len(sys.argv) > 1:
        ip_amount = int(sys.argv[1])
    run(ip_amount)
