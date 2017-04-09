from flask import Flask, request
import time
import urllib # request
import requests

app = Flask(__name__)

@app.route('/timer', methods=['POST'])
def receive():
	app.logger.info("OH")
	print(type(request.form['startTimer']))
	if(request.form['startTimer'] == "1"):
		print(request.form)
		app.logger.info("HI")
		#time.sleep(3)
		#req = urllib.request.urlopen('http://127.0.0.1:5000/receive')
		#print(request.read())
		requests.post('http://0c9d9014.ngrok.io/receive', data={'timeEnd':1})
	return "ggood"

if __name__ == "__main__":
	app.run(debug=True, port=8080)