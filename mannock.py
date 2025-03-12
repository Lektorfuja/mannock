import random

def battle():
    mannock_hp = 5  # Mannock's health points
    score = 0        # Number of German planes shot down
    target_kills = 3 # Number of enemy planes to defeat to win
    
    print("Welcome to the Air Combat Simulator!")
    print("You are Edward Mannock, an ace WW1 fighter pilot.")
    print("Your mission: Shoot down 3 German planes to win!")
    
    while mannock_hp > 0 and score < target_kills:
        print("\nA German fighter appears!")
        enemy_hp = 2  # Each enemy has 2 HP
        
        while enemy_hp > 0:
            action = input("Do you want to (A)ttack or (E)vade? ").strip().lower()
            
            if action == 'a':
                if random.randint(1, 10) > 3:  # 70% chance to hit
                    print("You hit the enemy!")
                    enemy_hp -= 1
                else:
                    print("You missed!")
            elif action == 'e':
                if random.randint(1, 10) > 5:  # 50% chance to evade
                    print("You successfully evaded the attack!")
                    continue
                else:
                    print("Evade failed!")
            else:
                print("Invalid input. Choose (A)ttack or (E)vade.")
                continue
            
            # Enemy attacks if it's still alive
            if enemy_hp > 0:
                if random.randint(1, 10) > 6:  # 40% chance to hit Mannock
                    print("The enemy hits you!")
                    mannock_hp -= 1
                else:
                    print("The enemy missed!")
                    
        print("You shot down the German fighter!")
        score += 1
    
    if score >= target_kills:
        print(f"\nMission accomplished! You shot down {score} German fighters and survived!")
    else:
        print(f"\nYou were shot down after scoring {score} kills. Better luck next time, Ace!")

if __name__ == "__main__":
    battle()
