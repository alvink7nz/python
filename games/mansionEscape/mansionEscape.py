import time

def print_slow(text):
    """Print text with a slight delay to mimic storytelling."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def starting_room():
    print_slow("You wake up in a dimly lit room. A lantern sits on a table nearby.")
    while True:
        choice = input("What do you do? (1: Pick up the lantern, 2: Open the door): ").strip()
        if choice == "1":
            print_slow("You pick up the lantern. Its faint glow reassures you.")
            return "lantern"
        elif choice == "2":
            print_slow("You stumble in the dark and fall! You lose some health.")
            return "injured"
        else:
            print("Invalid choice. Please choose 1 or 2.")

def hallway(has_lantern):
    print_slow("You enter a dark hallway. Strange noises echo around you.")
    while True:
        choice = input("What do you do? (1: Move forward cautiously, 2: Investigate the noise, 3: Run blindly): ").strip()
        if choice == "1":
            print_slow("You move cautiously and avoid any traps.")
            return True
        elif choice == "2":
            print_slow("You find a rusty key hidden in the shadows.")
            return "key"
        elif choice == "3":
            print_slow("You run blindly and trigger a trap! You lose health.")
            return "injured"
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def library():
    print_slow("You enter a dusty library. A faint glow catches your eye.")
    while True:
        choice = input("What do you do? (1: Search the bookshelves, 2: Investigate the glowing object, 3: Ignore everything): ").strip()
        if choice == "1":
            print_slow("You find a hidden compartment with a map inside.")
            return "map"
        elif choice == "2":
            print_slow("The glowing object is cursed! You feel weaker.")
            return "cursed"
        elif choice == "3":
            print_slow("You decide not to waste time and move on.")
            return None
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def final_room(items):
    print_slow("You reach a locked door with a riddle engraved on it:")
    print_slow("\"I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?\"")
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer == "echo":
            print_slow("The door unlocks! You step outside into freedom.")
            return True
        else:
            print_slow("That is incorrect. The door remains locked.")
            retry = input("Try again? (yes/no): ").strip().lower()
            if retry != "yes":
                return False

def main():
    print_slow("Welcome to 'Escape the Haunted Mansion'!")
    health = 3
    items = []

    # Starting Room
    result = starting_room()
    if result == "lantern":
        items.append("lantern")
    else:
        health -= 1

    # Hallway
    result = hallway("lantern" in items)
    if result == "key":
        items.append("key")
    elif result == "injured":
        health -= 1

    # Library
    result = library()
    if result:
        items.append(result)
    if result == "cursed":
        health -= 1

    # Check health
    if health <= 0:
        print_slow("You have succumbed to the dangers of the mansion. Game Over.")
        return

    # Final Room
    print_slow("You use the items you've collected to find the final door.")
    escaped = final_room(items)

    if escaped:
        print_slow("Congratulations! You have escaped the haunted mansion.")
    else:
        print_slow("The mansion claims you as its prisoner forever. Game Over.")

if __name__ == "__main__":
    main()
