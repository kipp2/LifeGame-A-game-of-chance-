import random 

def draw_numbers():
    while True:
        num1, num2 = random.randint(1, 5), random.randint(1, 5)
        if num1 != num2:
            return num1, num2
    
def play_game():
    friends = 3
    foes = 3
    
    print("Welcome to life! You start with 3 friends and foes. ")
    
    while 0 < friends < 6:
        life_num1, life_num2 = draw_numbers()
        life_sum = life_num1 + life_num2
        
        player_num1, player_num2 = draw_numbers()
        player_sum = player_num1 + player_num2
        
        print(f"\nLife draws: {life_num1}, {life_num2} (Total: {life_sum})")
        print(f"You draw: {player_num1}, {player_num2} (Total: {player_sum})")
        
        if player_sum > life_sum :
            friends -=1
            foes +=1
            print("You lost this round! You lose friend.")
        elif player_sum < life_sum:
            friends +=1
            foes -= 1
            print("You won this round you lose a foe ")
        else:
            print(f"Friends: {friends}, foes: {foes}")
            print("Its a draw")
            
    if friends == 6:
        print("\nCongrats You won!")
    else:
        print("\n Game Over! You lost all your frieds")
        
if __name__ == "__main__":
    play_game()
        
    
