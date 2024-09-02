#login system, ask for username and password, or to create an account, email, username, password, confirm password and store info into text file
#allow user to login, save information and validate against the text file

#GLOBAL VARIABLES
message = "Thanks for visiting our website!"
MAX_ATTEMPTS = 4

def create_password():
    file = open("userpass.txt","a")
    
    password = str(input("Please enter your password: "))
    confpassword = str(input("Please confirm your password: "))
    while password != confpassword:
        confpassword = str(input("Please confirm your password: "))
    file.write(password + "\n")

    qq = str(input("Would you like to login? "))
    if qq.lower() == "yes":
        login_menu()
    else:
        print("Thank you for creating an account with us!")
        
    for line in file:
        print(line)
    
    file.close()
    

def login_create():

        
    file = open("userpass.txt","a")
        
    email = str(input("Please enter your email: "))
    file.write(email + "\n")
        
    user = str(input("Please enter your username: "))
    file.write(user + "\n")
    
    create_password()
        
    file.close()


def reset_password():
    file = open("userpass.txt","r")
    
    email = str(input("Please enter email: "))
    
    for line in file:
        if line == email:
            file = open("userpass.txt","a")
            create_password()
        else:
            print("Please create an account")
            login_create()
    
    file.close()
        

def login_menu():
    
    file = open("userpass.txt","r")
    content = file.read()
    login_user = str(input("Please type username: "))
    counter = 0
    
    while counter < MAX_ATTEMPTS:
        if login_user in content:
            password = str(input("Please enter your password: "))
            
            if password in content:
                print("You have successfully logged in!")
                return message
            else:
                password = str(input("Please enter your password: "))
                counter = counter + 1
        else:
            login_user = str(input("Please type username: "))
            counter = counter + 1
    
    if counter == MAX_ATTEMPTS:
        redo = str(input("Would you like to create an account? "))
        if redo.lower() == "yes":
            login_create()
        else:
            reset_password()
    
    file.close()


login_q = str(input("Do you have an account with us? "))
if login_q.lower() == "no":
    login_create()
if login_q.lower() == "yes":
    login_menu()
            
                
        
        
        