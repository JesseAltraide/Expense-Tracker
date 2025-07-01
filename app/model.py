from flask_sqlalchemy import SQLAlchemy
from .database import db

class Expenses (db.Model):
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category
    
    id = db.Column("id", db.Integer, primary_key = True)
    title = db.Column("title",db.String(100), nullable = False)
    amount = db.Column("amount", db.Integer, nullable = False)
    category = db.Column("category", db.String(50), nullable = False)
    date = db.Column("date", db.String, nullable = False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Spent ${self.amount} on {self.title}"