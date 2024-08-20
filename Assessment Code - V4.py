import tkinter
from tkinter import ttk
from tkinter import messagebox
import random

used_receipt_numbers = set()

def used_receipt_number():
    with open("Julie's party hire.txt", "r") as file:
        for line in file:
            receipt_number = int(line.strip().split(",")[0])
            used_receipt_numbers.add(receipt_number)
            
#def function to generate receipt number
def generate_receipt_number():
    while True:
        randInt = random.randint(100000, 999999)
        if randInt not in used_receipt_numbers:
            used_receipt_numbers.add(randInt)
            return randInt

def load_receipt_details(receipt_number):
    with open("Julie's party hire.txt", "r") as file:
        for line in file:
            item = line.strip().split(",")
            if item[0] == receipt_number:  # Assuming receipt_number is the first item
                return {'first_name': item[1], 'last_name': item[2], 'item_hire_combo':item[3], 'quantity_hire_spinbox': int(item[4])} 
    return {'first_name': '', 'last_name' : '', 'item_hire_combo' : '','quantity_hire': 0}


            
used_receipt_number()

#Main Window
window = tkinter.Tk()
window.title("Julie's Party Hire")
window.geometry('350x350')

#frame for main window
frame = tkinter.Frame(window, width=325, height=350)
frame.pack(padx = 10, pady=10)

#Title 
title = tkinter.Label(frame, text="Julie's Party Hire")
title.place(x=102.5, y=10,width=120)

#Hire Window
def hire():
    window_hire = tkinter.Toplevel()
    window_hire.title("Hire Page - Julie's Party Hire")
    window_hire.geometry('350x350')

    #frame for hire window
    frame_hire = tkinter.Frame(window_hire,width=325, height=335)
    frame_hire.pack(padx = 10, pady=10)

    #def function to generate new receipt number for each transaction
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

    #first name label
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

    #validation for quantity hire
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
        last_name = last_name_entry.get()       
        item_hire = item_hire_combo.get()
        quantity_hire = quantity_hire_spinbox.get()

        #validation messages
        if not check_empty(first_name):
            messagebox.showerror("Input Error", "First name cannot be blank.")
        elif not check_length(first_name):
            messagebox.showerror("Input Error", "First name must be at most 20 characters long.")
        elif not check_input(first_name):
            messagebox.showerror("Input Error", "First name must contain only letters.")
        elif not check_empty(last_name):
            messagebox.showerror("Input Error", "Last name cannot be blank.")
        elif not check_length(last_name):
            messagebox.showerror("Input Error", "Last name must be at most 20 characters long.")
        elif not check_input(last_name):
            messagebox.showerror("Input Error", "Last name must contain only letters.")
        elif not check_empty(item_hire):
            messagebox.showerror("Input Error", "Item to hire cannot be blank.")
        elif not check_empty(quantity_hire):
            messagebox.showerror("Input Error", "Quantity to hire cannot be blank.")
        elif not check_value(quantity_hire):
            messagebox.showerror("Input Error", "Quantity to hire must be between 1 and 500.")
        else:
            #def function for hire receipt
            def hire_receipt(receipt_number, first_name, last_name, item_hire, quantity_hire):
                window_hire_receipt = tkinter.Toplevel()
                window_hire_receipt.title("Hire Receipt - Julie's Party Hire")
                window_hire_receipt.geometry('250x220')

                #def function for return button
                def return_from_hire_page():
                    window_hire_receipt.destroy()
                    
                #frame for hire receipt
                frame_hire_receipt = tkinter.Frame(window_hire_receipt,width=225, height=205)
                frame_hire_receipt.pack(padx=10, pady=10)

                #labels for receipt 
                tkinter.Label(frame_hire_receipt, text=f"Receipt Number: #{receipt_number}").pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"First Name: {first_name}").pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"Last Name: {last_name}").pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"Item Hired: {item_hire}").pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"Quantity Hired: {quantity_hire}").pack(pady=5)

                #return from hire receipt button
                return_from_hire_button = tkinter.Button(frame_hire_receipt, text="Return", command=return_from_hire_page)
                return_from_hire_button.pack(pady=5)


            #Show message that hire information is added
            receipt_number = get_new_receipt_number()
            with open("Julie's party hire.txt","a") as file:
                file.write(f"{receipt_number},{first_name} ,{last_name}, {item_hire}, {quantity_hire}\n")
            first_name_entry.delete(0, tkinter.END)
            last_name_entry.delete(0, tkinter.END)
            item_hire_combo.set('')
            quantity_hire_spinbox.delete(0, tkinter.END)
            messagebox.showinfo("Info", "Item hired successfully!")
            hire_receipt(receipt_number, first_name, last_name, item_hire, quantity_hire)   

            
    #Command for quit button for hire page
    def quit_h():
        window_hire.destroy()
        window.destroy()

    #add to hire button
    add_to_hire = tkinter.Button(frame_hire, text="Add to Hire", command=validate_inputs)
    add_to_hire.place(x=20, y=210, width = 285)

    #quit button 
    quit_button_hire = tkinter.Button(frame_hire, text="Quit",command=quit_h)
    quit_button_hire.place(x=167.5, y=250, width=137.5)

    #homepage button code
    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Hire page","Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            window_hire.destroy()

    homepage_button = tkinter.Button(frame_hire, text="Homepage", command=homepage)
    homepage_button.place(x=20, y =250, width=137.5)

