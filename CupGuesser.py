import os
import time
import random


ball_index = 0
num_cups = 3
guess = 0
select = 1
score = 0
best_score = 0
index1 = 0
index2 = 0
guess = 0

with open("best_score.txt","r") as file:
	content = file.read()
	if content:
		best_score = int(content)


os.system('cls')
print("******************************")
print("*                            *")
print("*                            *")
print("* Welcome to CupGuesser!     *")
print("*                            *")
print("******************************")
time.sleep(1)
os.system('cls')
print("******************************")
print("*         CupGuesser         *")
print("*                            *")
print("*          [1] play          *")
print("*          [0] exit          *")
print("******************************")

while(select == 1):
	select = int(input())
	if(select == 1):
		ball_index = random.randint(1,num_cups)
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("* At start ball is on cup #{} ".format(ball_index))
		print("*                            *")
		print("******************************")
		time.sleep(3)
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("*           READY!           *")
		print("*                            *")
		print("******************************")
		time.sleep(3)
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("*            GO!             *")
		print("*                            *")
		print("******************************")
		time.sleep(1)
		for i in range(5):
			index1 = random.randint(1,num_cups)
			index2 = random.randint(1,num_cups)
			while(index2 == index1):
				index2 = random.randint(1,num_cups)
			if(ball_index == index1  or ball_index == index2 ):
				if (ball_index == index1):
					ball_index = index2
				else:
					ball_index = index1
			os.system('cls')
			print("******************************")
			print("*                            *")
			print("*          Swap {}            ".format(i))
			print("          {} <=> {}           ".format(index1, index2))
			print("*                            *")
			print("******************************")
			time.sleep(1)
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("*        Shuffle completed   *")
		print("*                            *")
		print("******************************")
		time.sleep(2)
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("* Guess the cup number:      *")
		print("*                            *")
		print("******************************")
		guess = int(input())
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("* Guess the cup number: {}    *".format(guess))
		print("*                            *")
		print("******************************")
		time.sleep(1)
		correct = (guess == ball_index)
		if correct:
			score += 1
		if score > best_score:
			best_score = score
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		if correct:
			print("*Correct! Ball was on cup #{}".format(ball_index))
		else:
			print("*Incorrect! Ball was on cup #{}".format(ball_index))
		print("*                            *")
		print("******************************")
		time.sleep(1)
		if not correct :
			os.system('cls')
			print("******************************")
			print("*                            *")
			print("*                            *")
			print("*          Game Over!        *")
			print("*                            *")
			print("******************************")
			time.sleep(1)
			os.system('cls')
			print("******************************")
			print("*                            *")
			print("*          Game Over!        *")
			print("*        best score: {}       ".format(best_score))
			print("*                            *")
			print("******************************")
			time.sleep(3)
			with open("best_score.txt","w") as file:
				file.write(str(best_score))
			exit()
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("* Your score: {}              ".format(score))
		print("* Best score: {}              ".format(best_score))
		print("*                            *")
		print("******************************")
		time.sleep(1)
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("*          Round Ended       *")
		print("*                            *")
		print("******************************")
		time.sleep(1)
	else:
		os.system('cls')
		print("******************************")
		print("*                            *")
		print("*                            *")
		print("*          Goodbye!          *")
		print("*                            *")
		print("******************************")
		time.sleep(1)
		with open("best_score.txt","w") as file:
			file.write(str(best_score))
		exit()
	os.system('cls')
	print("******************************")
	print("*                            *")
	print("*         [1] continue       *")
	print("*         [0] exit           *")
	print("*                            *")
	print("******************************")