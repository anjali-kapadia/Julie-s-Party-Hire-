import tkinter
from tkinter import ttk
from tkinter import messagebox
import random

receipt_data = []

used_receipt_numbers = set()

def generate_receipt_number():
    while True:
        randInt = random.randint(100000, 999999)
        if randInt not in used_receipt_numbers:
            used_receipt_numbers.add(randInt)
            return randInt

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
    window_hire = tkinter.Toplevel()
    window_hire.title("Hire Page - Julie's Party Hire")
    window_hire.geometry('350x350')

    frame_hire = tkinter.Frame(window_hire,width=325, height=335)
    frame_hire.pack(padx = 10, pady=10)

    def get_new_receipt_number():
        return generate_receipt_number()

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
    first_name = tkinter.Label(frame_hire, text="First Name :")
    first_name.pack(padx=10, pady=10)
    first_name.place(x = 10, y = 50)

    #first name entry box
    global first_name_entry
    first_name_entry = tkinter.Entry(frame_hire)
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
    last_name = tkinter.Label(frame_hire, text="Last Name :")
    last_name.pack(padx=10, pady=10)
    last_name.place (x = 10, y = 90)

    #last name entry box
    global last_name_entry
    last_name_entry = tkinter.Entry(frame_hire)
    last_name_entry.pack(padx=10, pady=10)
    last_name_entry.place (x = 105, y = 90, width = 220)

    #def function for combo box for Item to hire
    def show_item_to_hire(event) :
        item_to_hire = item_hire_combo.get()

    #Item to hire label
    item_hire = tkinter.Label(frame_hire, text="Item to hire :")
    item_hire.pack(padx=10, pady=10)
    item_hire.place(x = 10, y = 130)

    #Item to hire combo box
    global item_hire_combo
    item_hire_combo = ttk.Combobox(frame_hire, values=["Spoons","Forks","Knives","Balloons","Cake Stand","Birthday Banner"], state="readonly")
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
    quantity_hire = tkinter.Label(frame_hire, text="Quantity to hire :")
    quantity_hire.pack(padx=10, pady=10)
    quantity_hire.place(x = 10, y = 170)

    #spin box for quantity to hire
    global quantity_hire_spinbox
    quantity_hire_spinbox = tkinter.Spinbox(frame_hire, from_=1, to=500)
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

        #def function to reset combobox and spinbox if user wants to hire more items
        def reset():
            item_hire_combo.set('')
            quantity_hire_spinbox.delete(0, 'end')
            quantity_hire_spinbox.insert(0, '1')

        #def function for hire receipt
        def hire_receipt(receipt_number, first_name, last_name, item_hire, quantity_hire):
            window_hire_receipt = tkinter.Toplevel()
            window_hire_receipt.title("Hire Reciept - Julie's Party Hire")
            window_hire_receipt.geometry('250x220')

            def return_hire_page():
                window_hire_receipt.destroy()

            frame_hire_receipt = tkinter.Frame(window_hire_receipt,width=225, height=205)
            frame_hire_receipt.pack(padx=10, pady=10)

            tkinter.Label(frame_hire_receipt, text=f"Receipt Number: #{receipt_number}").pack(pady=5)
            tkinter.Label(frame_hire_receipt, text=f"First Name: {first_name}").pack(pady=5)
            tkinter.Label(frame_hire_receipt, text=f"Last Name: {last_name}").pack(pady=5)
            tkinter.Label(frame_hire_receipt, text=f"Item Hired: {item_hire}").pack(pady=5)
            tkinter.Label(frame_hire_receipt, text=f"Quantity Hired: {quantity_hire}").pack(pady=5)

            return_hire_button = tkinter.Button(frame_hire_receipt, text="Return", command=return_hire_page)
            return_hire_button.pack(pady=5)
            

        if not check_empty(first_name):
            messagebox.showerror("Input Error", "First name cannot be blank")
        elif not check_length(first_name):
            messagebox.showerror("Input Error", "First name must be at most 20 characters long.")
        elif not check_input(first_name):
            messagebox.showerror("Input Error", "First name must contain only letters.")
        elif not check_empty(last_name):
            messagebox.showerror("Input Error", "Last name cannot be blank")
        elif not check_length(last_name):
            messagebox.showerror("Input Error", "Last name must be at most 20 characters long.")
        elif not check_input(last_name):
            messagebox.showerror("Input Error", "Last name must contain only letters.")
        elif not check_empty(item_hire):
            messagebox.showerror("Input Error", "Item to hire cannot be blank")
        elif not check_empty(quantity_hire):
            messagebox.showerror("Input Error", "Quantity to hire cannot be blank")
        elif not check_value(quantity_hire):
            messagebox.showerror("Input Error", "Quantity to hire must be between 1 and 500")
        else:
            #Show message that hire information is added
            receipt_number = get_new_receipt_number()
            receipt_data.append((receipt_number, first_name, last_name, item_hire, quantity_hire))
            messagebox.showinfo("Info", "Item hired successfully!")
            hire_receipt(receipt_number, first_name, last_name, item_hire, quantity_hire)
            reset()
            

    #Command for quit button for hire page
    def quit_h():
        window_hire.destroy()
        window.destroy()

    add_to_hire = tkinter.Button(frame_hire, text="Add to Hire", command=validate_inputs)
    add_to_hire.place(x=20, y=210, width = 285)

    quit_button_hire = tkinter.Button(frame_hire, text="Quit",command=quit_h)
    quit_button_hire.place(x=167.5, y=250, width=137.5)

    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Hire page","Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            window_hire.destroy()
            
    homepage_button = tkinter.Button(frame_hire, text="Homepage", command=homepage)
    homepage_button.place(x=20, y =250, width=137.5)


   
