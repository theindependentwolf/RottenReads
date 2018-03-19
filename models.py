from rottenreads import db
from sqlalchemy.dialects.postgresql import JSON


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(), unique=True, nullable=False)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    added_by = db.Column(db.String(), nullable=False)
    added_date = db.Column(db.DateTime(), nullable=False)


    def __init__(self, isbn, title, author, description, added_by, added_date):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.description = description
        self.added_by = added_by
        self.added_date = added_date

    def __repr__(self):
        return 'isbn: {}\ntitle: {}\nauthor: {}\n'.format(self.isbn, self.title, self.author)



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
  
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<id {}>'.format(self.id)



class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    star = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String())
    added_by = db.Column(db.String(), nullable=False)
    added_date = db.Column(db.DateTime(), nullable=False)


    def __init__(self, isbn, title, star, comment, added_by, added_date):
        self.isbn = isbn
        self.title = title
        self.star = star
        self.comment = comment
        self.added_by = added_by
        self.added_date = added_date


    def __repr__(self):
        return 'isbn: {}\nStar: {}\nReview: {}'.format(self.isbn, self.star, self.comment)
