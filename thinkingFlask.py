from flask import Flask, request
from twilio.rest import Client
import requests
import game
import time

app = Flask(__name__)

f = open('twilioapi', 'r')
acc = f.read().split()
ACCOUNT_SID = acc[0]
AUTH_TOKEN = acc[1]
f.close()
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# client.messages.create(
#         to = '9178681272',
#         from_ = '3476581337',
#         body = 'yay?',
#		  media_url = 'https://raw.githubusercontent.com/pooneetthaper/ThinkingGame/master/images/0.jpg?token=AHlePwtuOuIbczP3cS06i2m1i6J55ijhks5Y80yBwA%3D%3D'
#    )

currentWaits = -1
began = False

@app.route('/')
def index():
	# client.messages.create(
 #        to = '9178681272',
 #        from_ = '3476581337',
 #        body = 'yay?',
 #        
	game.setUpGame()
	return render_template("index.html")

@app.route('/sms', methods=['POST']) # UPDATE FUNCTION
def sms():
	global game.currentRound
	global game.maxRound
	global game.record
	global currentWaits
	global began

	if(game.currentRound < game.maxRound-1):
		
		game.endRound()
		if(game.currentRound == -1): # Before game
			num = request.form['From']
			user = request.form['Body']
			game.addUser(num, user)
			if(not began):
				began = True
				startTime = time.time()
				while(time.time() <= startTime + 10):
				 	continue
		else:
			if(currentWaits<game.currentRound):
				currentWaits+=1
				while(time.time() <= startTime + 10):
					continue
				game.nextRound()
				game.endRound()

def preGame():


	app.logger.info("Added User: {0}".format(user))
	return user


if __name__ == "__main__":
	app.run(debug = True)