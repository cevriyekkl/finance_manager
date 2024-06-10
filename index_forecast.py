from flask import Flask, render_template, request
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)

# Veritabanı yerine örnek borç verileri
sample_debts = [
    {"date": "2024-01-01", "debt_amount": 100},
    {"date": "2024-02-01", "debt_amount": 150},
    {"date": "2024-03-01", "debt_amount": 200},
    {"date": "2024-04-01", "debt_amount": 250},
    {"date": "2024-05-01", "debt_amount": 300}
]

@app.route("/")
def index():
    return render_template("index.html", debts=sample_debts)

@app.route("/track_debt", methods=["POST"])
def track_debt():
    user_id = request.form["user_id"]
    
    data = pd.DataFrame(sample_debts)
    data.set_index("date", inplace=True)
    
    model = ARIMA(data["debt_amount"], order=(5, 1, 0))
    model_fit = model.fit()
    
    forecast = model_fit.forecast(steps=3)[0]
    return render_template("forecast.html", forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)