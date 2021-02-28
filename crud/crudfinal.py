from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox



# Main frame for application
root = Tk()
root.title("Python: CRUD Application created in Tkinter")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 950
height =600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

# Creating Menubar
menubar = Menu(root)
#************Data base connection*********************************

def Database():
    global conn, cursor
    conn = sqlite3.connect('db_crud.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT,  address TEXT)")

#****************Show data stored*********************************************************************

def displayData():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3]))

    cursor.close()
    conn.close()
    firstname.focus()

#***************************

#********************************create function******************************************
def Create():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or ADDRESS.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `member` (firstname, lastname,address) VALUES(?,?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(ADDRESS.get())))
        conn.commit()
        FIRSTNAME.set("")
        LASTNAME.set("")
        ADDRESS.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Record  added Successfully!", fg="dark blue")
        displayData()


#************************end create**********************************
#**************************UPDATE***************************************************
def selectedRow(event):
    global mem_id;
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']

    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    ADDRESS.set("")


    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    ADDRESS.set(selecteditem[3])
    btn_update.config(state=NORMAL)
    btn_delete.config(state=NORMAL)


def Update():
    Database()
    tree.delete(*tree.get_children())
    cursor.execute("UPDATE `member` SET `firstname` = ?, `lastname` = ?,  `address` = ?  WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(ADDRESS.get()), int(mem_id)))
    conn.commit()
    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3]))


    FIRSTNAME.set("")
    LASTNAME.set("")
    ADDRESS.set("")
    cursor.close()
    conn.close()
    txt_result.config(text="Record  updated Successfully!", fg="dark blue")

    btn_update.config(state=DISABLED)



#**************************************end update********************************


def Delete():
    if tree.selection():
        result = tkMessageBox.askquestion(' Delete', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            FIRSTNAME.set("")
            LASTNAME.set("")
            ADDRESS.set("")
            cursor.close()
            conn.close()


        else:
            FIRSTNAME.set("")
            LASTNAME.set("")
            ADDRESS.set("")
            btn_update.config(state=DISABLED)
            btn_delete.config(state=DISABLED)
            displayData()



#****************************END delete******************************************************

def Exit():
    result = tkMessageBox.askquestion('Python: CRUD Application', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#********************************************************

def About():

    tkMessageBox.showinfo("Information","You can add , update and delete records. Those will be stored in a database created in sqlite3")
#****************************************SEARCH


#*function to search data*********************************
def SearchRecord():
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        Database()

        #select query with where clause
        cursor.execute("SELECT * FROM member WHERE firstname LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#*********************display data after SEARCH************************************
def DisplayData():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    Database()

    #select query
    cursor.execute("SELECT * FROM member")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))

    cursor.close()
    conn.close()


#*********************end search********************
#menu
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About CRUD', command = About)


#==================================VARIABLES==========================================
memid = int()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
ADDRESS = StringVar()
SEARCH = StringVar()


#==================================FRAME==============================================
Top = Frame(root, width=900, height=500, bd=3, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=100, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 20), text = "GsepDev: CRUD Application", bg='#3b5998',fg='white')
txt_title.pack()



txt_firstname = Label(Forms, text="First Name:", font=('arial', 14), bd=15)
txt_firstname.grid(row=1, stick="e")
txt_lastname = Label(Forms, text="Last Name:", font=('arial', 14), bd=15)
txt_lastname.grid(row=2, stick="e")

txt_address = Label(Forms, text="Address:", font=('arial', 14), bd=15)
txt_address.grid(row=3, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================


firstname = Entry(Forms, textvariable=FIRSTNAME, width=30)
firstname.focus()
firstname.grid(row=1, column=1)

lastname = Entry(Forms, textvariable=LASTNAME, width=30)
lastname.grid(row=2, column=1)

address = Entry(Forms, textvariable=ADDRESS, width=30)
address.grid(row=3, column=1)


#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)

btn_update = Button(Buttons, width=10, text="Update", command=Update, state= DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", command=Delete,state= DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)
#btn_search = Button(Buttons, width=10,text="Search", command=SearchRecord)
#btn_search.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("MemID","Firstname", "Lastname",  "Address"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemID', text="ID", anchor=W)
tree.heading('Firstname', text="First Name", anchor=W)
tree.heading('Lastname', text="Last Name", anchor=W)
tree.heading('Address', text="Address", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)

tree.pack()
tree.bind('<Double-Button-1>', selectedRow)
#******************************************************************************
#**********************Search*******************************
SEARCH = StringVar()
lbl_txtsearch = Label(root, text="Search", font=('verdana', 15))
lbl_txtsearch.pack(side=TOP, anchor=W)
search = Entry(root, textvariable=SEARCH, font=('verdana', 15), width=10)
search.pack(side=TOP, padx=10, fill=X)
btn_search = Button(root, text="Search", command=SearchRecord)
btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
btn_search = Button(root, text="View All", command=DisplayData)
btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
#==================================INITIALIZATION=====================================
displayData()
root.config(menu = menubar)

if __name__ == '__main__':
    root.mainloop()
