import random

def game():
    score =  random.randint(1, 69)
    print(f"score is {score}")
    with open("highscore.txt") as f:
        highscore = f.read()
        if ( highscore !=""):
         highscore = int(highscore)
        else:
           highscore = 0
       
        if( score > highscore):
            with open("highscore.txt", "w") as f:
                f.write(str(score))
                print(f"new high score is {score}")
    return score 

game()