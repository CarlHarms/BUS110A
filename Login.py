import sqlite3
conn = sqlite3.connect('OS_Employee.db')

cur=conn.cursor()

userEmail = ""
userPassword = ""

while not userEmail or not userPassword: 
    
    userEmail = input("Please enter your email: ")
    userPassword = input("Please enter your password: ")
    
    if not userEmail: 
        print("an email is required to log in\n") 
    else:
        userEmail = userEmail.lower()
        userEmail = userEmail.strip() 
        
    if userPassword:
        userPassword = userPassword.lower()
        userPassword = userPassword.strip()
    else:
        print("a password is necessary to login\n")

    with conn:
        try:
            cur.execute("SELECT COUNT (*) FROM Employee WHERE (Email =  '" + userEmail + "' AND Password = '" + userPassword + "') ")
            results = cur.fetchone()
            if results[0] == 1:
                print("\nLogin Successful\n")
            else: 
                print("\nLogin unsuccessful")
                
                userEmail = ""
                userPassword = ""
                #^^this makes the login menu loop over and over until a valid login is made
        except:
            print("connection failed")
