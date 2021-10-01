import random
import time
#created by Ja'Crispy
#note, your choice must be a r, p, or s

playerwins = 0
computerwins = 0
gamesplayed = 0

CHOICES = 'rps'

while True:
    
    def get_player_choice():
        player_choice = None
        while player_choice is None:
            player_choice = input('Choices: \nr \np \ns \n\npick (type leave type exit): ')
            if player_choice == "exit":
                print("goodbye")
                time.sleep(1.5)
                quit()
            if player_choice.lower() not in CHOICES:
                player_choice = None
            return player_choice.lower()
            #if player_choice == "stats":
             #   stats()

    #def stats():
     #   global playerwins
      #  global computerwins
       # print("Your Wins: " + str(playerwins) + "\nComputer Wins: " + str(computerwins))
        #print("Games Played: ")


    def get_computer_choice():
        """Have the computer pick one of the valid choices at random"""
        computer_choice = random.randint(0, 2)
        computer_choice = CHOICES[computer_choice]
        return computer_choice


    def is_draw(player_choice, computer_choice):
        """Check if game was a draw"""
        if player_choice == computer_choice:
            return True


    def print_winner(player_choice, computer_choice):
        global playerwins
        global computerwins
        """Check to see who won"""
        if player_choice == 'r' and computer_choice == 's':
            print('Player wins!')
            print('%s beats %s' % (player_choice, computer_choice))
            playerwins += 1
            print("\n \n")
            time.sleep(3)
        elif player_choice == 's' and computer_choice == 'p':
            print('Player wins!')
            print('%s beats %s' % (player_choice, computer_choice))
            playerwins += 1
            print("\n \n")
            time.sleep(3)
        elif player_choice == 'p' and computer_choice == 'r':
            print('Player wins!')
            print('%s beats %s' % (player_choice, computer_choice))
            playerwins += 1
            print("\n \n")
            time.sleep(3)
        else:
            global computerwins
            print('Computer wins!')
            print('%s beats %s' % (computer_choice, player_choice))
            computerwins += 1
            print("")
            print("")
            time.sleep(3)


    def play_game():
        """play the game"""
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        if is_draw(player_choice, computer_choice):
            print("It's a draw, both players picked %s: " % player_choice)
            time.sleep(3)
        else:
            global gamesplayed
            gamesplayed += 1
            print("Computer picked: %s" % computer_choice)
            print("Player picked: %s" % player_choice)
            print_winner(player_choice, computer_choice)
            print("Games Played: " + str(gamesplayed) + "\nPlayer Wins: " + str(playerwins) + " \nComputer Wins: " + str(computerwins))
            time.sleep(3)

    if __name__ == "__main__":
        play_game()
