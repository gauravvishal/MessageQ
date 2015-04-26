# -*- coding: utf-8 -*-
"""
Code for processing the messages from message queue

Created on Mon Apr 06 2015

@author: Vishal
"""

import pika
from MessageHandler import MessageHandler


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='msg_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    print " [x] Done"
    
    # creating message dict from string then we can process that
    msg = eval(body)
    
    if isinstance(msg, dict):
        mh = MessageHandler()
        mh.processMsg(msg)
    else:
        print "unsupported message: Can't be processed"
        
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='msg_queue')

channel.start_consuming()


    