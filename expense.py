from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('record_expense.html')

@app.route('/record_expense', methods=['POST'])
def record_expense():
    user_id = request.form['user_id']
    expense_amount = request.form['expense_amount']
    expense_type = request.form['expense_type']
    date = request.form['date']
    
    # record_expense fonksiyonunu çağır ve işlemleri gerçekleştir
    # Burada veritabanına kaydetme işlemini gerçekleştirmeniz gerekiyor.
    
    return "Expense recorded successfully"

if __name__ == '__main__':
    app.run(debug=True)