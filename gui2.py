import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os
import argparse



# CHATBOT_BASIC_GUI for COnnectfor

# Master- file select and message button
# To do - add connectfor image,disable button until xlsx is uploaded
 
# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *

from tkinter import messagebox as mb  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('900x700') 

 # Initialize in main

parser = argparse.ArgumentParser(description='PyWhatsapp Guide')
parser.add_argument('--chrome_driver_path', action='store', type=str, default='./chromedriver.exe', help='chromedriver executable path (MAC and Windows path would be different)')
parser.add_argument('--message', action='store', type=str, default='', help='Enter the msg you want to send')
parser.add_argument('--remove_cache', action='store', type=str, default='False', help='Remove Cache | Scan QR again or Not')
args = parser.parse_args()

if args.remove_cache == 'True':
    os.system('rm -rf User_Data/*')
browser = None
Contact = None
message = None if args.message == '' else args.message
Link = "https://web.whatsapp.com/"
wait = None
choice = None
docChoice = None
doc_filename = None
unsaved_Contacts = None
file_selected=0
 #Functions for whatsapp
 
def input_contacts():
    global Contact, unsaved_Contacts
    # List of Contacts
    unsaved_Contacts = []
    
    data = pd.read_excel(filename)
    df = pd.DataFrame(data, columns= ['Name','Number'])
    Name=df['Name'].values
    Number=df['Number'].values
    # print(Name)
    # print(Number)
    # for i in range(0,len(Name)):
    #     print(Name[i])
    #     print(Number[i])
                        
    for i in range(0,len(Number)):
        unsaved_Contacts.append(str(Number[i]))
    # print(unsaved_Contacts)
    
    
    if len(unsaved_Contacts) != 0:
        print("Unsaved numbers entered list->", unsaved_Contacts)
    # input("\nPress ENTER to continue...")


def input_message(temp):
    global message
    # Enter your Good Morning Msg
    message = temp
    

def whatsapp_login(chrome_path):
    global wait, browser, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")


def send_message(target):
    global message, wait, browser
    try:
        x_arg = '//span[contains(@title,' + target + ')]'
        ct = 0
        while ct != 10:
            try:
                group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                break
            except:
                ct += 1
                time.sleep(3)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")
        time.sleep(1)
    except NoSuchElementException:
        return


def send_unsaved_contact_message():
    global message
    try:
        time.sleep(20)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                print("Yes")
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")
    except NoSuchElementException:
        print("Failed to send message")
        return


def sender():
    global Contact, choice, docChoice, unsaved_Contacts
    
    time.sleep(5)
    if len(unsaved_Contacts) > 0:
        for i in unsaved_Contacts:
            link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(i)
            #driver  = webdriver.Chrome()
            browser.get(link)
            print("Sending message to", i)
            send_unsaved_contact_message()
            time.sleep(7)


# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
    global filename
    global file_selected
    file = askopenfile(mode ='r', filetypes =[('Excel Files', '*.xlsx')]) 
    if file is not None: 
        # content = file.read() 
        # print(file.name)
        l2['text'] = "File uploaded : \n"+file.name 
        filename=file.name
        file_selected=1

def message2(temp,file_selected): 
    l3['text'] = "Final message : \n"+temp 
    # print(temp)
    # Here We go to merge the code
    
    if(file_selected==1):
        #Main
        input_contacts()
        input_message(temp)
        whatsapp_login(args.chrome_driver_path)
        sender()
        print("Task Completed")
        browser.close()
        if mb.askyesno('Exit', 'Send again'):
            mb.showwarning('OK', 'Press OK to go again')
        else:
            exit()
    else:
        mb.showwarning('Go Back', '.xlsx file not selected')
        print("File not selected")



# Create text widget and specify size. 
T = Text(root, height = 10, width = 62) 

# Create label 
l = Label(root, text = "Message of the Day") 
l.config(font =("Courier", 24)) 

Fact = """Enter your message here"""

l3 = Label(root, text = "Please write the message !") 
l3.config(font =("Courier", 14)) 

# Create button for next text. 
b1 = Button(root, text = "Go",command=lambda:message2(str(T.get("1.0",END)),file_selected))

# Create an Exit button. 
b2 = Button(root, text = "Exit", 
            command = root.destroy) 

l2 = Label(root, text = "File not selected") 
l2.config(font =("Courier", 14)) 

btn = Button(root, text ='Upload Excel File', command = lambda:open_file()) 
btn.pack()
btn.place(x=415,y=90) 
l.pack() 
l2.pack()
l2.place(x=220,y=140)
b1.pack()
b1.place(x=415, y=550) 

T.pack()
T.place(x=220,y=350) 
b2.pack()
b2.place(x=415,y=630) 
l3.pack()
l3.place(x=220,y=200)
T.insert(END, Fact) 

mainloop()