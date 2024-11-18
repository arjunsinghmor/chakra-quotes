from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

with open('quotes.json', 'r') as f:
    quotes = json.load(f)

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/quote')
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
