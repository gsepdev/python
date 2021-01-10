#read csv file (grid)
import tkinter
import tkinter as tk
import csv


root = tkinter.Tk()
root.title("Read csv File ")

# open file
with open("yourfile.csv", newline = "") as file:
   reader = csv.reader(file)
   # r and c tell us where to grid the labels
   r = 0
   for col in reader:
      c = 0
      for row in col:
         #some styling
         label = tkinter.Label(root, width = 25, height =2, \
                               text = row,  fg='darkblue', relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

tk.Button(root, text='Close',fg='darkblue',command=root.destroy).grid()


root.mainloop()
