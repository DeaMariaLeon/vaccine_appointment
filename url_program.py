#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:18:08 2021

Program to find a vaccination appointment on Doctolib
for an earlier date than the one I currently have.

Input variables:
    min_var = How often should the program check Doctolib website in minutes
    yr m d = The date of the appointment I already have (year, month, day) integers
    
"""

   
import urllib 
import json
from datetime import timedelta
from datetime import date
from datetime import datetime
import time
import os

def my_beep():
        
        os.system("echo -n '\a';sleep 0.2;" * 10)
        return

#Function that opens the website. If there is a date available earlier than mine,
#it will return the read data and a True flag

def Open_link(request, yr=2021, m=6, d=5):
        responsejson = urllib.request.urlopen(request)
        
        data = json.load(responsejson)
        
        #my_appointment = date(2021, 6, 5)
        my_app = date(yr, m , d)
        if 'next_slot' in data.keys():
        
            next_date = date.fromisoformat(data['next_slot'])
            if next_date < my_app:
                print("Change!",next_date)
                
                return data, True
            else:
                print("Keep")
        return data, False    
    
def url_prog(min_var):    
    #Start checking the website with today's date 
    start_date= str(date.today())
    
    
    path = "https://www.doctolib.fr/availabilities.json?start_date=" + start_date + "&visit_motive_ids=2554492&agenda_ids=432131-412723&insurance_sector=public&practice_ids=176188&destroy_temporary=true&limit=4"
    
    request = urllib.request.Request(path)
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15')
           
    minutes = timedelta(minutes = min_var)
    now = datetime.today().now()
    add_time = now + minutes
    print(now)
    print(add_time)
    
    try:
        while True:
            time.sleep(min_var * 60)
            print("no duermo")
            if  (now + minutes) < datetime.today().now():
                print("Opening...")
                
                response = Open_link(request)
                
                if response[1]:
                    my_beep()
                    print(response)
                    
                    break
                now = datetime.today().now()
                        
    except KeyboardInterrupt:
        print("exiting")
        pass

url_prog(1)