from flask import Blueprint, render_template, request
from .model import Expenses
from .database import db
from flask_sqlalchemy import extract

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template("index.html")

@main.post("/expenses")
def add_expenses():
    data = request.get_json()
    new_expense = Expenses(data["title"], data["amount"], data["category"])
    db.session.add(new_expense)
    db.session.commit()
    return {"message": "Expenses Tracked successfully"}, 200

@main.get("/expenses")
def get_expenses():
    expenses = Expenses.query.all()
    expense_list = []
    for expense in expenses:
        expense_list.append({
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date
        })
        return expense_list, 200
    return {"message": "No expenses found"}, 401

@main.get("/expenses/<int:id>")
def get_single_expense(id):
    expenselist = []
    expenses = Expenses.query.all()
    for expense in expenses:
        if expense.id == id:
            return{
                "title": expense.title,
                "amount": expense.amount,
                "category": expense.category,
                "date": expense.date
            }
    return {"message": "No expenses found"}, 401
    

@main.put("/expenses/<int:id>")
def update_expenses(id):
    expenses = Expenses.query.get(id)
    data = request.get_json()
    if expenses != None:
        expenses.title = data.get("title", expenses.title)
        expenses.amount = data.get("amount", expenses.amount)
        expenses.category = data.get("category", expenses.category)
        expenses.date = db.func.current_timestamp()
        db.session.add(expenses)
        db.session.commit()
        return {"message": "Expenses Updated successfully"}, 200
    return {"message": "Task not found"}, 401

@main.delete("/expenses/<int:id>")
def delete_task(id):
    expense = Expenses.query.get(id)
    if expense is not None:
        db.session.delete(expense)
        db.session.commit()
        return {"message": "Expenses Deleted successfully"}, 200
    return {"message": "Task not found"}, 401

@main.get("expenses/month/<int:month>/total")
def get_month_total(month):
    total = 0
    expenselist = []
    expenses = Expenses.query.filter(extract("month", Expenses.date) == month).all()
    if expenses == None:
        return {"message": "Task not found"}, 401
    for expense in expenses:
        total += expense.amount
    return {"total": total}, 200