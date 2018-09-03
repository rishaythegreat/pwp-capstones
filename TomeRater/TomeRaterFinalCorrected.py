class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{user}'s email has been updated to {email}.".format(user=self.name, email=self.email))

    def __repr__(self):
            return "Reviewer: {name}, email: {email}, read: {read}".format(name=self.name, email=self, read=len(self.books))

    def __eq__(self, other_user):
            return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
            self.books[book] = rating

    def get_average_rating(self):
        rating_total = 0
        for value in self.books.values():
            if value != None:
                rating_total += value
        return rating_total / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

    def change_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{}'s ISBN has been updated to {}.".format(self.title, self.isbn))

    def add_rating(self, rating):
        if rating is not None and rating >= 0 and rating <= 4:
            self.rating.append(rating)
        else:
            return "Invalid Rating, please enter between 0 and 4!"

    def get_average_rating(self):
        sumkeeper = 0
        for rating in self.rating:
            sumkeeper += rating
        return sumkeeper / len(self.rating)


    def __eq__(self,other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().init(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().init(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} book about {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users[email]
            if book:
                user.read_book(book, rating)
                book.add_rating(rating)
            else:
                print("Book is not yet in collection.")
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user found")

    def add_user(self, name, email, user_books=None):
        if email not in self.users:
            user = User(name, email)
            self.users[email] = user
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_book_catalog(self):
        for book in self.books:
            print(book)

    def print_TomeRater_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read = None
        num_of_reads = 0

        for book, read in self.books.items():
            if reads > num_of_reads:
                num_of_reads = reads
                most_read = book
        return most_read

    def highest_rated_book(self):
        top_rating = 0
        top_book = None

        for book in self.books.keys():
            book_avg_num = book.get_average_rating()
            if book_avg_num > top_rating:
                top_rating = book_avg_num
                top_book = book
        return top_book

    def most_positive_user(self):
        highest_ratings = 0
        positive_user = None
        for user in self.users.values():
            user_avg_rating = user.get_average_rating()
            if user_avg_rating > highest_ratings:
                highest_ratings = user.get_average_rating()
                postive_user = user
        return positive_user

    def get_most_read_book(self):
        book_count = 0
        most_read = None
        for book in self.books:
            if self.books[book] > book_count:
                book_count = self.books[book]
                most_read = book
        return most_read
