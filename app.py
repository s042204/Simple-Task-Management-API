from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to test if the API is working
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Simple Task Management API!"})

if __name__ == '__main__':
    app.run(debug=True)
