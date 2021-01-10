
#Convert csv to excel using python
import pandas as pd
#********************CREATE THAT FILE IN THAT PATH**********************************************************
#read_file=pd.read_csv(r'C:\yourpath\yourfile.csv')
#read_file.to_excel(r'C:\yourpath\new_file.xlsx')
#print(read_file)
#**************************************************************************************************************

#*********import  withGUI*********************************************************************
import tkinter as tk

from tkinter import filedialog
import tkinter as MessageBox
import tkinter.messagebox as tkMessageBox
from tkinter import Menu
root= tk.Tk()
root.title(" gsepdev.com Python: File Conversion" )# title window
canvas1 = tk.Canvas(root, width = 400, height = 400, bg = '#3b5998', relief = 'raised')
canvas1.pack()

#*******title inside************************
label1 = tk.Label(root, text='File Conversion ', bg = '#3b5998',fg='white')
label1.config(font=('verdana', 20))
canvas1.create_window(150, 60, window=label1)

menubar = Menu(root)


#***********import csv to python****************************************************************
def getCSV ():
    global read_file

    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv (import_file_path)
    print(read_file)

browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='black', fg='white', font=('verdana', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)
#******************************************************************************************
#*************conevert to csv to excel********************************************************************
global read_file
def convertToExcel ():
    global read_file

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel(export_file_path, index = None, header=True)
    print(export_file_path)
saveAsButton_Excel = tk.Button(text='Convert CSV to Excel', command=convertToExcel, bg='black', fg='white', font=('verdana', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Excel)


#****************************************************************************************************************************

def exit():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?', icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
#*******************************************************************************************************************************************


#********************************************************************************************************************************************
def About():
    
    tkMessageBox.showinfo("Information"," Tool to import csv file to python and converting to excel using pandas. Original exercise found in Datafish.com. Visit www.gsepdev.com, keep it simple!")

#**************************************************************************************************************************************


#***************************************************************************************************************************
#menu
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command =  exit)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About', command = About)


#*********************************************************************************************************************

root.config(menu = menubar)
root.mainloop()
