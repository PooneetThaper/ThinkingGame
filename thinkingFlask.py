from flask import Flask, request
from twilio.rest import Client
import requests
import time
import random
import api
import math
import changetext
import operator

app = Flask(__name__)

f = open('twilioapi', 'r')
acc = f.read().split()
ACCOUNT_SID = acc[0]
AUTH_TOKEN = acc[1]
f.close()
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# client.messages.create(
#         to = '',
#         from_ = '',
#         body = 'yay?',
#		  media_url = 'https://raw.githubusercontent.com/pooneetthaper/ThinkingGame/master/images/0.jpg?token=AHlePwtuOuIbczP3cS06i2m1i6J55ijhks5Y80yBwA%3D%3D'
#    )

maxRound = 5
currentRound = -1
record = {}
randomPhotos = []
currentTags = []

@app.route('/')
def index():
	setUpGame()
	app.logger.info("HI")
	return render_template("index.html")

@app.route('/increment')
def increment():
	endRound()
	nextRound()

@app.route('/sms', methods=['POST']) # UPDATE FUNCTION
def sms():
	global currentRound
	global maxRound
	global record
	global currentWaits
	global began
	num = request.form['From']
	inp = request.form['Body']

	if(currentRound < 0):
		addUser(num, inp)
	else:
		makeGuess(num,inp)

def setUpGame():
	global randomPhotos
	allPhotos = api.getAllPaths()
	randomIndices = []

	while(len(randomIndices) < maxRound):
		index = random.randrange(len(allPhotos))
		if index not in randomIndices:
			randomIndices.append(index)
			randomPhotos.append(allPhotos[index])

def addUser(number,username):
	global record
	record[number] = {}
	record[number]["lastSuccessfulRound"] = 0
	record[number]["score"] = 0
	record[number]["username"] = username

def nextRound():
	#send time request to flask server
	global randomPhotos
	global currentRound
	global currentTags

	currentRound +=1
	currentTags = api.getAllTags(randomPhotos[currentRound])
	# print(randomPhotos[currentRound],currentTags)

def endRound():
	changetext.changeText(getTops())

def makeGuess(number,guess):
	global currentRound
	global record

	if currentRound > record.get(number).get("lastSuccessfulRound"):
		index = isGood(guess)
		if (index >= 0):
			record[number]["score"] += getScore(index)
			record[number]["lastSuccessfulRound"] = currentRound

def getTops():
	global record
	newDict = {}
	for user in record:
		newDict[record[user]["username"]] = record[user]["score"]
	sortedRanking = sorted(newDict.items(), key=operator.itemgetter(1))
	return sortedRanking[:10]

def isGood(guess):
	global currentTags
	for i in range(5):
		if guess.lower() == currentTags[i].lower(): return i
	return -1

def getScore(index):
	return math.floor(3-(index/2.0))


if __name__ == "__main__":
	app.run(debug = True)
