#!/usr/bin/env python3

import asyncio
import concurrent.futures
import logging
import sys
import time
from netmiko import ConnectHandler
from pprint import pprint

from my_devices import device_list
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


 
def blocks(device):
    pprint(device['host'])
    log = logging.getLogger('blocks({})'.format(device['host']))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    # cisco = {'device_type': 'cisco_ios', 'host': ip, 'username': '', 'password': 'cisco'}
    output = 'connection failed'
    try:
        print('here')
        net_connect = ConnectHandler(**device)
        # net_connect.send_command("uname -r")
        print('here')
        time.sleep(5)
        output = net_connect.send_command("show run")
        print('here')
        print(output)
    except:
        pass
    return output
 
 
async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')
    # hosts = [('192.168.10.4'), ('192.168.10.253')]
    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor, blocks, device)
        for device in device_list
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))
 
    log.info('exiting')
 
 
if __name__ == '__main__':
    # Configure logging to show the name of the thread
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )
 
    # Create a limited thread pool.
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=3,
    )
 
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()

