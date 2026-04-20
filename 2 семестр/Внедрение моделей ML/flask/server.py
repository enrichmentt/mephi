from flask import Flask, request, jsonify
import pickle
import numpy as np

# Создаём приложение Flask
app = Flask(__name__)

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Эндпоинт для предсказания по 4 признакам
    Ожидает POST-запрос с JSON-списком из 4 чисел
    """
    try:
        features = request.json

        if features is None:
            return jsonify({'error': 'No JSON data provided'}), 400

        if len(features) != 4:
            return jsonify({'error': f'Expected 4 features, got {len(features)}'}), 400

        features_array = np.array(features).reshape(1, 4)

        prediction_array = model.predict(features_array)

        prediction_value = prediction_array[0]

        return jsonify({
            'prediction': float(prediction_value),  # np.float64 -> float для JSON
            'status': 'success'
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'failed'
        }), 500

@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
