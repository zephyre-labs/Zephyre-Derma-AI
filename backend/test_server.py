from flask import Flask

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    return {"status": "success", "message": "Server is working"}

if __name__ == "__main__":
    app.run(port=5000)
