Introduction:
=============
Message queues provide an asynchronous communications protocol, meaning that the sender and receiver of the message do not need to interact with the message queue at the same time. Messages placed onto the queue are stored until the recipient retrieves them.

You can get more details about messageQ at:

http://blog.codepath.com/2013/01/06/asynchronous-processing-in-web-applications-part-2-developers-need-to-understand-message-queues/
http://blog.iron.io/2012/12/top-10-uses-for-message-queue.html

This code is a sample implementation for processiog a message queue created though RabbitMQ queue. RabbitMQ is a messaging broker - an intermediary for messaging. It gives your applications a common platform to send and receive messages, and your messages a safe place to live until received. Details can be found at (https://www.rabbitmq.com).

This application create a messaging service that reads incoming messages from a RabbitMQ queue, and sends out SMS and Emails, depending on the message type. It also care about a scenario where we want to pause sending SMS messages during a specified time period, like 6pm to 6am (only sms wiill be paused but mail will be sent). This time period will be configurable from a setting file i.e. settings.py.

The message formats on the input queue are:

Email:

{
  'type': 'email',
  'from': 'no-reply@company.com',
  'recipients': ['test1@test.com', 'test2@test.com'],
  'html': 'This is a test email. It can <i>also</i> contain HTML code'
  'text': 'This is a test email. It is text only'
}
SMS:

{
  'type': 'sms',
  'from': 'Vishal',
  'recipients': ['+919820494203'],
  'body': 'Test SMS message body'
}


Prereqisite:
============
You need to have following things installed for running this code:

1. Python 2.7 (www.python.org) . You Can use anaconda python distribution which comes with Python IDE (please check https://store.continuum.io/cshop/anaconda/)
2. python package pika. To install that on windows run "pip install pika==0.9.8" on command prompt .(check details on http://pypi.python.org/pypi/pika)
2. RabitMQ service (check details at https://www.rabbitmq.com)


Once you have those things installed then you can use this code to demontrate messaging application.


how to use this code:

1. unzip the file at some location 
2. open 2 consoles ( dos command prompt on windows) and go to the location where you have unzipped content.
3. run "python MessageWorker.py" in one console (without quotes)
4. On other console run "python CreatePopulateMsgQ.py" (without quotes)
5  you can see that sms message will be appearing on the console running MessageWorker.py and you can look into your mailtrap.io account for checking the mail sent by application.  


COde description:
=================

Code contains 4 files:


CreatePopulateMsgQ.py:  This file contains the code for creating a message queue from RabbitMQ Queue. I have populated the queue using manually created message list for simulating input messages.

MessageWorker.py: This file contains the code for receiving the messages from the message queue and processing those messages.

MessageHandler.py : This file contains the code for MessageHandler class which provides the functionality for sending mails and sms (sending sms is simulated by just identifying the message with sms type and printing its content. This also have the code to support an sms blackout window i.e. timeriod when smses should not be sent. There is no blackout window for sending mail.

settings.py: This contains the settings for sms blackout window. Sms blackout window supports time in hours (0-23 hours format) and not in minutes e.g. sms blackout window time (18, 6) means sms blackout start time is 18 hours (6pm) and blackout end hour is 6 am. start time like 18:30 is not supported. Apart from sms blackout window, this file also contains setting for SMTP mail Server. I am using https://mailtrap.io/ as my email SMTP server and have given the settings as per my mailtarp.io account. You need to change mail server setting as per your mailtarp.io account. you can create a free mailtrap.io account for sendmail testing. for more info please refer https://mailtrap.io/ 


