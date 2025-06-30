from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expenses (db.Model):
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    title = db.Column("title",db.String(100), nullable = False)
    amount = db.Column("amount", db.Integer, nullable = False)
    category = db.Column("category", db.String(50), nullable = False)
    date = db.Column("date", db.String, nullable = False)

    def __repr__(self):
        return f"Spent ${self.amount} on {self.title}"