# Assisted by Watsonx Code Assistant
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Route 1: Return current date and time
@app.route('/date', methods=['GET'])
def get_date():
    now = datetime.now()
    # Modified date format to include full weekday name and timezone (if needed)
    formatted_date = now.strftime('%A, %d %B %Y, %I:%M:%S %p')
    return jsonify({'date': formatted_date})

# Route 2: Server status
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({
        'status': 'Running',
        'uptime': 'Server uptime is not tracked in this demo app.',
        'message': 'Welcome to the enhanced Flask server!'
    })

# Route 3: Perform a simple computation (e.g., sum of two numbers)
@app.route('/sum/<int:num1>/<int:num2>', methods=['GET'])
def compute_sum(num1, num2):
    result = num1 + num2
    return jsonify({
        'num1': num1,
        'num2': num2,
        'sum': result,
        'message': 'Sum calculated successfully!'
    })
# Route 4: Perform a simple computation (e.g., sub of two numbers)
@app.route('/sub/<int:num1>/<int:num2>', methods=['GET'])
def compute_sub(num1, num2):
    result = num1 - num2
    return jsonify({
        'num1': num1,
        'num2': num2,
        'sum': result,
        'message': 'Sub calculated successfully!'
    })

# Route 5: Return server's current year
@app.route('/year', methods=['GET'])
def current_year():
    current_year = datetime.now().year
    return jsonify({
        'year': current_year,
        'message': 'Current year retrieved successfully!'
    })

if __name__ == '__main__':
    app.run()
