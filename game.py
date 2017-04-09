import random
import api
import math
import changetext
import operator

maxRound = 5
currentRound = -1
record = {}
randomPhotos = []
currentTags = []

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



# setUpGame()
# for i in range(5):
# 	addUser(i,"Urmom{}".format(i))
# while(currentRound < maxRound-1):
# 	nextRound()
# 	makeGuess(0,"sea")

# for user in record.keys():
# 	print(user, record[user]["score"])
