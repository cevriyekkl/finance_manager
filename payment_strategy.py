from flask import Flask, render_template, request, jsonify
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

app = Flask(__name__)

# Örnek bir veritabanı
database = {
    'user1': {
        'features': [[5000, 2000, 10000], [6000, 2500, 12000], [5500, 3000, 11000]],
        'strategies': [0.8, 0.7, 0.85]  # Örnek strateji puanları
    },
    'user2': {
        'features': [[4000, 1500, 8000], [4500, 1800, 9000], [4200, 2000, 8500]],
        'strategies': [0.75, 0.65, 0.8]  # Örnek strateji puanları
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/determine_payment_strategy', methods=['POST'])
def determine_payment_strategy():
    # Kullanıcı kimliğini al
    user_id = request.form['user_id']
    
    # Kullanıcının finansal verilerini al
    user_data = database.get(user_id)
    
    if user_data:
        # Yapay sinir ağı modelini oluştur
        model = Sequential()
        model.add(Dense(12, input_dim=3, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mean_squared_error', optimizer='adam')
        
        # Veriyi numpy dizisine dönüştür
        X = np.array(user_data['features'])
        y = np.array(user_data['strategies'])
        
        # Modeli eğit
        model.fit(X, y, epochs=150, batch_size=2, verbose=0)
        
        # Yeni veri için strateji puanını belirle
        new_data = np.array([request.form['income'], request.form['expenses'], request.form['debt']])
        strategy_score = model.predict(new_data.reshape(1, -1))
        
        return render_template('result.html', strategy_score=strategy_score[0])
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)