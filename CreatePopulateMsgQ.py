# -*- coding: utf-8 -*-
"""
Code for creating and populating the message queue using RabbitMQ queue

Created on Mon Apr 06 2015

@author: Vishal
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='msg_queue', durable=True)

msglist=[]
msglist.append("""{
  'type': 'email',
  'from': 'no-reply@company.com',
  'recipients': ['test1@test.com', 'test2@test.com'],
  'html': 'This is a test email. It can <i>also</i> contain HTML code',
  'text': 'This is a test email. It is text only'
}""")

msglist.append("""{
  'type': 'sms',
  'from': 'Vishal',
  'recipients': ['+919820494203'],
  'body': 'Test SMS message body'
}""")

# Send messages to queue
for msg in msglist:
    channel.basic_publish(exchange='',
                      routing_key='msg_queue',
                      body=msg,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
    print " [x] Sent %r" % (msg,)
    
connection.close()