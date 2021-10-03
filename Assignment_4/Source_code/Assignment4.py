import random

def play_again() -> bool:
    #in a while loop with condition True, input string return True or False
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    #play = input('Play again?\n')
    while True:
        play = input('Play again?\n')
        if play.lower() in {'y', 'yes'}:
            return True
        elif play.lower() in {'n', 'no'}:
            return False
        else:
            print('Please enter another value')
    return play

def get_wager(bank : int) -> int:
    #in a while loop input integer
    #return wager if it is valid
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How many chips do you want to wager?\n'))
    if wager < 0:
      print('Value too low')
    return wager

def get_slot_results() -> tuple:
    #reela, reelb, reelc = random.randint(1,10), random.randint(1,10)
    ''' Returns the result of the slot pull '''
    reela = random.randint(1,10)
    reelb = random.randint(1,10)
    reelc = random.randint(1,10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    matches = 0
    if reela == reelb:
        matches += 2
        if reela == reelc:
            matches += 1
    elif reela == reelc:
        matches =+ 2
        if reela == reelb:
            matches += 1
    elif reelb == reelc:
        matches += 2
        if reelb == reela:
            matches += 1
    return matches

def get_bank() -> int:
    #in a while loop, input integer
    ''' Returns how many chips the user wants to play with. Loops until a value greater than 0 and less than 101 '''
    num = 0
    while num == 0:
        bankStart = int(input('How many chips do you want to start with?\n'))
        if bankStart <= 0:
            print('Too low a value, you can only choose between 1 - 100 chips')
        elif bankStart > 100:
            print('Too high a value, you can only choose between 1 - 100 chips')
        else:
            num = 1
    return bankStart

def get_payout(wager, matches):
    #wager * 10  - wager
    #wager * 3 - wager
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 5 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        x = (wager * 10) - wager
    elif matches == 2:
        x = (wager * 3) - wager
    elif matches == 0:
        x = wager - wager - wager
    return x

if __name__ == "__main__":
    playing = True
    bank_roll = []
    while playing:

        bank = get_bank()
        bank_roll.append(bank)
        counter = 0

        while bank > 0:  # Replace with condition for if they still have money.
            
            counter += 1
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            bank_roll.append(bank)

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            
            if bank == 0:
              print("You lost all", bank_roll[0], "in", counter, "spins")
              print("The most chips you had was", max(bank_roll))
              playing = play_again()