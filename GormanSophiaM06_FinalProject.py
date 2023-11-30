"""
Sophia Gorman
Final Project - M06
11/29/23

"""
#This program will determine how many pulls you need to get the wanted "banner" character.
#Based on the popular game "Genshin Impact". This program is based on purchasing primogems instead of farming them.

primogems = 160 #160 primogems = 1 wish. 1600 primos = 10 wishes. 
primoCost = 35.00 #It costs roughly $35.00 for 15 wishes/pulls. (~$23 for 10 pulls)
costs = 200.00 #It costs at least $200.00 for 90 pulls
#Players have the option to wish one time, or pull 10 wishes at once. 
print("Welcome to the Genshin Pity System program! If you previously won your 50/50 pity, you will still be in the pity on your next 75-90 wishes. ", '\n', "If you lost, you are guaranteed the banner character in the next 90 wishes. Good luck and have fun! :D")

pity = str(input("Did you previously 'win' or 'lose' your pity? (If you are unsure, put 'win'.) "))
chance = int(input("Enter the amount of wishes made after obtaining last 5-star character: "))
#Every 75-90 wishes, the user will be put into a "pity system".
#This pity system will give the user a 50/50 chance of either "winning" a banner character, 
#or losing, and obtaining a regular 5-star character. If a character wins, they stay in the pity for the next 90 wishes.
#If they lose, their next banner character is guaranteed.

if pity == "lose":
    if chance >= 75:
        chance = 90 - chance
        chanceCost = float((chance/15)*primoCost)
        print("You will get the banner character within the next ",chance," wish(es)  or $", chanceCost,". Congratulations!")
    elif chance < 75:
        chance = 75 - chance
        chanceCost = float((chance/15)*primoCost)
        totalCost = chanceCost + primoCost
        print("You still need ",chance," wishes or roughly $",chanceCost," to get into the pity draw.," '\n', "After that, you will obtain the banner character within 15 wishes. You need to spend a max total of $", totalCost, ". You got this!")

if pity == "win":
    if chance >= 75:
        chance = 90 - chance
        chanceCost = chanceCost = float((chance/15)*primoCost)
        print("You're still in the pity! You need ", chance, " wishes or  $",chanceCost," to see if you win.")
        print("If you lose, it will cost around $", costs, "to be guaranteed the next banner character.")
    elif chance < 75:
        chance = 75 - chance
        chanceCost = float((chance/15)*primoCost)
        totalCost = chanceCost + primoCost
        print("You still need ",chance," wishes or roughly $", chanceCost, "to begin the soft pity. You will need a max total of $", totalCost, "to obtain a 5-star character.")
        print("You are still in the pity so you have a 50/50 chance to obtain the banner character.", '\n', "If you lose, it will cost around $", costs, "to be guaranteed the next banner character. Good luck!")
    else:
        print("Invalid. Please try again")

#These functions tell the user how many more wishes they need to obtain a 5-star character, whether banner or regular
