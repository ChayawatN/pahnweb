from flask import Flask, jsonify


app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def home():
    return "Hello World"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)  # Return web frameworks information


if __name__ == "__main__":
    app.run(debug=False)