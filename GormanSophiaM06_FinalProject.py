"""
Sophia Gorman
Final Project - M06
11/29/23

"""
#This program will determine how many pulls you need to get the wanted "banner" character
#Based on the popular game "Genshin Impact"

pity = str(input("Did you previously 'win' or 'lose' your pity? (If you are unsure, put 'win'.) "))
chance = int(input("Enter the amount of wishes made after obtaining last 6-star character: "))
#Every 75-90 wishes, the user will be put into a "pity system"
#This pity system will give the user a 50/50 chance of either "winning" a 5-star banner character, 
#or losing, and obtaining a regular 5-star character.

if pity == "lose":
    if chance >= 75:
        print("You will get the banner character within the next 15 wishes. Congratulations!")
    elif chance < 75:
        chance = 75 - chance
    print("You still need ", chance, " wishes to get into the pity draw. After that, you will obtain the banner character within 15 wishes. You got this!")
    
if pity == "win":
    if chance >= 75:
        print("You will get a regular 5-star character within the next 15 wishes. You still need another 75-90 wishes to obtain the banner character.")
    elif chance < 75:
        chance = 75 - chance
        print("You still need ", chance, " wishes to get into the pity draw to obtain a 5-star character. Afterwards, it will take you another 75-90 wishes to obtain the banner character. Good luck!")
    else:
        print("Invalid. Please try again")

#These functions tell the user how many more wishes they need to obtain a 5-star character, whether banner or regular
