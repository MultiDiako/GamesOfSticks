import random

num_sticks = random.randint(10, 60)
max_pick = random.randint(1, 20)
current_player = random.randint(0, 1)

def display_sticks(n):
        print("o  "*n)
        print("|  "*n)

def player_input(max_pick):
    while True:
        try:
            player_pick = int(input(f"\nYour turn. Enter the number of sticks to pick (1-{max_pick}): "))
            if 1 <= player_pick <= max_pick:
                return player_pick
            else:
                print(f"Invalid input. Please enter a number between 1 and {max_pick}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
while num_sticks > 0:
    print(f"\nRemaining sticks: {num_sticks}")
    display_sticks(num_sticks)
        
    if current_player == 0:
        player_pick = player_input(max_pick)
    else:
        computer_pick = random.randint(1, min(max_pick, num_sticks))
        print(f"Computer picks {computer_pick} sticks.")
        player_pick = computer_pick

    num_sticks -= player_pick
    current_player = 1 - current_player

print("\nGame over!")
if current_player == 0:
    print("You win!")
else:
    print("Computer wins!")