# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 2015

@author: Vishal
"""

import time
import smtplib
from settings import BLACKOUT_WINDOW, EMAIL_HOST,EMAIL_HOST_USER, \
                     EMAIL_HOST_PASSWORD,EMAIL_PORT
     

class MessageHandler:
    def __init__(self):
        self.sms_blackout_hours = set()
    
    def isMsgBlackoutPeriod(self):
        current_hour = time.localtime().tm_hour
        blackout_start_hour, blackout_end_hour = BLACKOUT_WINDOW
        
        if blackout_start_hour < blackout_end_hour:
            self.sms_blackout_hours = set(range(blackout_start_hour,\
                                                 blackout_end_hour))
        elif blackout_start_hour > blackout_end_hour:
            sms_allowed_hours = set(range(blackout_end_hour,\
                                          blackout_start_hour)) 
            self.sms_blackout_hours = set(range(0,24)) - sms_allowed_hours
        else:
            print "no blackout window is set"
            return False
            
        if current_hour in self.sms_blackout_hours:
            return True
        else:
            return False

    def sendsms(self, sender, msg):
        print "sms: %s  received from %s" % (msg,sender)
    
    def sendmail(self, sender, receivers, message):
        try:
           smtpserver = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
           smtpserver.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)  
           smtpserver.sendmail(sender, receivers, message)
        except smtplib.SMTPException:
           print "Error: unable to send email"
        
    def processMsg(self, message):
        if message['type'] == 'email':
                sender = message['from']
                receivers = message['recipients']
                subject = "Test mail for JRD"
    
                header  = 'From: %s\n' % message['from']
                header += 'To: %s\n' % ','.join(message['recipients'])
                header += 'Subject: %s\n\n' % subject
                msg = header + message['text']
                
                print "sending email with msg : \n %s" %(msg)
                self.sendmail(sender, receivers, msg)
        elif message['type'] == 'sms':
            if self.isMsgBlackoutPeriod():
                print "sms blackout period is going on"
            else:
                self.sendsms(message['from'], message['body'])
        else:
            print "unsupported message type %r" % (message)
        