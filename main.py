import imaplib
import email
from datetime import datetime
from time import sleep
import os
from helper import *

account = select_account('config.json')

imap_server = account['imap_server']
username = account['username']
password = account['password']
download_path = account['download_path']




last_message = None
email_message = {}


while True:
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)
    imap.select('INBOX')
    
    print('running...', last_message)
    _, message_ids = imap.search(None, 'ALL')
    if not message_ids[0]:
        last_message = 'empty'
        sleep(10)
        continue
    latest_message_id = message_ids[0].split()[-1]


    _, msg_data = imap.fetch(latest_message_id, '(RFC822)')

    raw_email = msg_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    message_id = email_message['Message-ID']
    if last_message == None:
        last_message = message_id
        sleep(10)
        continue
    elif last_message == 'empty':
        last_message = message_id
    elif last_message == message_id:
        sleep(10)
        continue

    timestamp = email_message['Date']
    filenames = []
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # Save the attachment
        filename = part.get_filename()
        if filename:
            unique_filepath = uniquify_file_path(os.path.join(download_path, filename))
            unique_filename = os.path.basename(unique_filepath)
            with open(unique_filepath, 'wb') as attachment_file:
                attachment_file.write(part.get_payload(decode=True))
            change_file_timestamp(unique_filepath, timestamp)
        filenames.append(unique_filename)
    if filenames:
        print(f"*** Attachments Downloaded ({timestamp}): {', '.join(filenames) }*** ")
    last_message = message_id
    imap.close()
    imap.logout()
    sleep(10)
