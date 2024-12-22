# Assisted by watsonx Code Assistant 
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    now = datetime.now()
    return jsonify({'date': now.strftime('%Y-%m-%d %H:%M:%S')})

if __name__ == '__main__':
    app.run()
