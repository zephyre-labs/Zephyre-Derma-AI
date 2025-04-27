from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 💥 Add this magic line

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    print("Data received:", data)
    return jsonify({'message': 'Received your data!', 'data': data})

if __name__ == "__main__":
    app.run(debug=True)
