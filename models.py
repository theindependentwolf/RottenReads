from rottenreads import db
from sqlalchemy.dialects.postgresql import JSON


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.String(), unique=True, nullable=False)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    added_by = db.Column(db.String(), nullable=False)
    added_date = db.Column(db.DateTime(), nullable=False)
    result_all = db.Column(JSON)


    def __init__(self, ISBN, title, description, added_by, added_date, result_all):
        self.ISBN = ISBN
        self.title = title
        self.description = description
        self.added_by = added_by
        self.added_date = added_date
        self.result_all = result_all

    def __repr__(self):
        return '<id {}>'.format(self.id)



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
    ISBN = db.Column(db.String(), nullable=False)
    star = db.Column(db.String(), nullable=False)
    comment = db.Column(db.String())
    added_by = db.Column(db.String(), nullable=False)
    added_date = db.Column(db.DateTime(), nullable=False)
    result_all = db.Column(JSON)


    def __init__(self, ISBN, star, comment, added_by, added_date, result_all):
        self.ISBN = ISBN
        self.title = title
        self.description = description
        self.added_by = added_by
        self.added_date = added_date
        self.result_all = result_all


    def __repr__(self):
        return '<id {}>'.format(self.id)
