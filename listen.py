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

url = 'https://chatroll.com/embed/chat/anonymous-group-chat-room?name=anonymous-group-chat-room'

def base_soup():
    response = requests.get(url)
    soup = scrapper(response.content, 'html.parser')
    for script in soup(['script', 'style']):
        script.extract()
    chats = soup.findAll('div', {'class': 'message-content'})
    return chats

def main():
    chats = base_soup()
    for chat in chats:
        print(bcolors.OKBLUE + ''.join(chat.text).strip() + bcolors.ENDC)

    premsg = ''
    while True:
        chat = base_soup()
        try:
            content = chat[len(chat)-1]
            timestamp = content.find('div', {'class': 'message-timestamp'})
            name = content.find('span', {'class': 'message-profile-name'})
            msg = content.find('span', {'class': 'message-text'})
        except IndexError:
            continue
        except Exception:
            break
        if premsg != msg:
            c1 = bcolors.WARNING
            if name.text == ' (Guest)':
                c2 = bcolors.FAIL
                c3 = bcolors.OKBLUE
            else:
                c2 = bcolors.HEADER
                c3 = bcolors.OKGREEN
            print(c1 + ''.join(timestamp.text).strip() + bcolors.ENDC)
            print(c2 + ''.join(name.text).strip() + ': ' + bcolors.ENDC + \
            c3 + ''.join(msg.text).strip() + bcolors.ENDC)
            premsg = msg

if __name__ == "__main__":
    try:
        if sys.argv[1] == "-v":
            print('Scrapchat v1.0')
    except Exception:
        main()