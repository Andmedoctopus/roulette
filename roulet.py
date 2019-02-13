import random

'''def win():
    bank = bank + bet * 2
    bet = default_bet
    bet_color *= -1
'''
from tabulate import tabulate

default_bank = 100   #initial bank that we have
bank = default_bank
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27 ,30 ,32 ,34 ,36]
black = [elem for elem in range (1,36) if elem not in red ] #chose the numbers that not in red
trylist = [['Red','Black','Zero','Bank', 'Max bet','Default_bank']]

while (bank < 1000000):
    for coun_try in range(0,9):
        t_red = 0 #total count of red
        t_black = 0 #total count of black
        t_zero = 0 #total count of zero
        bank = default_bank 
        bet = 1 
        default_bet = 1 #initial bet (not changeble)
        bet_color = 1 #-1 - red, 1 - black
        maxbet = 1
    
        for total in range(0, 1000):
            curr_cell = random.randint(0,36)
            if bank <= 0:
                break    
            bank -= bet #bet acceptance 
        
            if curr_cell in red:
                t_red += 1
                if bet_color == -1:
                    bank = bank + bet * 2
                    bet = default_bet
                    bet_color *= -1
                else:
                    bet *= 2
            elif curr_cell in black:
                t_black += 1
                if bet_color == 1:
                    bank = bank + bet * 2
                    bet = default_bet
                    bet_color *= -1
                else:
                    bet *= 2
            else:
                t_zero += 1
                bet *= 2
            if maxbet < bet:
                maxbet = bet
        trylist.append([t_red,t_black, t_zero, bank, maxbet,default_bank])
    default_bank = default_bank * 1.5
    default_bank = int(default_bank)

for x in range(0,9):
    print(trylist[x])

print(tabulate(trylist)) #print more readable table 
