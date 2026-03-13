from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Feng Shui NLP Chatbot!'

@app.route('/about')
def about():
    return 'This is an NLP chatbot that helps you with feng shui queries.'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    # Add chatbot logic here
    response = {'reply': 'This is a placeholder response.'}  # Placeholder response
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)