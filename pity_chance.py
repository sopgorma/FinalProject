from breezypythongui import EasyFrame

#The class Pity will be used to calculate the needed amount of money and wishes needed
#for the next 5-star banner character.

class Pity(EasyFrame):
    def __init__(self, number):
        EasyFrame.__init__(self,title="~Genshin Pity Calculator~",width=500,height=200)
        self.config(bg="darksalmon")
        self.number = number
        self.addLabel(text="Enter the amount of wishes made: ", row=0, column=0)
        self.textInput = self.addIntegerField(value=0, row=0, column=1, width=10)
        self.number = self.textInput.getNumber()
        self.addButton(text="Continue", row=3, column=1, command=self.get_chance)

    def get_chance(self):
        self.addLabel(text="Did you win or lose your last pity?", row=1, column=1)
        self.addButton(text="Won Pity",row=3,column=1,command=self.get_win)
        self.addButton(text="Lost Pity",row=4,column=1,command=self.get_lose)

    def get_lose(self):
        if self.number >= 75:
            self.number = self.textInput.getNumber()
            self.number = (90 - self.number)
            chance_cost = float((self.number/15)*primo_cost)
            print("You will get the banner character within the next ",self.number," wish(es) or $", f'{chance_cost:.2f}',". Congratulations!")
            self.destroy()
        elif self.number < 75:
            self.number = self.textInput.getNumber()
            self.number = (75 - self.number)
            chance_cost = float((self.number/15)*primo_cost)
            total_cost = chance_cost + primo_cost
            print("You still need ",self.number," wishes or roughly $",f'{chance_cost:.2f}'," to get into the pity draw.", '\n', "After that, you will obtain the banner character within 15 wishes. You need to spend a max total of $", f'{total_cost:.2f}', ". You got this!")
            self.destroy()

    def get_win(self):
        if self.number >= 75:
            self.number = self.textInput.getNumber()
            self.number = (90 - self.number)
            chance_cost = chance_cost = float((self.number/15)*primo_cost)
            print("You're still in the pity! You need ",self.number, " wishes or  $",f'{chance_cost:.2f}'," to see if you win.", '\n', "If you lose, it will cost around $", cost, "to be guaranteed the next banner character.")
            self.destroy()
        elif self.number < 75:
            self.number = self.textInput.getNumber()
            self.number = (75 - self.number)
            chance_cost = float((self.number/15)*primo_cost)
            total_cost = chance_cost + primo_cost
            print("You still need ",self.number," wishes or roughly $", f'{chance_cost:.2f}', "to begin the soft pity. You will need a max total of $", f'{total_cost:.2f}', "to obtain a 5-star character.", '\n', "You are still in the pity so you have a 50/50 chance to obtain the banner character.", '\n', "If you lose, it will cost around $", cost, "to be guaranteed the next banner character. Good luck!")
            self.destroy()

primogems = 160  #The amount of primogems needed for one wish.
primo_cost = 35.00  #For 15 pulls, it is $35.00.
cost = 200.00 #It costs roughlt $200 to pull 90 wishes.
