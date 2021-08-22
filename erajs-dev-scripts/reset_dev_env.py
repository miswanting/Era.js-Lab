import sys
from ctypes import windll
from os import link, remove
from os.path import exists
from shutil import rmtree
from threading import Thread
from time import sleep


def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


print('Era.js Development Environment Reset Script(EDEBS)')
print('Version: 0.1.0')
if exists('../erajs-frontend-web/node_modules/'):
    print('Remove Node Modules...', end='')
    rmtree('../erajs-frontend-web/node_modules/')
    print('OK')
if exists('../erajs-frontend-web/dist/'):
    print('Remove Dist...', end='')
    rmtree('../erajs-frontend-web/dist/')
    print('OK')
if exists('../erajs-frontend-web/npm.lock'):
    print('Remove yarn.lock...', end='')
    remove('../erajs-frontend-web/npm.lock')
    print('OK')
if exists('../erajs-frontend-web/yarn.lock'):
    print('Remove yarn.lock...', end='')
    remove('../erajs-frontend-web/yarn.lock')
    print('OK')
def aaa():
    # link('../erajs-backend/erajs', '../erajs-sdk/erajs')
    # sleep(10)
    pass

# if is_admin():
#     t = Thread(target=aaa)
#     t.start()
#     # sleep(10)
# else:
#     windll.shell32.ShellExecuteW(
#         None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#     # sleep(20)
