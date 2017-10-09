# ThinkingGame

Thinking game is an SMS-based image classification guessing game where players try to guess the top tags given to an image by the Clarifai Image Classification API. The game shows a random image each round and waits for user input through the Twilio SMS API. User scores are tallied and top users are shown on the displayed leaderboard. Thats about it, all thats left is to have some fun!

## Technologies used:
* Clarifai Image Classification API: Getting classification tags for each image
* MongoDB: Storing and accessing image paths and tags 
* Twilio: SMS interactions between the players and the game
* Flask: Interaction between the Twilio API and the game
* OpenCV: Image processing to make images consistent and easier to display
