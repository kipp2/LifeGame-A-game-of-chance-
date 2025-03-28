import random 

def roll():
	while True:
		rolldie = random.randint(1, 9)
		return rolldie
		
def play():
    total = 100
    score = 0 
    running = True 
    step = 0
    while running and score < 100:
        add = roll()
        print("dice=", add)
        score2 = score + add
        step += 1 
        print("step=", step)
        score = score2
        print("score=", score)
        
        if score >= total:
            print("You done did it")
            break
            
if __name__ == "__main__":
    play()

