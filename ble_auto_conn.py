#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Stanley Wang

import pexpect
actions = [
    ('', '# ', 'starting'),
    ('power on', 'Changing power on succeeded', ''),
    ('discoverable on', 'Changing discoverable on succeeded', ''),
    ('connect B8:09:8A:F3:ED:FC', 'Connection succeedful', 'connecting keyboard'),
    ('connect E8:80:2E:E6:D6:0E', 'Connection succeedful', 'connecting touchpad'),
    ('connect 2C:41:A1:47:69:F5', 'Connection succeedful', 'connecting speaker'),
    ('exit', '', ''),
]

cmd = 'bluetoothctl'
print(f'Running cmd:{cmd}')
ctl = pexpect.spawn(cmd)
for action, expect, memo in actions:
    try:
        print(memo if memo else action)
        if action: ctl.sendline(action)
        if expect: idx = ctl.expect(expect, timeout=5)
    except pexpect.EOF:
        print("EOF")
    except pexpect.TIMEOUT:
        print("TIMEOUT")
ctl.close()

