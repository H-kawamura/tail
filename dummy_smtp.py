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
 

#メインクラス
class Hoge():
  def __init__(self):

    #初期設定

    self.stop_event=threading.Event()
    self.thread=threading.Thread(target=self.funk1)
    self.thread.start()
 
  def funk1(self):

    #stop_eventが実行されるとusbが停止

    while not self.stop_event.is_set():
       subprocess.call(["sudo","hub-ctrl","-h","0","-P","2","-p","0"],shell=False)
 
  def funk2(self):

    #外部に接続

    subprocess.call(["sudo","python","test.py"])
 
    try:
 
        asyncore.loop()

        #GmailAPIを呼び出し

        messages=Gmail.get_messages()
        print(messages)
     
        if not messages:
 
            time.sleep(5.0)
            self.Continue()
 
        else:
 
            for message in messages:

                #メールの振り分け

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
 
                #ファイルが空かどうかのテスト
                if len(data):
                    path = "mot1.py"

                    #メールの判定設定

                    hantei_kenmei = "テスト"
                    hantei_atesaki = "kawamura"
                    f = open("message.txt", 'r', encoding='utf-8')
                 
                    for line in f:
                        rec = []
                        rec = line.split("\t")

                        #メールの判定

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

            #5秒後にコンティニュー

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
 


#GmailAPIの初期設定
Gmail=gmailAPI.GmailClient()


 
 
h=Hoge()
h.funk2()