import requests
from bs4 import BeautifulSoup as scrapper
import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = 'https://chatroll.com/embed/chat/anonymous-group-chat-room?name=anonymous-group-chat-room'
content = {0: 'test'}


def base_soup():
    response = requests.get(url)
    soup = scrapper(response.content, 'html.parser')
    for script in soup(['script', 'style']):
        script.extract()
    chats = soup.findAll('div', {'class': 'message-content'})
    return chats

def login_conf():
    cookies = {
        #'__ctma': 'Fj-z-aQj4xk',
        #'_ga': 'GA1.2.1322460418.1591191908',
        #'_gid': 'GA1.2.1520026789.1591191908',
        #'JSESSIONID': '1r0qpw48z5pcvglqd8f9zyikw3539200',
        '_ga': '1'
    }

    headers = {
        'Host': 'chatroll.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'text/plain',
        'Content-Length': '2104',
        'Origin': 'https://chatroll.com',
        'Connection': 'close',
        'Referer': 'https://chatroll.com/embed/chat/anonymous-group-chat-room?name=anonymous-group-chat-room',
        'Cache-Control': 'max-age=0',
    }

    data = {
    
    'callCount': '1',
    'page': '/embed/chat/anonymous-group-chat-room?name=anonymous-group-chat-room',
    #'httpSessionId': '1r0qpw48z5pcvglqd8f9zyikw3539200',
    #'scriptSessionId': 'B88DE1FB298327ABA8ECC6C34088BCD7410',
    'c0-scriptName': 'ServiceInterface',
    'c0-methodName': 'connect',
    'c0-id': '0',
    'c0-e1': 'string:4b3d6484d732f05e',
    'c0-e2': 'boolean:true',
    'c0-e3': 'string:https%3A%2F%2Fd167qii8h0pw75.cloudfront.net',
    'c0-e4': 'string:https%3A%2F%2Fdw3mgzt87vzb4.cloudfront.net%2Fclient%2F32a5c8c6',
    'c0-e5': 'string:https%3A%2F%2Fchatroll.com',
    'c0-e6': 'number:0',
    'c0-e7': 'boolean:true',
    'c0-e8': 'boolean:true',
    'c0-e9': 'string:15760828052',
    'c0-e10': 'string:ezcJWzDHi91',
    'c0-e12': 'boolean:true',
    'c0-e13': 'boolean:true',
    'c0-e14': 'boolean:true',
    'c0-e15': 'boolean:true',
    'c0-e16': 'boolean:true',
    'c0-e11': 'Object_Object:{twitter:reference:c0-e12, facebook:reference:c0-e13, guest:reference:c0-e14, sso:reference:c0-e15, chatroll:reference:c0-e16}',
    'c0-e19': 'boolean:false',
    'c0-e20': 'boolean:true',
    'c0-e18': 'Object_Object:{5:reference:c0-e19, 100:reference:c0-e20}',
    'c0-e21': 'null:null',
    'c0-e23': 'boolean:true',
    'c0-e24': 'boolean:true',
    'c0-e25': 'boolean:false',
    'c0-e26': 'boolean:false',
    'c0-e27': 'boolean:false',
    'c0-e28': 'boolean:true',
    'c0-e29': 'boolean:true',
    'c0-e30': 'boolean:true',
    'c0-e31': 'boolean:true',
    'c0-e32': 'boolean:true',
    'c0-e33': 'boolean:false',
    'c0-e22': 'Object_Object:{0:reference:c0-e23, 1:reference:c0-e24, 4:reference:c0-e25, 5:reference:c0-e26, 6:reference:c0-e27, 7:reference:c0-e28, 8:reference:c0-e29, 9:reference:c0-e30, 11:reference:c0-e31, 12:reference:c0-e32, 13:reference:c0-e33}',
    'c0-e34': 'Array:[]',
    'c0-e35': 'string:online',
    'c0-e17': 'Object_Object:{features:reference:c0-e18, groupUser:reference:c0-e21, permissions:reference:c0-e22, products:reference:c0-e34, status:reference:c0-e35}',
    'c0-e36': 'string:en',
    'c0-e37': 'number:-330',
    'c0-param0': 'Object_Object:{authChallenge:reference:c0-e1, autoConnect:reference:c0-e2, baseImagesUrl:reference:c0-e3, baseStaticUrl:reference:c0-e4, baseWebUrl:reference:c0-e5, contactListPosition:reference:c0-e6, defaultSoundOn:reference:c0-e7, embedded:reference:c0-e8, fbAppId:reference:c0-e9, groupId:reference:c0-e10, groupSigninMethods:reference:c0-e11, groupUserState:reference:c0-e17, language:reference:c0-e36, timezoneOffset:reference:c0-e37}',
    'batchId': '1'

    }
    response = requests.post('https://chatroll.com/service/call/plaincall/ServiceInterface.connect.req', headers=headers, cookies=cookies, data=data)
    return response.content

def main():
    iterator = 1
    while True:
        
        chats = base_soup()
        if iterator < 2:
            login_conf()
            for chat in chats:
                print(bcolors.OKBLUE + ''.join(chat.text).strip() + bcolors.ENDC)
                time.sleep(1)
        last_div = None
        for last_div in chats:
            pass

        if last_div:
            content[iterator] = last_div.getText()
            if content[iterator-1] != content[iterator]:
                print(bcolors.OKGREEN + ''.join(content[iterator]).strip() + bcolors.ENDC)

            else:
                pass

        iterator+=1


if __name__ == "__main__":
    try:    
        if sys.argv[1] == "-v":
            print('Scrap Chat (part B) v0.1')
    except:
        main()