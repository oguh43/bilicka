from __future__ import print_function
import httplib2
import os
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from httplib2 import Http
from email import encoders
from apiclient import errors
from datetime import date
from apiclient.discovery import build
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
credentials = get_credentials()
service = build('gmail', 'v1', http=credentials.authorize(Http()))

def send_message(service, user_id, message):
  try:
    message = service.users().messages().send(userId=user_id, body=message).execute()

    print('Message Id: %s' % message['id'])

    return message
  except Exception as e:
    print('An error occurred: %s' % e)
    return None


def create_message_with_attachment(sender, to, subject, message_text, file):
  message = MIMEMultipart()
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject

  msg = MIMEText(message_text)
  message.attach(msg)

  content_type, encoding = mimetypes.guess_type(file)

  if content_type is None or encoding is not None:
    content_type = 'application/octet-stream'

  main_type, sub_type = content_type.split('/', 1)

  if main_type == 'text':
    fp = open(file, 'rb')
    msg = MIMEText(fp.read().decode("utf-8"), _subtype=sub_type)
    fp.close()
  elif main_type == 'image':
    fp = open(file, 'rb')
    msg = MIMEImage(fp.read(), _subtype=sub_type)
    fp.close()
  elif main_type == 'audio':
    fp = open(file, 'rb')
    msg = MIMEAudio(fp.read(), _subtype=sub_type)
    fp.close()
  else:
    fp = open(file, 'rb')
    msg = MIMEBase(main_type, sub_type)
    msg.set_payload(fp.read())
    #
    encoders.encode_base64(msg)
    fp.close()
  filename = os.path.basename(file)
  msg.add_header('Content-Disposition', 'attachment', filename=filename)
  message.attach(msg)

  #raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
  #return {'raw': raw_message.decode("utf-8")}
  return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


today = date.today()
dte = today.strftime("%d.%m.%Y")

teacher = ["Hugo Bohácsek","Jana Manczálová","Iveta Rybárová"]
adr = ["agenthugo43@gmail.com","s.bohacsekova@cartv.eu","agentzoja43@gmail.com"]
sub_a = ["Informatika","Fyzika","Matematika"]
sub = ["Informatiky","Fyziky","Matematiky"]
r = 0
for i in teacher:
  r+=1
  print(r,") ",i, sep="")
who = int(input("Číslo vybraného učiteľa: "))-1
file_name = "%s_uloha.docx" %sub_a[who].lower()
a = "Riešenie príkladov z %s" %sub[who]
b = "Dobrý deň,\nPosielam vám vypracované úlohy z %s.\nHugo Bohácsek, Ki.B %s" %(sub[who],dte)

mine = create_message_with_attachment("hugo.bohacsek@gmail.com",adr[who],a,b,file_name)
testSend = send_message(service, 'me', mine)