from random import randint,choice

def CPUturn(number, slotcheck, rng):
    slot_list = []
    for i in range(0,5):
        if slotcheck[i] == 0:
            slot_list.append(i)
            #print("Adding", i, "to slot list")
    rand_slot = choice(slot_list)
    #print("CPU's available slots: ", slot_list)
    #print("Assigning to slot", rand_slot)
    number[rand_slot] = rng
    slotcheck[rand_slot] = 1
    return number, slotcheck

def CorrectAssignment(number, slot):
    if(0 < slot < 6):
        if(number[slot-1]==0):
            return True
        else:
            return False
    else:
        return False

turn = 0
player_number = [0,0,0,0,0]
player_slotcheck = [0,0,0,0,0]
cpu_number = [0,0,0,0,0]
cpu_slotcheck = [0,0,0,0,0]

#CPU algorithm here
#use a function to return best strategic slot
#sample rules:
#   the closer the number is to 9, the farther left it should go
#   the closer it is to 1, the farther right it should go
#   based on the desired position, sort through the cpu_number from
#       left to right or from right to left
#   additionally, cpu needs to take into account how many turns are
#       remaining--this will affect the probability of the cpu's choosing
#       a position all the way left or right
#
#the simplest rule would be:
#if rando == 9 and cpu_number[0] == 0:
#   cpu_number[0] = rando

print("\n\nLet's Play Numeroll!")
print("""
In this game you are given five random digits, one at a time,
and have to assign each of them to a slot in your five-digit number.
Can you beat the CPU and come up with the bigger number?
""")

while(turn < 5):
    valid_input = False
    rando = randint(0,9)
    print(f"\nRound {turn+1}: {rando}")
    print('Your number: ', player_number)
    #display CPU number for testing purposes only
    #print('CPU number:  ', cpu_number)
    print('To which slot will you assign the number? (1-5) ')
    while valid_input == False:
        try:
            pick = int(input('> '))
            if CorrectAssignment(player_slotcheck, pick):
                player_number[pick-1] = rando
                player_slotcheck[pick-1] = 1
                valid_input = True
            else:
                print('Invalid entry, please try again.')
        except ValueError:
            print('Invalid entry, please try again.')
    #still no defined AI algorithm
    CPUturn(cpu_number, cpu_slotcheck, rando)
    turn += 1

player_finalnum = (10000*player_number[0] + 1000*player_number[1] +
            100*player_number[2] + 10*player_number[3] +
            player_number[4])

cpu_finalnum = (10000*cpu_number[0] + 1000*cpu_number[1] +
            100*cpu_number[2] + 10*cpu_number[3] +
            cpu_number[4])

print('\nYOUR FINAL NUMBER:', player_finalnum)
print("COMPUTER'S FINAL NUMER:", cpu_finalnum)

if(player_finalnum > cpu_finalnum):
    print("YAY YOU WIN!")
elif(player_finalnum < cpu_finalnum):
    print("TOO BAD, YOU LOSE! TRY AGAIN")
else:
    print("IT'S A TIE! YOU'LL GET 'EM NEXT TIME.")
print("Thank you for playing NUMEROLL")
