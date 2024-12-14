import pandas as pd 
import random
from Haversine import calculate_distance_and_bearing
import os 
import time

clear = lambda: os.system('cls')

df = pd.read_csv('LatAndLong.csv')

# Drop rows with NaN values in usa_state, usa_state_latitude, or usa_state_longitude
df = df.dropna(subset=['usa_state', 'usa_state_latitude', 'usa_state_longitude'])

# Convert state column to string, replacing any NaN with an empty string
df['usa_state'] = df['usa_state'].fillna('').astype(str)

state = df['usa_state'].astype(str)
latitude = df['usa_state_latitude'].astype(float)
longitude = df['usa_state_longitude'].astype(float)

stateFound = False
isPlaying = True
while(isPlaying):
    clear()
    stateID = random.randint(0, len(state) - 1)  
    guesses = 0
    while(not stateFound and guesses < 6):
        userStateID = -1
        while userStateID == -1:
            userstate = input('Please input a state:')
            for i in range(len(state)):
                if userstate.lower() == str(state[i]).lower():
                    userStateID = i
                    break
            if userStateID == -1:
                print("state not found. Please try again.\n")
        
        guesses += 1
        
        if userStateID == stateID:
            print("You found the state!")
            stateFound = True
        else:
            distance, bearing = calculate_distance_and_bearing(latitude[userStateID], longitude[userStateID], latitude[stateID], longitude[stateID])
            print('You are ' + str(round(distance)) + ' km away from the state. The correct direction is ' + bearing)
            if guesses < 6:
                print(f'Please try again. You have {6-guesses} guesses left.\n')
            
    if not stateFound:
        print(f"Game Over! The state was {state[stateID]}")
    
    playAgain = input("Do you want to play again? (y/n): ")
    if playAgain.lower() == 'y':
        stateFound = False
    else:
        isPlaying = False
        print("Thanks for playing!")
        time.sleep(3)
        os.system('python game.py') 
        clear()
