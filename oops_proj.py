class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

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
            print("You need to sugn in first")
        
        print("\n")
        self.menu()



#obj = chatbook()