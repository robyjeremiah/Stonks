from tkinter import *   
def Login_check():      
    try:                

        file = open(username_in.get()+".txt","r") 
        user_check = file.readline()          
        password_check = file.readline()          
        
        user = username_in.get() + "\n"             

       
        if user == user_check and password_check == password_in.get():
            Label(screen2, text = "Welcome", fg = "green").pack()
        else:
            Label(screen2, text = "Incorrect Password", fg = "red").pack()
        file.close()


    except IOError:     
        Label(screen2, text = "Invaid Username", fg = "red").pack()
    
def regsiter_user():                    
    user_info = username.get()      
    password_info = password.get()      

    file = open(user_info+".txt","w")   
    file.write(user_info+"\n")          
    file.write(password_info)               
    file.close()                            
    username_entry.delete(0,END)           
    password_entry.delete(0,END)            

    Label(screen1, text = "Registration Successful!!", fg = "green").pack()

def register():                 

    global screen1
    screen1 = Toplevel(screen)  
    screen1.title("Register")   
    screen1.geometry("450x350") 

    Label(screen1, text = "").pack()
    Label(screen1, text = "").pack()

    Label(screen1, text = "Please Enter Details", width = "300" , height = "2" , font = ("Calibri", 13)).pack()
    

    global username
    global password
    global username_entry
    global password_entry

    image = StringVar()
    username = StringVar()
    password = StringVar()
 

    Label(screen1, text = "Upload an Image *").pack()
    image_entry = Entry(screen1, textvariable = image)
    image_entry.pack()
                       
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    Button(screen1, text = "Register", command = regsiter_user).pack()  
    

def login():                       
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("450x350")
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()

    Label(screen2, text = "Please Login", width = "300" , height = "2" , font = ("Calibri", 13)).pack()
    

    Label(screen2, text = "Please enter your credentials").pack()
    Label(screen2, text = "").pack()
    global username_in
    global password_in
    username_in = StringVar()
    password_in = StringVar()
    
    Label(screen2, text = "Username").pack()
    Entry(screen2, textvariable = username_in).pack()

    Label(screen2, text = "Password").pack()
    Entry(screen2, textvariable = password_in).pack()

    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", command = Login_check).pack()

def main_screen():    
    global screen
    screen = Tk()
    screen.geometry("450x350")
    screen.title("Stonks - Accounting Solutions")
    Label(text = "Stonks - Accounting Solutions", bg = "grey", width = "300" , height = "2" , font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "30" , height = "2", command = login  ).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30" , height = "2", command = register ).pack()

    screen.mainloop()
main_screen()
    