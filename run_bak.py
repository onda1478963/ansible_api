#!/usr/bin/env python3
# -*- coding: utf8 -*-
from flask import Flask
from ansible_api import MyApi


app = Flask(__name__)

@app.route('/run')
def run_ansible():
    host='webserver'
    api = MyApi(host)
    # api = MyApi(<hostfile>)

    # 执行 Ad-hoc
    api.run(host, 'command', 'ls /')

    # 执行 playbook
    # api.run_playbook(<host>, <playbookfile>)

    # 获取返回值
    api.get_result()    # 字典
    api.get_json()      # json


    # hosts 文件格式

    # - ini
    # [group1]
    # host1   ansible_ssh_host = xxx.xx.xx.xxx





if __name__ == '__main__':
    app.run()





