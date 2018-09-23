#!/bin/python3
import pexpect

child = pexpect.spawn('telnet 172.16.1.20')
child.expect('Username')
child.sendline('cisco')
child.expect('Password')
child.sendline('cisco')
child.expect('iosv-1#')
child.sendline('show version | i V')
child.expect('iosv-1#')