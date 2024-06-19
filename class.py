from tkinter import *

screen=Tk()

screen.geometry('400x600')
screen.maxsize(500,700)
screen.minsize(300,500)

User_name=Label(screen,text="Username",fg="red").place(x=2,y=10)
User_password=Label(screen,text="UserPassword",fg="red").place(x=2,y=40)

submit_button=Button(screen,text="Submit",width=55,bg="black",fg="white").place(x=4,y=80)

User_name_area=Entry(screen,width=20).place(x=80,y=10)
User_password_area=Entry(screen,width=20).place(x=80,y=40)

screen.mainloop()




#code
import tkinter as tk   

def on_button_click():
    user_input=entry.get()
    display_label.config(text=f"you entered:={user_input}")
    print(user_input)
    
    
root=tk.Tk()

root.geometry("400x300")
root.title("Tkinter Input File")

# create a lable
label=tk.Label(root,text="Enter something")
label.pack(pady=20)


# create an entry

entry=tk.Entry(root)
entry.pack(pady=5)

# create button

button=tk.Button(root,text="Submit",command=on_button_click)
button.pack(pady=10)

display_label=tk.Label(root,text='')
display_label.pack(pady=10)

root.mainloop()



#code1
import tkinter as tk

# Function to be called when the button is clicked
def on_button_click():
    label.config(text="Button clicked!")

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter Example")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click me", command=on_button_click)
button.pack(pady=10)

# Run the main event loop
root.mainloop()