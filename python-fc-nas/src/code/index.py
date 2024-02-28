#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import subprocess
import string
import os


def handler(event, context):
    # report file system disk space usage and check NAS mount target
    out, err=subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE).communicate()
    print('disk: ' + str(out))
    lines = [ l.decode() for l in out.splitlines() if str(l).find(':') != -1 ]
    nas_dirs = [ x.split()[-1] for x in lines ]
    print('uid : ' + str(os.geteuid()))
    print('gid : ' + str(os.getgid()))

    for nas_dir in nas_dirs:
        sub_dir = randomString(16)
        file_name = randomString(6)+'.txt'
        new_dir = nas_dir + '/' + sub_dir + '/'
        print('test file: ' + new_dir + file_name)
        # 写入NAS文件
        content = "NAS here I come"
        os.mkdir(new_dir)
        fw = open(new_dir + file_name, "w+")
        fw.write(content)
        fw.close()
        # Showing the folder tree in NAS
        for home, dirs, files in os.walk(nas_dir):
            level = home.replace(nas_dir, '').count(os.sep)
            indent = ' ' * 2 * (level)
            print('{}{}/'.format(indent, os.path.basename(home)))
            subindent = ' ' * 2 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
        # 读取NAS文件
        f = open(new_dir + file_name, "r")
        print(f.readline())
        f.close()
    
    return 'success'


def randomString(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))
  