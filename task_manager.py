#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
from datetime import datetime
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
def login_details ( username, password):
   with open("user.txt", "r") as file:
    for line in file:
        u,p = line.strip().split(",")
        p = p.strip()
      

        if u == username and p == password:
            print("welcome back") 
            return True 
        #else:
    print(" incorrect username or password \n", "please contact Adminstrator for access")
    return False

def new_user():
    with open("user.txt", "a") as file:
        new_username = input("Please enter a username: ")
        new_password = input("Please enter your password: ")
        password_check = input("Please re-enter the password: ")

        if new_password == password_check:
            file.write("\n" + new_username + "," + new_password)
            print("Welcome", new_username)
        else:
            print("Passwords do not match. Please try again.")

def access ():

    valid_user = False

    while not valid_user:
        
        username = input("please enter username:")
        pasword = input ("please enter your password:")
        valid_user=login_details(username,pasword)
    return username

           
        

    
    
        

print(" Welcome to LET'S work task manager")
current_user = access()


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if current_user == "admin":
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    ds - display statistics (total tasks & users)    
    e - exit
    : ''').lower()

    else:
        menu = input('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

    if menu == 'r' and current_user == "admin":
        
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        new_user()
    
    elif menu == 'a':
        
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        file= open("tasks.txt","a+")
        username = input("please enter your username:")
        assigned = input("please user the task will be asissgned too :")
        title = input("enter the task title :")
        task_descr = input("please give a task description:")
        date_assigned = datetime.now().strftime("%d %b %Y")
        due_date = input("please enter the due date (DD MMM YYYY):")
        status = "no"
        file.write(f"\n{assigned}, {title}, {task_descr}, {due_date}, {date_assigned}, {status}")
        
        file.close()
        

    elif menu == 'va':
        
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        file =open("tasks.txt","r")
        tasks= file.readlines()
        for line in tasks :
            task_info = line.strip().split(", ")
        
            print(f"Task :", task_info[1])
            print(f"Assigned to :", task_info[0])
            print(f"Date Assigned :", task_info[3])
            print(f"Due Date :", task_info[4])
            print(f"Task complete? :", task_info[5])
            print(f"Task Description :", task_info[2])
        
            
             

        file.close()

    elif menu == 'vm':
        
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        file =open("tasks.txt","r")
        tasks= file.readlines()
        
        for line in tasks :
            
            task_info = line.strip().split(", ")
            if task_info[0] == current_user:
        
        
                
                print(f"Task :", task_info[1])
                print(f"Assigned to :", task_info[0])
                print(f"Date Assigned :", task_info[3])
                print(f"Due Date :", task_info[4])
                print(f"Task complete? :", task_info[5])
                print(f"Task Description :", task_info[2])
        file.close()

    elif menu == 'ds':

        with open("user.txt","r") as file:
            total_users = len(file.readlines())

        with open("tasks.txt","r") as file:
            total_tasks = len(file.readlines())

            print(f"the total number of users: {total_users}")
            print(f"the total number of tasks: {total_tasks}")
    
   
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")