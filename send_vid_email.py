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
    # fp = open(mp3file, 'rb')                                                    
    # vid = MIMEAudio(fp.read())
    # fp.close()
    # vid.add_header('Content-ID', '<' +mp3file + '>')
    # msg.attach(vid)
    
    ##### OTHER
    ctype, encoding = mimetypes.guess_type(mp3file)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    fileToSend = mp3file
    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    msg.add_header("Content-Disposition", "attachment", filename=fileToSend)

s.send_message(msg)