# coding: utf-8
'''
win_device.py
在 Windows 上获取窗口名称
by: @wyf9
依赖: pywin32, requests
'''
import win32gui  # type: ignore
import requests
import time
import json

# --- config start
SERVER = 'http://152.32.188.131:9010'
SECRET = ''
CHECK_INTERVAL = 2
BYPASS_SAME_REQUEST = True
DEVICE_ID = 'device-1'
DEVICE_SHOW_NAME = '有栖的电脑'
# --- config end
RETRY = 3

def get(url):
    for t1 in range(RETRY):
        t = t1 + 1
        try:
            x = requests.get(url)
            return x.text
        except:
            print(f'Retrying... {t}/{RETRY}')
            if t >= RETRY:
                print('Max retry limit!')
                raise
            continue


def loadjson(url):
    raw = get(url)
    try:
        return json.loads(raw)
    except json.decoder.JSONDecodeError:
        print('Error decoding json!\nRaw data:\n"""')
        print(raw)
        print('"""')
        raise
    except:
        print('Error:')
        raise


def main():
    url = f'{SERVER}/device/set'
    last_window = ''
    while True:
        use = True
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        stnow = loadjson(f'{SERVER}/query')
        if(stnow["status"] == 1):
            window = '未在使用'
            use = False
        elif(window == ''):
            window = '系统桌面'
            use = True
        print(f'--- Window: {window}')
        print(f'POST {url}')
        try:
            resp = requests.post(url=url, json={
                'secret': SECRET,
                'id': DEVICE_ID,
                'show_name': DEVICE_SHOW_NAME,
                'using': use,
                'app_name': window
            }, headers={
                'Content-Type': 'application/json'
            })
            print(f'Response: {resp.status_code} - {resp.text}')
        except Exception as e:
             print(f'Error: {e}')
        '''
        if (BYPASS_SAME_REQUEST and window != last_window) or (not BYPASS_SAME_REQUEST):
            print(f'POST {url}')
            try:
                resp = requests.post(url=url, json={
                    'secret': SECRET,
                    'id': DEVICE_ID,
                    'show_name': DEVICE_SHOW_NAME,
                    'using': True,
                    'app_name': window
                }, headers={
                    'Content-Type': 'application/json'
                })
                print(f'Response: {resp.status_code} - {resp.text}')
            except Exception as e:
                print(f'Error: {e}')
            last_window = window
        else:
            print('window not change, bypass')
        '''
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()
