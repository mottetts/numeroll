from random import randint

print("\n\nLet's Play Numeroll!")
print("""
In this game you get five random digits and have to assign
each of them to a slot in your five-digit number. Can you beat the CPU
and come up with the bigger number?
""")

turn = 0
player_numstring = [0,0,0,0,0]
cpu_numstring = [0,0,0,0,0]
#don't allow for 00000 or 99999
#allzero = False
#allnine = False

#CPU algorithm can go here
#use a function to return best strategic slot
#sample rules:
#   the closer the number is to 9, the farther left it should go
#   the closer it is to 1, the farther right it should go
#   based on the desired position, sort through the cpu_numstring from
#       left to right or from right to left
#   additionally, cpu needs to take into account how many turns are
#       remaining--this will affect the probability of the cpu's choosing
#       a position all the way left or right
#
#the simplest rule would be:
#if rando == 9 and cpu_numstring[0] == 0:
#   cpu_numstring[0] = rando

while(turn < 5):
    rando = randint(1,9)
    print(f"\nRoll number {turn+1}: {rando}")
    print(player_numstring)
    #print('A B C D E')
    pick = int(input('To which slot will you assign the number? (1-5) '))
    if pick>=1 and pick<=5 and player_numstring[pick-1]==0:
        player_numstring[pick-1] = rando
    else:
        print('Error: assigned to default slot')
        player_numstring[-1] = rando

    cpu_numstring[-1-turn] = rando
    turn += 1

player_finalnum = (10000*player_numstring[0] + 1000*player_numstring[1] +
            100*player_numstring[2] + 10*player_numstring[3] +
            player_numstring[4])

cpu_finalnum = (10000*cpu_numstring[0] + 1000*cpu_numstring[1] +
            100*cpu_numstring[2] + 10*cpu_numstring[3] +
            cpu_numstring[4])

print('\nYOUR FINAL NUMBER:', player_finalnum)
print("COMPUTER'S FINAL NUMER:", cpu_finalnum)

if(player_finalnum > cpu_finalnum):
    print("YAY YOU WIN!")
elif(player_finalnum < cpu_finalnum):
    print("TOO BAD, YOU LOSE! TRY AGAIN")
else:
    print("IT'S A TIE! YOU'LL GET 'EM NEXT TIME.")
print("Thank you for playing NUMEROLL")
