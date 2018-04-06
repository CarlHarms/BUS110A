import sqlite3
conn = sqlite3.connect("OS_Employee.db")

with conn:
    cur = conn.cursor()
    
  
    def RegisterNewUser():
        IDnumber= ""
        firstName = ""
        lastName = ""
        email = ""
        password = ""
        
        while not IDnumber:
            IDnumber = input("Please enter the employee ID that you want to register: ")
            if IDnumber:
                cur.execute("SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + IDnumber + "')")
                results = cur.fetchone()
                count = results[0]
                
                if count == 1:
                    print("This ID number is taken, please choose another\n")
                    IDnumber = ""
                    continue 
                    
              
        while not firstName:
            firstName = input("Please enter the first name of the employee you want to register: ")
            
            if not firstName:
                print("\na first name is required")
                firstName = ""
            else:
                firstName = firstName.title()
                firstName = firstName.strip()
    
            
        while not lastName:
            lastName = input("Please enter the last name of the employee you want to register: ")
            if not lastName: 
                print("\nA last name is required\n")
                lastName = ""
            else:
                lastName = lastName.title()
                lastName = lastName.strip()
                
        while not email:
            email = input("Please enter the email of the employee you want to register: ")
            if not email:
                print("\nan email is required\n")
                email = ""
            else:
                email = email.lower()
                email = email.strip()
                
        while not password:
            password = input("Please enter the password to be used for this user: ")
            if not password:
                print("\na password is required\n")
            else:
                password = password.title()
                password = password.strip()
                
        cur.execute("INSERT INTO Employee (EmployeeID,FirstName,LastName,Email,Password) VALUES ('" + IDnumber + "','" + firstName + "','" + lastName + "','" + email + "','" + password + "')")
        
        results = cur.fetchall()
        print(results)
        
    try:
        RegisterNewUser()
    except:
        print("Connection Failed")
