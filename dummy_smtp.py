# -*- coding: utf-8 -*-
 
import os
import asyncore
import smtpd
import datetime
import base64
import quopri
import logging
import gmailAPI
import subprocess
import re
import threading
import time
 

#���C���N���X
class Hoge():
  def __init__(self):

    #�����ݒ�

    self.stop_event=threading.Event()
    self.thread=threading.Thread(target=self.funk1)
    self.thread.start()
 
  def funk1(self):

    #stop_event�����s������usb����~

    while not self.stop_event.is_set():
       subprocess.call(["sudo","hub-ctrl","-h","0","-P","2","-p","0"],shell=False)
 
  def funk2(self):

    #�O���ɐڑ�

    subprocess.call(["sudo","python","test.py"])
 
    try:
 
        asyncore.loop()

        #GmailAPI���Ăяo��

        messages=Gmail.get_messages()
        print(messages)
     
        if not messages:
 
            time.sleep(5.0)
            self.Continue()
 
        else:
 
            for message in messages:

                #���[���̐U�蕪��

                f=open("message.txt","w")
                f.write(message.fromget+"\t")
                print(message.fromget)
                mes=message.subject.encode("cp932", "ignore")
                mes2=mes.decode("cp932", "ignore")
                f.write(mes2)
                print(mes2)
                f.close()
                with open("message.txt","r") as f:
                    data = f.read()
 
                #�t�@�C�����󂩂ǂ����̃e�X�g
                if len(data):
                    path = "mot1.py"

                    #���[���̔���ݒ�

                    hantei_kenmei = "�e�X�g"
                    hantei_atesaki = "kawamura"
                    f = open("message.txt", 'r', encoding='utf-8')
                 
                    for line in f:
                        rec = []
                        rec = line.split("\t")

                        #���[���̔���

                        if rec[1] == hantei_kenmei:
                           #ON=1
                           self.stop()
                           break
                        if hantei_atesaki in rec[0]:
                           #ON=1
                           self.stop()
                           break
 
 
                    print(line)
                    f.close()
                else:
                    f.close()

            #5�b��ɃR���e�B�j���[

            time.sleep(5.0)
            self.Continue()
 
    except:
        print("miss")
        logging.info('Server Stopped')
 
 
  def stop(self):
    print("stop")
    self.stop_event.set()
    subprocess.call(["sudo","hub-ctrl","-h","0","-P","2","-p","1"],shell=False)
 
  def Continue(self):
    print("ok")
 


#GmailAPI�̏����ݒ�
Gmail=gmailAPI.GmailClient()


 
 
h=Hoge()
h.funk2()