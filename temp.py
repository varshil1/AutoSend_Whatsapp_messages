#Create Warning Box in Python GUI Application  
import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
app = tk.Tk()  
#Add a Title  
app.title("Python GUI App")  
#Label  
ttk.Label(app, text="Warning Messsage Box App").grid(column=0,row=0,padx=20,pady=30)  
#Create a Menu Bar  
menuBar=Menu(app)  
app.config(menu=menuBar)  
#Display a Message Box  
def _msgBox():  
   mbox.showwarning('Python Warning Message','This Python GUI Application Using Warning Box.')  
   #Create warning Message Menu  
   infoMenu=Menu(menuBar, tearoff=0)  
   infoMenu.add_command(label="Warning", command=_msgBox)menuBar.add_cascade(label="Message", menu=infoMenu)  
   #Calling Main()  
   app.mainloop()