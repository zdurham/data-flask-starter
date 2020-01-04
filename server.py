from flask import Flask, render_template, jsonify;
import os
port = os.environ.get('PORT')

app =  Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/data')
def getData():
  return jsonify([1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
  if port:
    app.run(port=os.environ.get('PORT'))
  else:
    app.run(port=5000, debug=True)

  
    