#dice game with two players, and determines winners at the end, also displays scores.
#Certain name effects score (Person with the most vowels in the game will be the number of rounds they play).
#Rolling an Odd adds + 2 pts.
#Rolling same # as opponent + 1pts. per player.
#Range is decided by players picking the numbers before the game.
import random

name = raw_input("what is your name?")

def roll(beginning,end):
		return random.randint(beginning,end)

def round_winner(rollresult1,rollresult2):
	if(rollresult1 > rollresult2):
		return "player1"
	elif(rollresult2 > rollresult1):
		return "player2"
	else:
		return "tie"

def game_winner(score1,score2):
	if(score1 > score2):
		return "player1 won"
	elif(score2 > score1):
		return "player2 won"
	else:
		return "it was a tie!"

if name = "Omer" -1 score1 and score2:
 
if player1 + player2 roll 1=1:
	print("+2 both")


beginning = 1
end = 6 
rollresult1 = 0
rollresult2 = 0
score1 = 0
score2 = 0
range = [1,6]
ledger = []

gamerunning = 3

while(gamerunning >= 0):
	rollresult1 = roll(beginning,end)
	rollresult2 = roll(beginning,end)
	roll_win = round_winner(rollresult1,rollresult2)
	if(rollresult1 > rollresult2):
		score1 += 1
	elif(rollresult2 > rollresult1):
		score2 += 1
	gamerunning -= 1
	print(rollresult1,rollresult2,roll_win)

gamewin = game_winner(score1,score2)

print(gamewin)
