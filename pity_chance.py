from breezypythongui import EasyFrame

class MainFrame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="~Genshin Pity~")
        self.config(bg="darksalmon")

class Pity():
    def __init__(self, pity, chance):
        self.pity = input("Did you previously 'win' or 'lose' your pity? (If you are unsure, put 'win'.) ")
        self.chance = int(input("Enter the amount of wishes made after obtaining last 5-star character: "))

    def get_pity(self):
        return self.pity
    
    def get_chance(self):
        return self.chance

    def lose(self):
        if self.pity == "lose":
            if self.chance >= 75:
                self.chance = 90 - self.chance
                chanceCost = float((self.chance/15)*primoCost)
                print("You will get the banner character within the next ",self.chance," wish(es)  or $", f'{chanceCost:.2f}',". Congratulations!")
            elif self.chance < 75:
                self.chance = 75 - self.chance
                chanceCost = float((self.chance/15)*primoCost)
                totalCost = chanceCost + primoCost
                print("You still need ",self.chance," wishes or roughly $",f'{chanceCost:.2f}'," to get into the pity draw.," '\n', "After that, you will obtain the banner character within 15 wishes. You need to spend a max total of $", f'{totalCost:.2f}', ". You got this!")
    
    def win(self):
        if self.pity == "win":
            if self.chance >= 75:
                self.chance = 90 - self.chance
                chanceCost = chanceCost = float((self.chance/15)*primoCost)
                print ("You're still in the pity! You need ", self.chance, " wishes or  $",f'{chanceCost:.2f}'," to see if you win.", '\n', "If you lose, it will cost around $", cost, "to be guaranteed the next banner character.")
            elif self.chance < 75:
                self.chance = 75 - self.chance
                chanceCost = float((self.chance/15)*primoCost)
                totalCost = chanceCost + primoCost
                print ("You still need ",self.chance," wishes or roughly $", f'{chanceCost:.2f}', "to begin the soft pity. You will need a max total of $", f'{totalCost:.2f}', "to obtain a 5-star character.", '\n', "You are still in the pity so you have a 50/50 chance to obtain the banner character.", '\n', "If you lose, it will cost around $", cost, "to be guaranteed the next banner character. Good luck!")

primogems = 160 
primoCost = 35.00 
cost = 200.00 

totalPity = Pity(any,any)
print(totalPity)
totalPity.lose()
totalPity.win()
