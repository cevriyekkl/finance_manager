from flask import Flask, render_template, request, jsonify
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Örnek veritabanı
# Kullanıcı finansal verileri
user_financial_data = {
    'user1': {
        'features': [[5000, 2000, 10000], [4000, 1500, 8000], [3000, 1000, 5000]],
        'plans': ['Plan1', 'Plan2', 'Plan3']
    },
    'user2': {
        'features': [[6000, 2500, 12000], [4500, 2000, 7000], [3500, 1500, 6000]],
        'plans': ['Plan2', 'Plan3', 'Plan1']
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_repayment_plan', methods=['POST'])
def create_repayment_plan():
    user_id = request.form['user_id']
    user_data = user_financial_data.get(user_id)
    if user_data:
        clf = DecisionTreeClassifier()
        clf = clf.fit(user_data['features'], user_data['plans'])
        
        new_data = [int(request.form['income']), int(request.form['expenses']), int(request.form['debt'])]
        plan = clf.predict([new_data])
        return render_template('result.html', plan=plan[0])
    else:
        return render_template('error.html', message="Kullanıcı bulunamadı.")
@app.route('/track_debt', methods=['POST'])
def track_debt():
    # Borç takibi işlemleri burada gerçekleştirilecek
    # Örneğin, bir hesaplama sonucu elde edilen veri
    debt_status = calculate_debt_status()  # Hesaplama fonksiyonunu çağırın
    return jsonify(debt_status)  # Hesaplama sonucunu JSON formatında döndürün

def calculate_debt_status():
    # Burada borç takibi işlemleri gerçekleştirilir ve sonuç hesaplanır
    # Örnek olarak, basit bir sözlük yapısı kullanalım:
    debt_status = {
        "total_debt": 5000,
        "remaining_debt": 3000,
        "paid_debt": 2000
    }
    return debt_status
if __name__ == '__main__':
    app.run(debug=True)