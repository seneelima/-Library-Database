
def librarian_menu():
    print("Press 1- Sign in \nPress 2- Register \nPress 3- Quit")
    while True:
        try:
            choice=int(input("Enter option:"))
            if choice<=3:
                break
            else:
                raise ValueError:
            except ValueError:
                print('Entry invalid,please try again')
            return choice

    def librarian_sign_in():
        email=input("Enter mail id: ")
        password=input("Enter password: ")
        return email,password
    def librarian_register_view():
        name=input('Enter name: ')
        email=input('Enter email: ')
        password=input('Enter password: ')
        phone=int(input('Enter phone number:'))
        return name,email,password,ph_no=view.librarian_register_view()
        self.cursor.execute('''
        insert)



