###########################################
############# SECURE STMP EMAILING #####
###########################################
# https://gist.github.com/elprup/3205948
import time
import smtplib
import mimetypes
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase

# Try again later lol
import os
if os.environ.get('GMAIL_USER') is not None:
    email_from = os.environ.get("GMAIL_USER")
    email_pass = os.environ.get("GMAIL_PASS")
    email_to = os.environ.get("GMAIL_TO")

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(email_from, email_pass)
# s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
tmmrDate = (time.strftime("%m/%d/%Y",time.localtime()))
msg = MIMEMultipart()       # create a message
 # setup the parameters of the message
msg['From']=email_from
msg['To']=email_to
msg['Subject']="Sending Video %s" % tmmrDate

def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

for mp3file in mp3gen():
    fp = open(mp3file, 'rb')                                                    
    vid = MIMEAudio(fp.read())
    fp.close()
    vid.add_header('Content-ID', '<' +mp3file + '>')
    msg.attach(vid)

s.send_message(msg)