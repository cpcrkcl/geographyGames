import os
import sys
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("Which game would you like to play?")
        print("1. Statle")
        print("2. Worldle")
        print("3. Quit")
        
        choice = input("Enter 1, 2, or 3: ").strip()
        
        if choice == '1':
            subprocess.run([sys.executable, 'statle.py'])
        elif choice == '2':
            subprocess.run([sys.executable, 'worldle.py'])
        elif choice == '3':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
