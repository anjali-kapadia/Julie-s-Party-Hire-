#Anjali Kapadia - 16.08.24
#Purpose : To help Julie with her party hire store. 
import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

used_receipt_numbers = set()

#def function to load the receipt number to text file
def used_receipt_number():
    with open("Julie's party hire.txt", "r") as file:
        for line in file:
            receipt_number = (line.strip().split(",")[0])
            used_receipt_numbers.add(receipt_number)
            
#def function to generate receipt number
def generate_receipt_number():
    while True:
        randInt = random.randint(100000, 999999)
        if randInt not in used_receipt_numbers:
            used_receipt_numbers.add(randInt)
            return randInt
            
used_receipt_number()

#Main Window
window = tkinter.Tk()
window.title("Julie's Party Hire")
window.geometry('350x350')

#window colour
window.configure(bg="#ffbac4")

#frame for main window
frame = tkinter.Frame(window, width=310, height=320, bg='#b6e5f9')
frame.pack(padx = 10, pady=10)

#heading image (logo) 
logo = Image.open("heading.png").resize((130, 60))
logo_image = ImageTk.PhotoImage(logo)

img_label = tkinter.Label(frame, image=logo_image)
img_label.image = logo_image  
img_label.place(x=90, y=10, width=130, height=60)

#Hire Window
def hire():
    window_hire = tkinter.Toplevel()
    window_hire.title("Hire Page - Julie's Party Hire")
    window_hire.geometry('350x350')
    
    #hire window colour
    window_hire.configure(bg="#ffbac4")

    #frame for hire window
    frame_hire = tkinter.Frame(window_hire,width=310, height=320, bg='#b6e5f9')
    frame_hire.pack(padx = 10, pady=10)

    #def function to generate new receipt number for each transaction
    def new_receipt_number():
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
    
    #inserting logo
    logo = Image.open("heading.png").resize((130, 60))
    logo_image = ImageTk.PhotoImage(logo)

    img_label = tkinter.Label(frame_hire, image=logo_image)
    img_label.image = logo_image  
    img_label.place(x=90, y=10)
                        

    #first name label
    first_name = tkinter.Label(frame_hire, text="First Name :", bg='#7cd8f0', fg='#fdfdfd')
    first_name.pack(padx=10, pady=10)
    first_name.place(x = 15, y = 85, width=110)

    #first name entry box
    global first_name_entry
    first_name_entry = tkinter.Entry(frame_hire)
    first_name_entry.pack(padx=10, pady=10)
    first_name_entry.place (x = 135, y = 85, width = 160)

    #validation for last name
    #function to check the length
    def check_length(last_name):
        return len(last_name) <= 20

    #function to check if input is empty
    def check_empty(last_name):
        return last_name != ""

    #function to check if the input contains only alphabets
    def check_input(last_name):
        return last_name.isalpha()

    #last name label
    last_name = tkinter.Label(frame_hire, text="Last Name :", bg='#7cd8f0', fg='#fdfdfd')
    last_name.pack(padx=10, pady=10)
    last_name.place (x=15, y=120, width=110)

    #last name entry box
    global last_name_entry
    last_name_entry = tkinter.Entry(frame_hire)
    last_name_entry.pack(padx=10, pady=10)
    last_name_entry.place (x = 135, y = 120, width = 160)

    #def function for combo box for Item to hire
    def show_item_to_hire(event) :
        item_to_hire = item_hire_combo.get()

    #Item to hire label
    item_hire = tkinter.Label(frame_hire, text="Item to hire :", bg='#7cd8f0', fg='#fdfdfd')
    item_hire.pack(padx=10, pady=10)
    item_hire.place(x = 15, y = 155, width=110)

    #Item to hire combo box
    global item_hire_combo
    item_hire_combo = ttk.Combobox(frame_hire, values=["Spoons","Forks","Knives","Balloons","Cake Stand","Birthday Banner"], state="readonly")
    item_hire_combo.pack(padx=10, pady=10)
    item_hire_combo.place(x = 135, y = 155, width = 160)
    item_hire_combo.bind("<<ComboboxSelected>>", show_item_to_hire)

    #validation for quantity hire
    def check_value(quantity_hire_spinbox):
        try:
            value = int(quantity_hire_spinbox)
            return 1 <= value <= 500
        except ValueError:
            return False

    #label for quantity to hire
    quantity_hire = tkinter.Label(frame_hire, text="Quantity to hire :", bg='#7cd8f0', fg='#fdfdfd')
    quantity_hire.pack(padx=10, pady=10)
    quantity_hire.place(x = 15, y = 190, width=110)

    #spin box for quantity to hire
    global quantity_hire_spinbox
    quantity_hire_spinbox = tkinter.Spinbox(frame_hire, from_=1, to=500)
    quantity_hire_spinbox.pack(padx=10, pady=10)
    quantity_hire_spinbox.place(x = 135, y=190, width=160)

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
            messagebox.showerror("Input Error", "First name must be less than 20 characters long.")
        elif not check_input(first_name):
            messagebox.showerror("Input Error", "First name must contain only letters.")
        elif not check_empty(last_name):
            messagebox.showerror("Input Error", "Last name cannot be blank.")
        elif not check_length(last_name):
            messagebox.showerror("Input Error", "Last name must be less than 20 characters long.")
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
                window_hire_receipt.configure(bg="#ffbac4")

                #def function for return button
                def return_from_hire_page():
                    window_hire_receipt.destroy()
                    
                #frame for hire receipt
                frame_hire_receipt = tkinter.Frame(window_hire_receipt, bg='#b6e5f9')
                frame_hire_receipt.pack(padx=20, pady=20)

                #labels for receipt 
                tkinter.Label(frame_hire_receipt, text=f"Receipt Number: #{receipt_number}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"First Name: {first_name}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"Last Name: {last_name}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"Item Hired: {item_hire}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                tkinter.Label(frame_hire_receipt, text=f"Quantity Hired: {quantity_hire}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)

                #return from hire receipt button
                return_from_hire_button = tkinter.Button(frame_hire_receipt, text="Back", command=return_from_hire_page,bg='#7cd8f0', fg='#fdfdfd')
                return_from_hire_button.pack(pady=5)


            #Show message that hire information is added
            receipt_number = new_receipt_number()
            with open("Julie's party hire.txt","a") as file:
                file.write(f"{receipt_number},{first_name} ,{last_name}, {item_hire}, {quantity_hire}\n")
            #reset inputs
            first_name_entry.delete(0, tkinter.END)
            last_name_entry.delete(0, tkinter.END)
            item_hire_combo.set('')
            quantity_hire_spinbox.delete(0, tkinter.END)
            #message for hire success
            messagebox.showinfo("Info", "Item hired successfully!")
            hire_receipt(receipt_number, first_name, last_name, item_hire, quantity_hire)   

    
    #add to hire button
    print_receipt = tkinter.Button(frame_hire, text="Print Receipt", command=validate_inputs, bg='#7cd8f0', fg='#fdfdfd')
    print_receipt.place(x=95, y=240, width = 120)

    #homepage button code
    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Hire page","Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            window_hire.destroy()

    homepage_button = tkinter.Button(frame_hire, text="Homepage", command=homepage, bg='#7cd8f0', fg='#fdfdfd')
    homepage_button.place(x=95, y =270, width=120)

#Hire button
hire_button = tkinter.Button(frame, text="Hire",command=hire, bg='#7cd8f0', fg='#fdfdfd')
hire_button.place(x=95, y=90, width=120)

  
def save_return():
    #find receipt number from combobox
    receipt_number = receipt_combo.get().strip()

    if not receipt_number:
        tkinter.messagebox.showerror("Error", "Receipt number cannot be empty.")
    else:
        found = False
        with open("Julie's party hire.txt", "r") as file:
            for line in file:
                item = line.strip().split(",")
                if item[0] == receipt_number:
                    #found the item with the matching receipt number
                    found = True
                    item_details = (
                        f"Receipt Number: {item[0]}\n"
                        f"Name: {item[1]} {item[2]}\n"
                        f"Item Hired: {item[3]}\n"
                        f"Quantity Hired: {item[4]}")
                    
                    #show item details in the messagebox for confirmation
                    save_return_question = tkinter.messagebox.askquestion("Save",f"Are you sure you would like to return this item?\n\n{item_details}",icon="warning")
                    if save_return_question == "yes":
                            #update record and write to file
                            updated_lines = []
                            with open("Julie's party hire.txt", "r") as file:
                                for line in file:
                                    item = line.strip().split(",")
                                    if item[0] == receipt_number:
                                        record_deleted = True
                                    else:
                                        updated_lines.append(line)
                            

                    #updated records back to file
                    with open("Julie's party hire.txt", "w") as file:
                        file.writelines(updated_lines)
                        tkinter.messagebox.showinfo("Success", "Return Successful!\nReceipt deleted as quantity hired became zero")


def return_r():
    #frame for return window
    window_return = tkinter.Toplevel()
    window_return.title("Return Page - Julie's Party Hire")
    window_return.geometry('350x220')
    window_return.configure(bg="#ffbac4")

    #frame for return window
    frame_return = tkinter.Frame(window_return,width=310, height=190, bg='#b6e5f9')
    frame_return.pack(padx = 10, pady=10)

    #image for heading on return page
    logo = Image.open("heading.png").resize((130, 60))
    logo_image = ImageTk.PhotoImage(logo)

    img_label = tkinter.Label(frame_return, image=logo_image)
    img_label.image = logo_image  
    img_label.pack(padx=10, pady=10)
    img_label.place(x=90, y=10)

    #receipt number label
    receipt_number = tkinter.Label(frame_return, text="Receipt Number:",bg='#7cd8f0', fg='#fdfdfd')
    receipt_number.pack(padx=10,pady=10)
    receipt_number.place(x=15,y=85,width=110)

    #receipt combobox
    global receipt_combo
    receipt_combo = ttk.Combobox(frame_return, values=list(used_receipt_numbers),state="readonly")
    receipt_combo.pack(padx=10, pady=10)
    receipt_combo.place(x=145, y=85, width =155)
    receipt_combo.bind("<<ComboboxSelected>>")

    #save button
    save_button = tkinter.Button(frame_return, text="Save", command=save_return,bg='#7cd8f0', fg='#fdfdfd')
    save_button.place(x=95, y=120, width=120)

    #back button on return page
    def return_back_r():
        window_return.destroy()

    return_back = tkinter.Button(frame_return, text="Back", command=return_back_r,bg='#7cd8f0', fg='#fdfdfd')
    return_back.place(x=95, y=150, width=120)

#Return Button
return_button = tkinter.Button(frame, text="Return",command=return_r, bg='#7cd8f0', fg='#fdfdfd')
return_button.pack(padx=10, pady=40)
return_button.place(x=95, y=140, width=120)

#def function for view receipt button
def view_receipt():
    window_view_receipt = tkinter.Toplevel()
    window_view_receipt.title("View Receipt - Julie's Party Hire")
    window_view_receipt.geometry('350x175')
    window_view_receipt.configure(bg="#ffbac4")

    #frame for view receipt window
    frame_view_receipt = tkinter.Frame(window_view_receipt, width=310, height=145, bg='#b6e5f9')
    frame_view_receipt.pack(padx=10, pady=10)
    
    #receipt number label
    receipt_number = tkinter.Label(frame_view_receipt, text="Receipt Number:",bg='#7cd8f0', fg='#fdfdfd')
    receipt_number.pack(padx=10,pady=10)
    receipt_number.place(x=20,y=15,width=100)

    #receipt combobox
    global receipt_combo
    receipt_combo = ttk.Combobox(frame_view_receipt, values=list(used_receipt_numbers),state="readonly")
    receipt_combo.place(x=130, y=15, width=175)

    #validation for receipt combobox
    def display_receipt():
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
                    #find receipt from combobox, and details inputted loads
                    receipt_window = tkinter.Toplevel()
                    receipt_window.title("Receipt - Julie's Party Hire")
                    receipt_window.configure(bg="#ffbac4")

                    #back receipt command
                    def back_receipt():
                        receipt_window.destroy()

                    #receipt window
                    receipt_frame = tkinter.Frame(receipt_window, bg='#b6e5f9')
                    receipt_frame.pack(padx=20, pady=20)

                    #labels for receipt 
                    tkinter.Label(receipt_frame, text=f"Receipt Number: {item[0]}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"First Name: {item[1]}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"Last Name: {item[2]}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"Item Hired: {item[3]}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)
                    tkinter.Label(receipt_frame, text=f"Quantity Hired: {item[4]}",bg='#7cd8f0', fg='#fdfdfd').pack(pady=5)

                    #back code 
                    return_button = tkinter.Button(receipt_frame, text="Back",command=back_receipt,bg='#7cd8f0', fg='#fdfdfd')
                    return_button.pack(pady=5)

                    found = True
                    break
                
    #def function for View All button 
    def display_receipts():
        #window for view all window 
        display_window = tkinter.Toplevel()
        display_window.title("Display Receipts - Julie's Party Hire")
        display_window.geometry("350x350")
        display_window.configure(bg="#ffbac4")

        #frame for view all window 
        display_frame = tkinter.Frame(display_window,bg='#b6e5f9',width=310, height=320)
        display_frame.pack(padx=10, pady=10)

        #variable text for receipt
        receipt_data = tkinter.Text(display_frame, width=80, height=20)
        receipt_data.pack(padx=10, pady=10)

        #open hire details and print it out 
        with open("Julie's Party Hire.txt", "r") as file:
                    lines = file.readlines()
                    if lines:
                            for line in lines:
                                    data = line.strip().split(",")
                                    receipt_data.insert(tkinter.END, f"Receipt Number: {data[0]}\n")
                                    receipt_data.insert(tkinter.END, f"First Name: {data[1]}\n")
                                    receipt_data.insert(tkinter.END, f"Last Name: {data[2]}\n")
                                    receipt_data.insert(tkinter.END, f"Item: {data[3]}\n")
                                    receipt_data.insert(tkinter.END, f"Amount: {data[4]}\n")
                                    receipt_data.insert(tkinter.END, "-"*40 + "\n")
                    else:
                        receipt_text.insert(tkinter.END, "No receipts found.")

        def back_display():
            display_window.destroy()
             
        return_button = tkinter.Button(display_window, text="Back", command=back_display, bg='#7cd8f0', fg='#fdfdfd')
        return_button.place(x=125, y=310, width=100)


    #view all receipts button
    view_all = tkinter.Button(frame_view_receipt, text="View All", command=display_receipts, bg='#7cd8f0', fg='#fdfdfd')
    view_all.place(x=102.5, y=80, width=120)

            
    #back receipt button command       
    def back_receipt():
        receipt_window.destroy()

    #View Receipt Button 
    view_receipt_button = tkinter.Button(frame_view_receipt, text="View Receipt",command=display_receipt,bg='#7cd8f0', fg='#fdfdfd')
    view_receipt_button.place(x=102.5, y=50, width=120)

    def return_view_receipt():
        window_view_receipt.destroy()

    #Return from view receipt button
    return_view_receipt_button = tkinter.Button(frame_view_receipt, text="Back",command=return_view_receipt, bg='#7cd8f0', fg='#fdfdfd')
    return_view_receipt_button.place(x=102.5, y=110, width=120)

#View Receipt Button
reciept_button = tkinter.Button(frame, text="View Receipt",command = view_receipt, bg='#7cd8f0', fg='#fdfdfd')
reciept_button.place(x=95, y=190, width=120)

#Command for quit button
def quit_b():
    question_box = tkinter.messagebox.askquestion("Exit Julie's Party Hire","Are you sure you would like to Quit?", icon="warning")
    if question_box == "yes":
            window_hire.destroy()

#Quit Button
quit_button = tkinter.Button(frame, text="Quit",command=quit_b, bg='#7cd8f0', fg='#fdfdfd')
quit_button.place(x=95, y=240, width=120)

#window mainloop 
window.mainloop()




