from flask import Flask, render_template, jsonify
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def getData():
    return jsonify([1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(port=port, host='0.0.0.0')
