# CHATBOT_BASIC_GUI for COnnectfor

# Master- file select and message button
# To do - add connectfor image,disable button until xlsx is uploaded
 
# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('900x700') 
  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Excel Files', '*.xlsx')]) 
    if file is not None: 
        # content = file.read() 
        # print(file.name)
        l2['text'] = "File uploaded : \n"+file.name 
def message(temp): 
    l3['text'] = "Final message : \n"+temp 
    # print(temp)

# Create text widget and specify size. 
T = Text(root, height = 10, width = 62) 

# Create label 
l = Label(root, text = "Message of the Day") 
l.config(font =("Courier", 24)) 

Fact = """Enter your message here"""

l3 = Label(root, text = "Please write the message !") 
l3.config(font =("Courier", 14)) 

# Create button for next text. 
b1 = Button(root, text = "Go",command=lambda:message(str(T.get("1.0",END))))

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