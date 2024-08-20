import tkinter
from tkinter import ttk
from tkinter import messagebox
import random

#Main Window
window = tkinter.Tk()
window.title("Julie's Party Hire")
window.geometry('350x350')

frame = tkinter.Frame(window, width=325, height=350)
frame.pack(padx = 10, pady=10)

#Title 
title = tkinter.Label(frame, text="Julie's Party Hire")
title.place(x=102.5, y=10,width=120)

#Hire Window
def hire_b():
    window_1 = tkinter.Tk()
    window_1.title("Hire Page - Julie's Party Hire")
    window_1.geometry('350x350')

    frame_1 = tkinter.Frame(window_1,width=325, height=350)
    frame_1.pack(padx = 10, pady=10)

    #reciept number label
    reciept_number = tkinter.Label(frame_1, text="Reciept Number :")
    reciept_number.pack(padx=10, pady=10)
    reciept_number.place(x = 10, y = 10)

    #generating receipt number
    #keep track of used receipt numbers
    used_receipt_numbers = set()

    def generate_receipt_number():
        while True:
            randInt = random.randint(100000, 999999)
            if randInt not in used_receipt_numbers:
                used_receipt_numbers.add(randInt)
                return randInt
            
    randInt = generate_receipt_number()

    receipt_number_generate = tkinter.Label(frame_1, text=randInt)
    receipt_number_generate.pack(padx=10, pady=10)
    receipt_number_generate.place(x = 120, y=10)


    #validation for first name
    #function to check the length
    def check_length(first_name):
        return len(first_name) <= 20

    #function to check if input is empty
    def check_empty(first_name):
        return first_name != ""

    #function to check if the input contains only alphabets
    def check_input(first_name):
        return first_name.isalpha()

    #first name input
    first_name = tkinter.Label(frame_1, text="First Name :")
    first_name.pack(padx=10, pady=10)
    first_name.place(x = 10, y = 50)

    #first name entry box
    first_name_entry = tkinter.Entry(frame_1)
    first_name_entry.pack(padx=10, pady=10)
    first_name_entry.place (x = 105, y = 50, width = 220)

    #validation for last name
    #function to check the length
    def check_length(last_name):
        return len(last_name) <= 20

    #function to check if input is empty
    def check_empty(first_name):
        return first_name != ""

    #function to check if the input contains only alphabets
    def check_input(last_name):
        return last_name.isalpha()

    #last name label
    last_name = tkinter.Label(frame_1, text="Last Name :")
    last_name.pack(padx=10, pady=10)
    last_name.place (x = 10, y = 90)

    #last name entry box
    last_name_entry = tkinter.Entry(frame_1)
    last_name_entry.pack(padx=10, pady=10)
    last_name_entry.place (x = 105, y = 90, width = 220)

    #def function for combo box for Item to hire
    def show_item_to_hire(event) :
        item_to_hire = item_hire_combo.get()


    #Item to hire label
    item_hire = tkinter.Label(frame_1, text="Item to hire :")
    item_hire.pack(padx=10, pady=10)
    item_hire.place(x = 10, y = 130)

    #Item to hire combo box
    item_hire_combo = ttk.Combobox(frame_1, values=["Spoons","Forks","Knives","Balloons","Cake Stand","Birthday Banner"], state="readonly")
    item_hire_combo.pack(padx=10, pady=10)
    item_hire_combo.place(x = 105, y = 130, width = 220)
    item_hire_combo.bind("<<ComboboxSelected>>", show_item_to_hire)


    def check_value(quantity_hire_spinbox):
        try:
            value = int(quantity_hire_spinbox)
            return 1 <= value <= 500
        except ValueError:
            return False

        

    #label for quantity to hire
    quantity_hire = tkinter.Label(frame_1, text="Quantity to hire :")
    quantity_hire.pack(padx=10, pady=10)
    quantity_hire.place(x = 10, y = 170)

    #spin box for quantity to hire
    quantity_hire_spinbox = tkinter.Spinbox(frame_1, from_=1, to=500)
    quantity_hire_spinbox.pack(padx=10, pady=10)
    quantity_hire_spinbox.place(x = 130, y = 170, width = 195)

    #function to validate the input
    def validate_inputs():
        first_name = first_name_entry.get()

        if not check_empty(first_name):
            messagebox.showerror("Input Error", "First name cannot be blank")
        elif not check_length(first_name):
            messagebox.showerror("Input Error", "First name must be at most 20 characters long.")
        elif not check_input(first_name):
            messagebox.showerror("Input Error", "First name must contain only letters.")

        last_name = last_name_entry.get()

        if not check_empty(last_name):
            messagebox.showerror("Input Error", "Last name cannot be blank")
        elif not check_length(last_name):
            messagebox.showerror("Input Error", "Last name must be at most 20 characters long.")
        elif not check_input(last_name):
            messagebox.showerror("Input Error", "Last name must contain only alphabets.")

        item_hire = item_hire_combo.get()
        
        if not check_empty(item_hire):
            messagebox.showerror("Input Error", "Item to hire cannot be blank")

        quantity_hire = quantity_hire_spinbox.get()

        if not check_empty(quantity_hire):
            messagebox.showerror("Input Error", "Quantity to hire cannot be blank")
        elif not check_value(quantity_hire):
            messagebox.showerror("Input Error", "Quantity to hire must be between 1 and 500")
            

    #Command for quit button for hire page
    def quit_h():
        window_1.destroy()
        window.destroy()

    def done():
        window_4
        

    add_to_hire = tkinter.Button(frame_1, text="Add to Hire", command=validate_inputs)
    add_to_hire.place(x=20, y=210, width = 122.5)

    print_reciept_button = tkinter.Button(frame_1, text="Print Reciept")
    print_reciept_button.place(x=182.5, y=210, width=122.5)

    quit_button_hire = tkinter.Button(frame_1, text="Quit",command=quit_h)
    quit_button_hire.place(x=182.5, y=250, width=122.5)

    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Hire page","Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            window_1.destroy()
            

    homepage_button = tkinter.Button(frame_1, text="Homepage", command=homepage)
    homepage_button.place(x=20, y =250, width=122.5)

    

   
#Hire button
hire_button = tkinter.Button(frame, text="Hire",command=hire_b)
hire_button.pack(padx=10, pady=40)
hire_button.place(x=105, y=55, width=120)

#Return Button
return_button = tkinter.Button(frame, text="Return")
return_button.pack(padx=10, pady=40)
return_button.place(x=102.5, y=110, width=120)

#View Reciept Button
reciept_button = tkinter.Button(frame, text="View Receipt")
reciept_button.pack(padx=10, pady=40)
reciept_button.place(x=102.5, y=165, width=120)

#Command for quit button
def quit_b():
    window.destroy()

#Quit Button
quit_button = tkinter.Button(frame, text="Quit",command=quit_b)
quit_button.pack(padx=10, pady=40)
quit_button.place(x=102.5, y=220, width=120)


window.mainloop()




