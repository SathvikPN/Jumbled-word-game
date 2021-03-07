'''
Jumble Word Game
Author: Sathvik PN
---------------------------------------
'''
import random

print("Jumbled Words Game (2-Player)")

#Reading each line(contains a word) from words.txt
f = open('words.txt', 'r')
lines = f.read().splitlines()
words = lines

def agreedRounds(rounds):
    while(rounds<1):
        rounds = int(input("No. Rounds: "))
    print("Both Agree for Rounds?\n[1]Yes [2]No")
    ans = input("Make choice: ")
    if(ans!='1'):
        rounds=agreedRounds(0)
    return rounds

def choose(words):
    return random.choice(words)

def jumble(word):
    word = random.sample(word,len(word))
    return ''.join(word)

def shuffle_letters(word):
    word = list(word) #Splitting string into list of characters
    random.shuffle(word) #Jumble list characters
    jumbledWord=''.join(word) #converting list back to string
    return jumbledWord
    
def displayResult(s1,s2):
    if(s1>s2):
        print("[{}] Wins the game.Congratulations...".format(Player1))
    elif(s1<s2):
        print("[{}] Wins the game.Congratulations...".format(Player2))
    else:
        print("[ It was a tie! ]")

def check_answer(word,ans,Player_score):
    if(ans==word):
        print("Perfect!\n")
        Player_score = Player_score + 1
    else:
        print("Oops! expected <{}>\n".format(word))
    return Player_score

def displayBoard(Round,s1,s2,Player1,Player2):
    print('*'*60)
    print('''{} Rounds completed.
Scoreboard:
[{}] {} points
[{}] {} points'''.format(Round,Player1,s1,Player2,s2))
    print('*'*60)

#Main Function starts here...
Player1 = input("Player1 Name: ")
Player2 = input("Player2 Name: ")
rounds = agreedRounds(0)
print("-"*60)
print("The Game Begins...[Total Rounds = {}]".format(rounds))
print("-"*60)

#Initialisation
Player1_score,Player2_score,turn = 0,0,0

while (turn<(2*rounds)):
    word = choose(words)
    jumbledWord = jumble(word) #shuffle_letters(word) works with lists
    print("Jumbled Word: {}".format(jumble(word)))
    
    if turn%2==0:
        ans = input("[{}] ".format(Player1))
        Player1_score = check_answer(word,ans,Player1_score)
        
    elif turn%2==1:
        ans = input("[{}] ".format(Player2))
        Player2_score = check_answer(word,ans,Player2_score)
  
    turn = turn + 1

displayBoard(rounds,Player1_score,Player2_score,Player1,Player2)
displayResult(Player1_score,Player2_score)
