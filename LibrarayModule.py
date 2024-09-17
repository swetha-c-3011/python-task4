class Book:

    def __init__(self,title,author,bookId):
        self.title=title
        self.author=author
        self.bookId=bookId
        self.book_dict={
            "title": title, "author": author, "book_Id": bookId
        }

    def display_book_details(self):

         print(self.title,self.author,self.bookId)

class Library:
    booklist = []
    def __init__(self):
        pass



    def add_book(self,title,author,bookId):
         if not any(d['book_Id'] == bookId for d in Library.booklist):

             book_obj=Book(title,author,bookId)
             Library.booklist.append(book_obj.book_dict)
             print(Library.booklist)

         else:
             print(f"Book with ID {bookId} already exists.")


    def remove_book(self,bookId):

        if  any(d['book_Id'] == bookId for d in Library.booklist):
            for item in range(len(self.booklist)):
                if(Library.booklist[item]['book_Id']==bookId):
                    del Library.booklist[item]
                    print("book id ",bookId," deleted")
                    break
        else:

            print("there is no book id ",bookId)

    def search_book(self,title):
        if any(d['title']==title for d in Library.booklist):
         for item in range(len(Library.booklist)):
             if (Library.booklist[item]['title']==title):
                 print(Library.booklist[item])
                 break
        else:
            print("the title you are searching for is not there")

    def __iter__(self):
        for books in Library.booklist:
            yield books


class User:
    borrow_lst = []
    lis_of_user = []
    def __init__(self,name,userid):
        self.name=name
        self.userid=userid
        self.user_detail={
            "name":name,
            "userid":userid
        }

    def display_user_details(self):

        print(User.lis_of_user)

class LibraryUser(User):
    def __init__(self, name, userid,library,userobj):
        super().__init__(name, userid)
        self.borrow_dict={}

        self.library = library
        self.userobj=userobj

        if not any(d['userid'] == userobj.userid for d in User.lis_of_user):
            User.lis_of_user.append(self.userobj.user_detail)

    def borrow_book(self,bookId,userid):


            if  any(d['book_Id']==bookId for d in Library.booklist ):
                if not any (d['bookId']== bookId for d  in User.borrow_lst) :
                    self.borrow_dict={
                        "userid":userid,
                        "bookId":bookId
                    }
                    User.borrow_lst.append(self.borrow_dict)
                    print("please ,Return the book without any damages")
                else:
                    print(f"bookId : {bookId}  is already borrowed ")
            else:
                 print(f"There is no bookId  {bookId}")


    def return_book(self,bookId):

            if any(d['bookId'] == bookId for d in User.borrow_lst):
                for i in range(len(User.borrow_lst)):
                    if (User.borrow_lst[i]['bookId'] == bookId):
                        del User.borrow_lst[i]
                        print("Thank you,Visit Again")
                        break
            else:
                print("book_Id is not borrowed")


    def track_borrowed_books(self):
        print("borrowed list ",User.borrow_lst)




