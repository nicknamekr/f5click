from flask import Flask, render_template
from replit import db
app = Flask('app')

@app.route('/')
def main():
  db["x"] = int(db["x"]) + 1
  return render_template('index.html', value = db['x'])

app.run(host='0.0.0.0', port=1588, debug=True)