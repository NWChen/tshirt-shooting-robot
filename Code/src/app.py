from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<cmd>')
def command(cmd=None):
	if cmd=='spinup':
		return str(int(round(time.time() * 1000))), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')