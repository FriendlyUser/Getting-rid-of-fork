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


def _get_attach_msg(path):
    ''' make MIME type attachment message '''
    if not os.path.isfile(path):
        return
    # Guess the content type based on the file's extension.  Encoding
    # will be ignored, although we should check for simple things like
    # gzip'd or compressed files.
    ctype, encoding = mimetypes.guess_type(path)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        fp = open(path)
        # Note: we should handle calculating the charset
        msg = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'image':
        fp = open(path, 'rb')
        msg = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(path, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(path, 'rb')
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        encoders.encode_base64(msg)
    # Set the filename parameter
    msg.add_header('Content-Disposition', 'attachment', filename=path.split('/')[-1])
    return msg

def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

for mp3file in mp3gen():
    print(mp3file)
    msg.attach(_get_attach_msg(mp3file))

s.send_message(msg)