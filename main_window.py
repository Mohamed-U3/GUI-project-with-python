from tkinter import *
from tkinter import messagebox
from turtle import width

#Create the main window of the app
main_window = Tk()

#change app Text title
main_window.title("orders notification App")

#set dimintions
main_window.geometry("600x400")

#Writing age label
the_text = Label(main_window, text=" Write your age",height=2,font=("Arial",20))
the_text.pack() #Place the text into the main window

# Age Variables
age = StringVar()

#Set Default Value for age
age.set("00")

#Create The Input for age
age_input = Entry(main_window,width="2",font=("arial",20),textvariable=age)
age_input.pack() #Place the text input into the main window

def calc():
    #get age in years
    the_age_avlue = age.get()

    #get time in units of months, weeks and days
    months = int(the_age_avlue)*12
    weeks = months * 4
    days = int(the_age_avlue) * 365

    line_one = f"your age in monthes is: {months}"
    line_two = f"your age in monthes is: {weeks}"
    line_three = f"your age in monthes is: {days}"

    all_lines = [line_one, line_two,line_three]

    messagebox.showinfo("Your Age in all time units", "\n".join(all_lines))

# create teh calculate Button
btn = Button(main_window, text="Calculate Age", width=20, height=2,bg="#e92e63",fg="white",borderwidth=0, command=calc)
btn.pack() #Place the button into the main window

#maximize the app
# main_window


#Run App for Infinty time
main_window.mainloop()