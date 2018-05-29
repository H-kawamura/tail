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

und=0
ON=1
class Hoge():
  def __init__(self):
    self.stop_event=threading.Event()
    self.thread=threading.Thread(target=self.funk1)
    self.thread.start()

  def funk1(self):
    global unb
    unb=0
    while not self.stop_event.is_set():
	    #subprocess.call(["sudo","hub-ctrl","-h","0","-P","2","-p","0"],shell=False)
       print("on")
       time.sleep(10.0)

  def funk2(self):
    global unb
    unb=0
    subprocess.call(["sudo","python","test.py"])
    ON=1


    try:

        asyncore.loop()
        messages=Gmail.get_messages()
        print(messages)
    
        if not messages:

            time.sleep(5.0)
            self.Continue()

        else:

            for message in messages:
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

                #繝輔ぃ繧､繝ｫ縺檎ｩｺ縺九←縺・°縺ｮ繝・せ繝・                if len(data):
                    path = "mot1.py"
                    hantei_kenmei = "繝・せ繝・
                    hantei_atesaki = "kawamura"
                    f = open("message.txt", 'r', encoding='utf-8')
                
                    for line in f:
                        rec = []
                        rec = line.split("\t")
                        if rec[1] == hantei_kenmei:
                           #ON=1
                           self.stop()
                           break
                        if hantei_atesaki in rec[0]:
                           #ON=1
                           self.stop()
                           break


                    print(line)
                    #subprocess.call(窶徘ython %s窶・% path)
                    f.close()
                else:
                    f.close()
            time.sleep(5.0)
            self.Continue()

    except:
        print("miss")
        logging.info('Server Stopped')


  def stop(self):
    print("stop")
    self.stop_event.set()
    #subprocess.call(["sudo","hub-ctrl","-h","0","-P","2","-p","1"],shell=False)

  def Continue(self):
    print("ok")

Gmail=gmailAPI.GmailClient()
ON=0
app_down=0


h=Hoge()
h.funk2()


