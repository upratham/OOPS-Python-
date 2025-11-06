class chatbook:

    __user_id=0
    def __init__(self):  # Constructor/Magic method/dunder method
        self.__name = "Default User" # Encapsulation of Attribute
        self.user_id= chatbook.__user_id 
        chatbook.__user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    # Useing statis method we can use method directly from class rather than object. 
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(value):
        chatbook.__user_id=value


    def get_name(self):
        return self.__name 
    
    def set_name(self,value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to chat book !! how would you like to proceed?
                           1.Press 1 to signup
                           2.Press 2 to signin
                           3.press 3 to write post
                           4.press 4 to messaage a friend
                           5. Press any other key to exit""" )
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.mypost()
        elif user_input=='4':
            self.sendmsg()
        else:
            exit()


    def signup(self):
        email=input("Entyer you Email here :")
        pwd = input('Setup your password here :')
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print('\n')
        self.menu()

    def signin(self):
        if self.username == '' and self.password=='':
            print("Please Signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username")
            pwd= input("Enter your password here")
            if self.username == uname and self.password== pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()

    def mypost(self):
        if self.loggedin==True :
            txt=input("Enter your message here ->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin== True:
            txt=input("Enter your message here ->")
            frnd=input("whom to send th message ?")
            print(f"Your message has be sent to {frnd}")
        else:
            print("You need to sign up first")
        
        print("\n")
        self.menu()



#obj = chatbook()