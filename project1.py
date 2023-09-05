print("****************************************Welcome to Melon Contact Manager****************************************")
choice = input("Do you want to login[If You Have an Account] or Do you want to SignUp? login || signup : ")

if(choice=="login"):
    
 print("****************************************Enter your username and password****************************************")
 userName = input("Enter your username: ") 
 if userName in users:
    password = input("Enter your Password: ") 
    if password==users[userName]:
        print("Hello World")
    
        #go to the function where users can create their contact lists
    else:
     for i in range(1, 4):
        invalidPass= input("Invalid Password. Do you want to try again? Y||N : ") 
        if(invalidPass== "Y" or "y"):
          password = input("Re-enter your Password: ")
        else:
          print("Thank You!!! Good Bye!")
          break 
 else:
    for i in range(1,3):
      invalidUser=input('Invalid User name. Do you want to try again? (y/n):')
      if(invalidUser=="Y"):
          password = input("Re-enter your Password: ")
      else:
          print("Thank You!!! Good Bye!")   

else:
 users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

 print("****************************************Welcome our New user, kindly insert the required fields****************************************")
 userName = input('Enter your user Name: ')
 password = input('Enter your password: ')
 reEnter = input('ReEnter your password: ')
 if password == reEnter:
    users[userName] = password
    print(f'The username {userName} and password have been added to the dictionary for future use')
    print("Welcome")

 else:
    print('The entered passwords do not match')
#the function that executes the creation deletion and insertion of contacts would be called  
    



