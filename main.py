'''Library management application'''

import model
import view

#librarian_menu={1:librarian_sign_in,2:store_book,3:delete_book,4:view_all_books,5:update_book_author,6:update_book_title}
#user_menu={1:user_registration,2:view_all_books,3:rent_book,4:return_book,5:delete_user,6:update_email}



def main():
    key=True
    while key:
        choice=view.librarian_menu()
        if choice==3:
            key=False
        elif choice==1:
            email,password=view.librarian_sign_in()
            librarian=model.librarian_sign_in(email,password)
            if librarian[0]:
                print('Success login and now you can perform librarian activity functions')
                # librarian_activity()# this function will call the various actions that can be performed
                librarian_activity()
            else:
                key=False
        elif choice==2:
            model.librarian_register()

   if__name__=="__main__":
        model.Library.connect()
        model.Library.create_tables()
        model.Library.insert_librarian()
        main()

