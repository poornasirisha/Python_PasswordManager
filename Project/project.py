#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Project answers


user_dic={}
count=0
flag=0


def unlock_acc():
    print("---------------------------------------------")
    id=input("Enter your User-id")
    temp=check_use(id)
    if(temp==1):
        if(user_dic[id][1]=="Active"):
            print("Account is already active")
        else:
            user_dic[id][1]="Active"
            print("Account has been unlocked")

        print("---------------------------------------------")
        menu()

    def menu():
        print("Welcome to IT Support Password Management Application")
        print("--------------------------------------------------------")
        print("1 Display all the users")
        print("2 Create new user account ")
        print("3 Update user password")
        print("4 Unlock use Account")
        print("5 exit application")

        ans=int(input("Enter your choice : "))

        if(ans==1):
            display_user()
        elif(ans==2):
            create_user()
        elif(ans==3):
            update_pw()
        elif(ans==4):
            unlock_acc()
        elif(ans==5):
            print("Exited")
        else:
            print("Enter valid response")
            menu()

    def display_user():
        print("---------------------------------------------")
        print("user-id password status ")
        for key in user_dic:
            print("{} {} {}".format(key,user_dic[key][0],user_dic[key][1]))

        print("---------------------------------------------")
        menu()

    def create_user():
        print("---------------------------------------------")
        user_name=input("Enter your username")
        user_dic[user_name]=["p@sswOrd","Active"]

        print("---------------------------------------------")
        menu()



    def update_pw():
        print("---------------------------------------------")
        id=input("Enter your User-id")
        temp=check_use(id)
        if(temp==1):
            pas=input("Enter you new passwor")
            while(len(pas)<6):
                print("Password must contain at least 6 char")
                pas=input("Enter you new passwor")

            user_dic[id][0]=pas
        print("---------------------------------------------")

        menu()









    def check_use(id):

        global flag
        if id in user_dic:
            flag=1

        else:
            print("Invalid user id")
        return flag 



    menu() 


# ## Answer for Task 1 in Project

# In[12]:


def menu():
    print("IT support password management application")
    print("*"*100)


    print("\t1.Display all user accounts")
    print("\t2.Create new user accounts")
    print("\t3.Update user password")
    print("\t4.Unlock user account")
    print("\t5.Exit Application")
    print(" "*100)
    print(" "*100)
    print(" "*100)
    option = int(input('Enter your option[1-5]'))
    
    return option


# ## Answer for Task 2

# In[10]:


users = {'abc':['234569','active'],'pqr':['455566','active'],'xyz':['658675','locked']}
    
def display_users():
    
    print("-"*50)
    
    print("{0:<15} {1:<15} {2:<20}".format("User ID", "Password", "Account Status"))
    
    
    print("-"*50)
    
    for user in users:
        
        print("{0:<15} {1:<15} {2:<20}".format(user, users[user][0], users[user][1]))


# In[11]:


display_users()


# ## Answer for Task3

# In[14]:


def create_user():
    
    userID = input("Enter new user ID: ")
    password = "p@ssw0rd"
    status = "active"
    
    users[userID] = [password, status]


# In[16]:


def unlock_account():
    
    userID = Check_user()
    
    if userID == "exit":
        pass
    elif users[userID][1] == 'locked':
        users[userID][1] == 'active'
        print("Account for {} has been unloacked successfully".format(userID))
    else:
        print("Account for {} is already active".format(userID))


# In[22]:


def update_pw():
    userID = check_user()
    
    while userID != 'exit':
        password = input('Enter new password:')
    if len(password) <6:
        print('Password must contain atleast 6 characters')
    else:
        users[user][0] = password
break


# In[23]:


def Check_user():
    while True:
        userID = input('Enter new user ID:')
        if userID == 'exit':
            return userID
        elif userID not in users:
            print('Invalid user ID. ')
        else:
            return userID


# In[24]:


option = 0


# In[25]:


while option != 5:
    option = menu()
    
    print()
    
    if option == 1:
        display_users()
    elif option == 2:
        create_user()
    elif option == 3:
        update_pw
    elif option == 4:
        unlock_account()
    else:
        continue
    print()


# In[ ]:




