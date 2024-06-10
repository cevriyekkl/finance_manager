from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'
db = SQLAlchemy(app)

# Veritabanı modeli
class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    debt_amount = db.Column(db.Float, nullable=False)
    lender = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Veritabanını oluştur
with app.app_context():
    db.create_all()

@app.route('/record_debt', methods=['GET', 'POST'])
def record_debt():
    if request.method == 'POST':
        user_id = request.form['user_id']
        debt_amount = request.form['debt_amount']
        lender = request.form['lender']
        due_date = request.form['due_date']
        new_debt = Debt(
            user_id=user_id,
            debt_amount=debt_amount,
            lender=lender,
            due_date=datetime.strptime(due_date, '%Y-%m-%d')
        )
        db.session.add(new_debt)
        db.session.commit()
        flash('Debt recorded successfully', 'success')
        return redirect(url_for('record_debt'))
    return render_template('record_debt.html')

if __name__ == '__main__':
    app.run(debug=True)