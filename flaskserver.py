from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(_name_)
CORS(app)

# Modeli yükle
model = joblib.load('knn_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # İstekten JSON veriyi alma
        data = request.get_json()

        # 'x' ve 'y' anahtarlarını kontrol etme
        if 'x' in data and 'y' in data:
            x = data['x']
            y = data['y']
        else:
            # Varsayılan değerler
            x = 0
            y = 0

        # Diğer değerlerin kontrolü ve depolanması
        other_values = []
        for i in range(1, 29):  # 28 değer varsa
            key = 'value{}'.format(i)
            if key in data:
                other_values.append(data[key])
            else:
                # Varsayılan değerler
                other_values.append(0)

        # Veriyi numpy array formatına dönüştürme
        input_data = np.array([[x, y] + other_values])

        # Modeli kullanarak tahmin yapma
        prediction = int(model.predict(input_data)[0])

        # Yanıtı JSON formatında gönderme
        response = {
            'prediction': prediction
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if _name_ == '_main_':
    app.run(host='127.0.0.1', port=5000, debug=True)
