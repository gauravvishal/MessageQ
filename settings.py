# -*- coding: utf-8 -*-
"""
Contains reqquired setting used by messagehandler

Created on Mon Apr 06 2015

@author: Vishal
"""

# Setting for Blackout Window : (blackout_start_hour, blackout_end_hour) . 
# start hours and end hour should be in 0-24 hour format .e.g (1,7) or (18,6)
BLACKOUT_WINDOW = (18, 6)

# Setting for SMTP Mail Server 
EMAIL_HOST = 'mailtrap.io'
EMAIL_HOST_USER = '328538ae2971cf050'
EMAIL_HOST_PASSWORD = 'bc326b37c3163d'
EMAIL_PORT = 2525