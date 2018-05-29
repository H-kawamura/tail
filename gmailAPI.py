# -*- coding: utf-8 -*-

from __future__ import print_function

import httplib2

import os

import base64

import email



from apiclient import discovery, errors

import oauth2client

from oauth2client import client

from oauth2client import tools



try:

    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

except ImportError:

    flags = None





class GmailClient(object):

    

    SCOPES = 'https://mail.google.com/'

    CLIENT_SECRET_FILE = 'client_secret.json'

    APPLICATION_NAME = 'Gmail Client'

    

    def __init__(self, **kwargs):

        if "user_id" in kwargs:

            self.user_id = user_id

        else:

            self.user_id = "me"



        credentials = self.credentials()

        http = credentials.authorize(httplib2.Http())

        self.service = discovery.build('gmail', 'v1', http=http)



    # Gmailの認証処理

    def credentials(self):

        home_dir = os.path.expanduser('~')

        credential_dir = os.path.join(home_dir, '.credentials')

        if not os.path.exists(credential_dir):

            os.makedirs(credential_dir)

        

        credential_path = os.path.join(credential_dir,

            'gmail-python-quickstart.json')



        store = oauth2client.file.Storage(credential_path)

        credentials = store.get()

        

        if not credentials or credentials.invalid:

            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)

            flow.user_agent = self.APPLICATION_NAME

            if flags:

                credentials = tools.run_flow(flow, store, flags)

            else: # Needed only for compatibility with Python 2.6

                credentials = tools.run(flow, store)

            print('Storing credentials to ' + credential_path)

        

        return credentials



    # メールリストを取得

    def get_messages(self, q=""):

        try:
            
            results = self.service.users().messages().list(userId=self.user_id, labelIds=['UNREAD', 'INBOX'], q=q).execute()

            for msg in results.get("messages", []):

                message = self.service.users().messages().get(userId=self.user_id, id=msg["id"],format='raw').execute()

                msg_str = base64.urlsafe_b64decode(message['raw']).decode("utf-8", "ignore")

                self.msg = email.message_from_string(msg_str)

                yield self

        except errors.HttpError as error:

            raise("An error occurred: %s" % error)



    # 件名を取得

    @property

    def fromget(self):

        subjects = email.header.decode_header(self.msg.get("From"))

        for subject in subjects:

            if isinstance(subject[0], bytes) and subject[1] is not None:

                return subject[0].decode(subject[1], "ignore")

            else:

                return subject[0]




    # 件名を取得

    @property

    def subject(self):

        subjects = email.header.decode_header(self.msg.get("Subject"))

        for subject in subjects:

            if isinstance(subject[0], bytes) and subject[1] is not None:

                return subject[0].decode(subject[1], "ignore")

            else:

                return subject[0]



    # 本文を取得

    @property

    def body(self):

        if self.msg.is_multipart():

            for payload in self.msg.get_payload():

                if payload.get_content_type() == "text/plain":

                    charset = self.msg.get_param("charset")

                    if charset is None:

                        return payload.get_payload(decode=True).decode("iso-2022-jp", "ignore")

                    else:

                        return payload.get_payload(decode=True).decode(charset)

        else:

            charset = self.msg.get_param("charset")

            return self.msg.get_payload(decode=True).decode(charset)



if __name__ == '__main__':

    Gmail = GmailClient()

    messages = Gmail.get_messages()


    """
    if not messages:

        print('No messages found.')

    else:

        for message in messages:
            print(message.fromget)
            mes=message.subject.encode("cp932", "ignore")
            mes2=mes.decode("cp932", "ignore")
            print(mes2) 
            #print(message.body)
    """