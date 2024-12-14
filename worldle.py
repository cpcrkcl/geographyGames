import pandas as pd 
import random
from Haversine import calculate_distance_and_bearing
import os 
import time

clear = lambda: os.system('cls')

df = pd.read_csv('LatAndLong.csv')

# Drop rows with NaN values in country, latitude, or longitude
df = df.dropna(subset=['country', 'latitude', 'longitude'])

country = df['country']
latitude = df['latitude']
longitude = df['longitude']

countryFound = False
isPlaying = True
while(isPlaying):
    clear()
    countryID = random.randint(0, len(country) - 1)  
    guesses = 0
    while(not countryFound and guesses < 6):
        userCountryID = -1
        while userCountryID == -1:
            userCountry = input('Please input a country:')
            for i in range(len(country)):
                if userCountry.lower() == country[i].lower():
                    userCountryID = i
                    break
            if userCountryID == -1:
                print("Country not found. Please try again.\n")
        
        guesses += 1
        
        if userCountryID == countryID:
            print("You found the country!")
            countryFound = True
        else:
            distance, bearing = calculate_distance_and_bearing(latitude[userCountryID], longitude[userCountryID], latitude[countryID], longitude[countryID])
            print('You are ' + str(round(distance)) + ' km away from the country. The correct direction is ' + bearing)
            if guesses < 6:
                print(f'Please try again. You have {6-guesses} guesses left.\n')
            
    if not countryFound:
        print(f"Game Over! The country was {country[countryID]}")
    
    playAgain = input("Do you want to play again? (y/n): ")
    if playAgain.lower() == 'y':
        countryFound = False
    else:
        isPlaying = False
        print("Thanks for playing!")
        time.sleep(3)
        os.system('python game.py') 
        clear()


