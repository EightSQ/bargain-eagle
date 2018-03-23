import os
from dotenv import load_dotenv
import time
from subprocess import Popen, PIPE

load_dotenv('.env')
FROM = os.getenv('MY_MAIL')
TO = os.getenv('TO_MAIL')

def mail(offers):
    subject = 'Bargain-Eagle Report ' + time.strftime('%m/%d')
    msg = 'I found interesting listings this week!\n\n'
    for offer in offers:
        msg += str(offer)+'\n'
    msg += '\nHave a nice day!'
    sendMail(FROM, TO, subject, msg)

def sendMail(from_addr, to_addr, subject, body):
    try:
        p = Popen(['mail', '-r', from_addr, '-s', subject, to_addr], stdin=PIPE)
        p.communicate(bytes(body, encoding='utf-8'))
    except Exception as e:
        print(e)
