import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life_Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 205, 50)
RED = (220, 20, 60)

font = pygame.font.Font(None, 36)

def draw_numbers():
    while True:
        num1, num2 = random.randint(1, 5), random.randint(1, 5)
        if num1 != num2:
            return num1, num2

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Welcome to life game!", 280, 200)
        draw_text("Click anywhere to Start", 280, 250)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return #Start Game
def play_game():
    friends = 3
    foes = 3
    running = True
    while running and 0 < friends < 6:
        screen.fill(WHITE)
        
        
        life_num1, life_num2 = draw_numbers()
        life_sum = life_num1 + life_num2
        
        player_num1, player_num2 = draw_numbers()
        player_sum = player_num1 + player_num2
        
        draw_text(f"\nLife draws: {life_num1}, {life_num2} (Total: {life_sum})", 250, 200)
        draw_text(f"You draw: {player_num1}, {player_num2} (Total: {player_sum})", 250, 200)
        
        if player_sum > life_sum :
            friends -=1
            foes +=1
            result_text ="You lost this round! You lose friend."
        elif player_sum < life_sum:
            friends +=1
            foes -= 1
            result_text = "You won this round you lose a foe "
        else:
            result_text = "Its a draw"
            
        draw_text(result_text, 250, 300, GREEN if player_sum > life_sum else RED)
        draw_text(f"friends: {friends}, Foes: {foes}", 250, 350)
        pygame.display.update()
        
        pygame.time.delay(2000)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
    screen.fill(WHITE)
    if friends == 6:
        draw_text("\nCongrats You won!", 250, 250, GREEN)
    else:
        draw_text("\n Game Over! You lost all your friends", 250, 250, RED)
    pygame.display.update()
    pygame.time.delay(3000)
        
if __name__ == "__main__":
    main_menu()
    play_game()
    pygame.quit()
    