#Hire button
hire_button = tkinter.Button(frame, text="Hire",command=hire)
hire_button.pack(padx=10, pady=40)
hire_button.place(x=105, y=55, width=120)

def on_receipt_selected(event):
    receipt_number = receipt_combo.get()
    details = load_receipt_details(receipt_number)
    
    # Update the first name and amount based on the selected receipt
    first_name_label.config(text=f"First Name : {details['first_name']}")
    last_name_label.config(text=f"Last Name : {details['last_name']}")
    item_return.config(text=f"Item to Return : {details['item_hire_combo']}")
    quantity_return_spinbox.delete(0, tkinter.END)  # Clear the existing value
    quantity_return_spinbox.insert(0, details['quantity_hire_spinbox'])  # Set the new value

def save_return():
    receipt_number = receipt_combo.get().strip()  # Get the receipt number from the combobox
    
    if not receipt_number:
        tkinter.messagebox.showerror("Error", "Receipt Number cannot be left blank")
        return
    
    try:
        return_quantity = int(quantity_return_spinbox.get())
    except ValueError:
        tkinter.messagebox.showerror("Error", "Return quantity must be a valid number")
        return
    
    # Load the details for the selected receipt number
    details = load_receipt_details(receipt_number)
    
    try:
        quantity_hire = int(details.get('quantity_hire_spinbox', 0))
    except ValueError:
        tkinter.messagebox.showerror("Error", "Invalid quantity data")
        return
    
    if return_quantity > quantity_hire:
        tkinter.messagebox.showerror("Error", "Return quantity cannot be greater than the quantity hired")
        return
    
    if return_quantity <= 0:
        tkinter.messagebox.showerror("Error", "Return quantity must be greater than zero")
        return
    
    # Check if return_quantity is less than or equal to quantity_hire
    if return_quantity <= quantity_hire:
        # Prepare the updated record (excluding quantity to be returned)
        updated_quantity = quantity_hire - return_quantity
        updated_record = f"{receipt_number},{details['first_name']},{details['last_name']},{details['item_hire_combo']},{updated_quantity}\n"
        
        # Update record and write to file

    
    updated_lines = []
    record_deleted = False
    
    with open("Julie's party hire.txt", "r") as file:
        for line in file:
            item = line.strip().split(",")
            if item[0] == receipt_number:
                if quantity_hire - return_quantity > 0:
                # Create the updated record
                    updated_record = f"{receipt_number},{item[1]},{item[2]},{item[3]},{quantity_hire - return_quantity}\n"
                    updated_lines.append(updated_record)
                else:
                    record_deleted = True
            else:
                updated_lines.append(line)
        

    # Write updated records back to file
    with open("Julie's party hire.txt", "w") as file:
        file.writelines(updated_lines)

    if record_deleted:
        used_receipt_numbers.discard(int(receipt_number))
        tkinter.messagebox.showinfo("Success", "Receipt deleted as quantity hired became zero")
    else:
        tkinter.messagebox.showinfo("Success", "Return quantity updated successfully")


