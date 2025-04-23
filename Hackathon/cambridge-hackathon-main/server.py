### Flask Backend (server.py)

# python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.json
    user_name = data.get('name', '').strip()
    if user_name:
        return jsonify({"message": f"Hello, {user_name}! Welcome to the app."})
    else:
        return jsonify({"error": "Name is required."}), 400

if __name__ == '__main__':
    app.run(debug=True)
