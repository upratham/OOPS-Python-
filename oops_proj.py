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
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()


obj = chatbook()