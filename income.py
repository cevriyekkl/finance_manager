from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('record_income.html')

@app.route('/record_income', methods=['POST'])
def record_income():
    user_id = request.form['user_id']
    income_amount = request.form['income_amount']
    income_source = request.form['income_source']
    frequency = request.form['frequency']
    
    # Burada record_income fonksiyonunu çağırabilir ve işlemleri gerçekleştirebilirsiniz
    
    return "Income recorded successfully"

if __name__ == '__main__':
    app.run(debug=True)