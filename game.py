import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import api

maxRound = 5
currentRound = 1

def setUpGame():
	allPhotos = getAllPaths()
	randomIndices = []
	randomPhotos = []

	while(len(randomIndices) < maxRound):
		index = random.randrange(len(allPhotos))
		randomPhotos.append(allPhotos[index])

	nextRound(allPhotos)

def nextRound(allPhotos):
	#send time request to flask server
	allTags = getAllTags(allPhotos[currentRound])
	currentRound +=1
