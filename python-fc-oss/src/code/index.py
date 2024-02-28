# -*- coding: utf-8 -*-
import os


def handler(event, context):
    # 挂载目录
    mount_path = '/mnt/oss'
    
    # 列出挂载目录中的文件
    files = os.listdir(mount_path)
    print("Files in OSS mount:", files)  
    # 读取挂载目录中的某个文件
    file_path = os.path.join(mount_path, 'example.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print("Content of example.txt:", content)
    else:
        print("example.txt does not exist.")
    # 向挂载目录中写入文件
    write_path = os.path.join(mount_path, 'output.txt')
    with open(write_path, 'w') as file:
        file.write("Hello, OSS mount!")
        print("Wrote to output.txt in OSS mount.")
    
    return "Function execution completed."
  