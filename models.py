from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    books = db.relationship('Book', backref='creator', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    reviews = db.relationship(
        'Review',
        backref='book',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Book {self.title}>'


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __repr__(self):
        return f'<Review {self.rating}/5>'