#Hire button
hire_button = tkinter.Button(frame, text="Hire",command=hire_b)
hire_button.pack(padx=10, pady=40)
hire_button.place(x=105, y=55, width=120)

#Return Button
return_button = tkinter.Button(frame, text="Return")
return_button.pack(padx=10, pady=40)
return_button.place(x=102.5, y=110, width=120)

def view_receipt():
    window_view_receipt = tkinter.Toplevel()
    window_view_receipt.title("View Receipt - Julie's Party Hire")
    window_view_receipt.geometry('350x115')

    frame_view_receipt = tkinter.Frame(window_view_receipt, width=325, height=100)
    frame_view_receipt.pack(padx=10, pady=10)

    receipt_number = tkinter.Label(frame_view_receipt, text="Receipt Number:")
    receipt_number.pack(padx=10,pady=10)
    receipt_number.place(x=20,y=15,width=100)         

    global receipt_combo
    receipt_combo = ttk.Combobox(frame_view_receipt, values=list(used_receipt_numbers),state="readonly")
    receipt_combo.place(x=130, y=15, width=175)

    def check_empty(receipt_combo):
        return receipt_combo != ""

    def display_receipt():
        def check_empty(receipt_combo):
            return receipt_combo != ""
        receipt_validation = receipt_combo.get()
        if not check_empty(receipt_validation):
            messagebox.showerror("Input Error", "Receipt number cannot be blank")
            
        
        found = False
        for item in receipt_data:
            if item[0] == receipt_number:
                receipt_window = tkinter.Toplevel()
                receipt_window.title("Receipt - Julie's Party Hire")
                receipt_window.geometry('250x180')

                def return_receipt():
                    receipt_window.destroy()

                receipt_frame = tkinter.Frame(receipt_window, width=225, height=165)
                receipt_frame.pack(padx=5, pady=5)
                
                tkinter.Label(receipt_frame, text=f"Receipt Number: {item[0]}").pack(pady=5)
                tkinter.Label(receipt_frame, text=f"Name: {item[1]} {item[2]}").pack(pady=5)
                tkinter.Label(receipt_frame, text=f"Item Hired: {item[3]}").pack(pady=5)
                tkinter.Label(receipt_frame, text=f"Quantity Hired: {item[4]}").pack(pady=5)

                return_button = tkinter.Button(receipt_frame, text="Return",command=return_receipt)
                return_button.pack(pady=5)

                found = True
                break


    def return_receipt():
        receipt_window.destroy()
        
    view_receipt_button = tkinter.Button(frame_view_receipt, text="View Receipt",command=display_receipt)
    view_receipt_button.place(x=102.5, y=50, width=120)



#View Receipt Button
reciept_button = tkinter.Button(frame, text="View Receipt",command = view_receipt)
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