def return_r():
    #frame for return window
    window_return = tkinter.Toplevel()
    window_return.title("Return Page - Julie's Party Hire")
    window_return.geometry('350x350')

    #frame for return window
    frame_return = tkinter.Frame(window_return,width=325, height=335)
    frame_return.pack(padx = 10, pady=10)
    
    receipt_number = tkinter.Label(frame_return, text="Receipt Number:")
    receipt_number.pack(padx=10,pady=10)
    receipt_number.place(x=10,y=10)

    #receipt combobox
    global receipt_combo
    receipt_combo = ttk.Combobox(frame_return, values=list(used_receipt_numbers),state="readonly")
    receipt_combo.pack(padx=10, pady=10)
    receipt_combo.place(x=105, y=10, width = 220)
    receipt_combo.bind("<<ComboboxSelected>>", on_receipt_selected)

    global first_name_label
    first_name_label = tkinter.Label(frame_return, text="First Name:")
    first_name_label.pack(padx=10, pady=10)
    first_name_label.place(x=10, y=50)

    global last_name_label
    last_name_label = tkinter.Label(frame_return, text="Last Name:")
    last_name_label.pack(padx=10, pady=10)
    last_name_label.place(x=10, y=90) 

    #Item to hire label
    global item_return
    item_return = tkinter.Label(frame_return, text="Item to hire :")
    item_return.pack(padx=10, pady=10)
    item_return.place(x = 10, y = 130)

    # Spinbox for editing return amount
    global quantity_return
    quantity_return = tkinter.Label(frame_return, text="Quantity to Retun:")
    quantity_return.pack(padx=10, pady=10)
    quantity_return.place(x = 10, y = 170)
    
    global quantity_return_spinbox
    quantity_return_spinbox = tkinter.Spinbox(frame_return, from_=1, to=500)
    quantity_return_spinbox.pack(padx=10, pady=10)
    quantity_return_spinbox.place(x = 130, y = 170, width = 195)

    # Save button
    save_button = tkinter.Button(frame_return, text="Save", command=save_return)
    save_button.place(x=102.50, y=200)

    

#Return Button
return_button = tkinter.Button(frame, text="Return",command=return_r)
return_button.pack(padx=10, pady=40)
return_button.place(x=102.5, y=110, width=120)

#def function for view receipt button
def view_receipt():
    window_view_receipt = tkinter.Toplevel()
    window_view_receipt.title("View Receipt - Julie's Party Hire")
    window_view_receipt.geometry('350x145')

    frame_view_receipt = tkinter.Frame(window_view_receipt, width=325, height=130)
    frame_view_receipt.pack(padx=10, pady=10)

    receipt_number = tkinter.Label(frame_view_receipt, text="Receipt Number:")
    receipt_number.pack(padx=10,pady=10)
    receipt_number.place(x=20,y=15,width=100)

    #receipt combobox
    global receipt_combo
    receipt_combo = ttk.Combobox(frame_view_receipt, values=list(used_receipt_numbers),state="readonly")
    receipt_combo.place(x=130, y=15, width=175)

    #validation for receipt combobox
    def display_receipt():
        receipt_number = receipt_combo.get()
        receipt_number = receipt_combo.get()
        try:
            receipt_number = int(receipt_number)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Receipt Number cannot be left blank")
            return
        
        found = False
        with open("Julie's party hire.txt", "r") as file:
            for line in file :
                item = line.strip().split(",")
                if int(item[0]) == receipt_number:
                    receipt_window = tkinter.Toplevel()
                    receipt_window.title("Receipt - Julie's Party Hire")
                    receipt_window.geometry('250x180')

                    #back receipt command
                    def back_receipt():
                        receipt_window.destroy()

                    #receipt window
                    receipt_frame = tkinter.Frame(receipt_window, width=225, height=165)
                    receipt_frame.pack(padx=5, pady=5)
                    
                    tkinter.Label(receipt_frame, text=f"Receipt Number: {item[0]}").pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"Name: {item[1]} {item[2]}").pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"Item Hired: {item[3]}").pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"Quantity Hired: {item[4]}").pack(pady=5)

                    return_button = tkinter.Button(receipt_frame, text="Back",command=back_receipt)
                    return_button.pack(pady=5)

                    found = True
                    break
            
    #back receipt button command       
    def back_receipt():
        receipt_window.destroy()

    #View Receipt Button 
    view_receipt_button = tkinter.Button(frame_view_receipt, text="View Receipt",command=display_receipt)
    view_receipt_button.place(x=102.5, y=50, width=120)

    def return_view_receipt():
        window_view_receipt.destroy()

    #Return from view receipt button
    return_view_receipt_button = tkinter.Button(frame_view_receipt, text="Back",command=return_view_receipt)
    return_view_receipt_button.place(x=102.5, y=80, width=120)

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

#window mainloop 
window.mainloop()




