
import random
import math
from itertools import permutations, product
import copy
from colorama import Fore, Back, Style, init
from copy import deepcopy

from CamelUpPlayer import CamelUpPlayer

class CamelUpBoard:
    def __init__(self, camel_styles: list[str]):
        self.TRACK_POSITIONS = 16
        self.DICE_VALUES = [1,2,3]
        self.BETTING_TICKET_VALUES = [5, 3, 2, 2]
        
        self.camel_styles = camel_styles
        self.camel_colors= camel_styles.keys()
        self.track = self.starting_camel_positions()
        self.pyramid = set(self.camel_colors)
        self.ticket_tents = {color:self.BETTING_TICKET_VALUES.copy() for color in self.camel_colors}
        self.dice_tents = [] #preserves order

    def starting_camel_positions(self)->list[list[str]]:
        '''Places camels on the board at the beginning of the game
            TODO: randomize these positions

            Return
               list[list[str]] - a 2D list model of the Camel Up race track
        '''
        track = [[] for i in range(self.TRACK_POSITIONS)]
        '''track[0] = list(self.camel_colors)
        random.shuffle(track[0])'''
        starting_camels = list(self.camel_colors)
        while len(starting_camels) > 0:
           camel = random.choice(starting_camels)
           starting_camels.remove(camel)
           roll = random.choice(self.DICE_VALUES)
           track[roll-1].append(camel)
        
        return track
    
    def print(self, players: list[CamelUpPlayer]):
        '''Prints the current state of the Camel Up board, including:
            - Race track with current camel positions
            - Betting Tents displaying available betting tickets
            - Dice Tents displaying an ordered collection of rolled dice
            - Player information for both players
                - name
                - coins
                - betting tickets for the current leg of the race
        '''
        board_string = "\n"
         #Ticket Tents
        ticket_string = "Ticket Tents: "
        for ticket_color in self.ticket_tents:
            if len(self.ticket_tents[ticket_color]) > 0:
                next_ticket_value = str(self.ticket_tents[ticket_color][0])
            else:
                next_ticket_value = 'X'
            ticket_string+=self.camel_styles[ticket_color]+next_ticket_value+Style.RESET_ALL+" "
        board_string += ticket_string +"\t\t"

        #Dice Tents
        dice_string = "Dice Tents: "
        for die in self.dice_tents:
            dice_string+=self.camel_styles[die[0]]+str(die[1])+Style.RESET_ALL+" "

        for i in range (5-len(self.dice_tents)):
            dice_string+=Back.WHITE+" "+Style.RESET_ALL+" "
        
        #Camels and Race Track
        board_string += dice_string +"\n"
        for row in range(4, -1, -1):
            row_str = ["  "]*16
            for i in range(len(self.track)):
                for camel_place, camel in enumerate(self.track[i]):
                    if camel_place == row:
                        row_str[i]=self.camel_styles[camel]+ '🐪' +  Style.RESET_ALL 
            board_string += "🌴 "+str("  ".join(row_str))+" |🏁\n"
        board_string += "   "+"".join([str(i)+"   " for i in range(1, 10)])
        board_string += "".join([str(i)+"  " for i in range(10, 17)])+"\n"

        #Player Info
        player_string=""
        for player in players:
            player_string+=f"{player.name} has {player.money} coins."
            if len(player.bets)>0:
                bets_string = " ".join([self.camel_styles[bet[0]]+str(bet[1])+Style.RESET_ALL for bet in player.bets])
                player_string += f" Bets: {bets_string}"  
            player_string+="\t\t" 
        
        board_string+=player_string
        print(board_string+"\n")

    def reset_tents(self):
        '''Rests dice tents and ticket tents at the end of a leg
        '''
        self.ticket_tents = {color:self.BETTING_TICKET_VALUES.copy() for color in self.camel_colors}
        self.dice_tents = []

    def place_bet(self, color:str)->tuple[str, int]:
        '''Manages the board perspective when a player places a bet:
            - removes the top betting ticket (with highest value) from the appropriate Ticket Tent
            - returns the ticket

            Args
               color (str) - the color of the ticket on which a player would like to bet: 'r'
           
            Return
                tuple(str, int) - a tuple representation of a betting ticket: ('r', 5)
        '''
        tickets_left = self.ticket_tents[color]
        ticket = ()
        if len(tickets_left)>0:
            ticket =(color, tickets_left[0])
            self.ticket_tents[color] = tickets_left[1:]
        return ticket

    def move_camel(self, die:tuple[str, int], verbose=False):
        '''Updates the track according to the die color and value
           The camel of the appropriate color moves the apporpriate number of spaces, 
           along with all camels riding on top of that camel.

           Args
             die (tuple[str, int]) - A tuple represntation of the die: ('g', 2)

           Return
             list[list[str]] - a 2D list model of the Camel Up race track
        '''
        if verbose: print("Current track state:", self.track)
        ### BEGIN SOLUTION
        # take in current position of camel, move it to "die roll + start"
        # also needs to take in whether it is stacked on top of another camel, or whether they have one on top
        # you can get track from self.track (it will not reshuffle every time)
        #print('this is the track')
        #print(self.track)
        position = 0
        for location in self.track:
            if die[0] in location:
                moving_camels = location[location.index(die[0]):]
                self.track[int(position + die[1])] += moving_camels
                for camel in moving_camels:
                    self.track[position].remove(camel)
                break
            position += 1
        ### END SOLUTION
        if verbose: print("Updated track state:", self.track)
        return self.track
    
    def shake_pyramid(self)->tuple[str, int]:
        '''Manages all the steps (from the board persepctive) involved with shaking the pyramid, 
           which includes:
                - selecting a random color and dice value from the dice colors in the pyramid
                - removing the rolled dice from the pyramid
                - placing the rolled dice in the dice tents

            Return
                tuple[str, int] - A tuple representation of the rolled die
        '''
        rolled_die=("", 0)
        ### BEGIN SOLUTION
        if len(self.pyramid) == 0:
            return rolled_die
        camel = random.choice(list(self.pyramid))
        self.pyramid.remove(camel)
        dice = random.choice(self.DICE_VALUES)
        self.dice_tents.append((camel, dice))
        rolled_die = (camel, dice)
        
        ### END SOLUTION
        return rolled_die

    def is_leg_finished(self)->bool:
        '''Determines whether the leg of a race is finished

           Return
             bool - True if all dice have been rolled, False otherwise
        '''
        ### BEGIN SOLUTION
        if len(self.pyramid) == 0:
            return True
        return False
        ### END SOLUTION

    def get_rankings(self):
        '''Determines first and second place camels on the track
           
           Returns:
            tuple: a tuple of strings of (1st, 2nd) place camels: ('b', 'y') 
        '''
        rankings = ("", "")
        ### BEGIN SOLUTION
        winner_list = list()
        while len(winner_list) < 2:
             for location in self.track[::-1]:
                 for camel in location[::-1]:
                     winner_list.append(camel)
        rankings = (winner_list[0], winner_list[1])

        ### END SOLUTION
        return rankings

    def get_all_dice_roll_sequences(self)-> set:
        '''
            Constructs a set of all possible roll sequences for the dice currently in the pyramid
            Note: Use itertools product function

            Return
               set[tuple[tuple[str, int]]] - A set of tuples representing all the ordered dice seqences 
                                             that could result from shaking all dice from the pyramid
        ''' 
        roll_space = set()
        ### BEGIN SOLUTION
        dice = [1, 2, 3]
        list_of_possbile_dice_rolls = list(product(dice, repeat=len(self.pyramid))) 
        list_of_camel_orders = list()
        
        for roll_sequence in permutations(self.pyramid, len(self.pyramid)):
            list_of_camel_orders.append(roll_sequence)
            
        for camel_order in list_of_camel_orders:
            for dice_rolls in list_of_possbile_dice_rolls:
                sequence = list()
                for pos in range(len(camel_order)):
                    sequence.append((camel_order[pos], dice_rolls[pos]))
                roll_space.add(tuple(sequence))
        ### END SOLUTION
        return roll_space
    
    def run_enumerative_leg_analysis(self)->dict[str, tuple[float, float]]:
        '''Conducts an enumerative analysis of the probability that each camel will win either 1st or 
           2nd place in this leg of the race. The enumerative analysis counts 1st/2nd place finishes 
           via calculating the entire state space tree

           General Steps:
                1) Precalculate all possible dice sequences for the dice currently in the pyramid
                2) Move through each sequence of possible dice rolls to count the number of 1st/2nd places 
                   finishes for each camel
                3) Calculates the probability that each camel will come in 1st or 2nd based on the total 
                   number of 1st/2nd finishes out of the total number of dice sequences

                TODO: Add notes about using deepcopy to preserve state
           
           Returns: 
              dict[str, tuple[float, float]] - A dictionary representing the probabilities that a camel will 
                                               come in first or second place according to an enumerative analysis
                {
                    'r':(0.5, 0.2),
                    'b':(0.1, 0.04),
                    ...
                }
        '''
        ## move_camel, get_rankings, get_all_dice_roll_sequences
        ## We have to go thru all dice sequences, track the amount of wins/2nd for all the camels
        ## wins / total in tuple
        win_percents={color:(float(0), float(0)) for color in self.camel_colors}
        ### BEGIN SOLUTION
        def get_rankings_sim(track_deepcopy: list):
            rankings = ("", "")
            winner_list = list()
            while len(winner_list) < 2:
                for location in track_deepcopy[::-1]:
                    for camel in location[::-1]:
                        winner_list.append(camel)
            rankings = (winner_list[0], winner_list[1])
            return rankings
        
        def move_camel_sim(die:tuple[str, int], track_deepcopy: list):
            position = 0
            for location in track_deepcopy:
                if die[0] in location:
                    moving_camels = location[location.index(die[0]):]
                    track_deepcopy[int(position + die[1])] += moving_camels
                    for camel in moving_camels:
                        track_deepcopy[position].remove(camel)
                    break
                position += 1
            return track_deepcopy
        
        first_place_dict = {color:0 for color in self.camel_colors}
        second_place_dict = {color:0 for color in self.camel_colors}
        winner_list = list()

        all_roll_sequences = self.get_all_dice_roll_sequences()
        
        for roll_sequence in all_roll_sequences:
            track_deepcopy1 = deepcopy(self.track)
            for roll in roll_sequence:
                track_deepcopy1 = move_camel_sim(roll, track_deepcopy1)
            winner_list.append(get_rankings_sim(track_deepcopy1))
            
        for winners in winner_list:
            first_place = winners[0]
            first_place_dict[first_place]=first_place_dict.get(first_place, 0)+1
            second_place_dict[winners[1]]=second_place_dict.get(winners[1], 0)+1
        
        roll_length = len(all_roll_sequences)
        
        for camel, first in first_place_dict.items():
            win_percents[camel] = (round(first/roll_length, 3), round(second_place_dict[camel]/roll_length, 3))

        return win_percents

    def run_experimental_leg_analysis(self, trials:int)->dict[str, tuple[float, float]]:
        '''Conducts an experimental analysis (ie. a random simulation) of the probability that each camel
            will win either 1st or 2nd place in this leg of the race. The experimental analysis counts 
            1st/2nd place finishes by counting outcomes from randomly shaking the pyramid over a given 
            number of trials.
           
           General Steps:
                1) Shake the pyramid enough times to randomly generate a dice sequence to finish the leg
                2) Count a 1st/2nd place finish for each camel
                3) Repeat steps #1 - #2 trials number of times
                3) Calculate the probability that each camel will come in 1st or 2nd based on the total 
                   number of 1st/2nd finishes out of the total number of trials

                TODO: Add notes about using deepcopy to preserve state

           Args
              trials (int): The number of random simulations to conduct

           Returns: 
              dict[str, tuple[float, float]] - A dictionary representing the probabilities that a camel will 
                                               come in first or second place according to an enumerative analysis
                {
                    'r':(0.5, 0.2),
                    'b':(0.1, 0.04),
                    ...
                }
        '''
        win_percents={color:(0, 0) for color in self.camel_colors}
        ### BEGIN SOLUTION
        def move_camel_sim(die:tuple[str, int], track_deepcopy: list):
            position = 0
            for location in track_deepcopy:
                if die[0] in location:
                    moving_camels = location[location.index(die[0]):]
                    track_deepcopy[int(position + die[1])] += moving_camels
                    for camel in moving_camels:
                        track_deepcopy[position].remove(camel)
                    break
                position += 1
            return track_deepcopy
        def get_rankings_sim(track_deepcopy: list):
            rankings = ("", "")
            winner_list = list()
            while len(winner_list) < 2:
                for location in track_deepcopy[::-1]:
                    for camel in location[::-1]:
                        winner_list.append(camel)
            rankings = (winner_list[0], winner_list[1])
            return rankings
        tests = 0
        
        first_place_dict = {color:0 for color in self.camel_colors}
        second_place_dict = {color:0 for color in self.camel_colors}
        winner_list = list()
        
        all_roll_sequences = sorted(self.get_all_dice_roll_sequences())
       
        while tests < trials:
            test_run = random.choice(all_roll_sequences)
            track_deepcopy1 = deepcopy(self.track)
            for roll in test_run:
                track_deepcopy1 = move_camel_sim(roll, track_deepcopy1)
            winner_list.append(get_rankings_sim(track_deepcopy1))
            tests +=1

        for winners in winner_list:
            first_place = winners[0]
            first_place_dict[first_place]=first_place_dict.get(first_place, 0)+1
            second_place_dict[winners[1]]=second_place_dict.get(winners[1], 0)+1
        
        for camel, first in first_place_dict.items():
            win_percents[camel] = (round(first/trials, 3), round(second_place_dict[camel]/trials, 3))

        
        ### END SOLUTION
        return win_percents
   
if __name__ == "__main__":
    camel_styles= {
            "r": Back.RED+Style.BRIGHT,
            "b": Back.BLUE+Style.BRIGHT,
            "g": Back.GREEN+Style.BRIGHT,
            "y": Back.YELLOW+Style.BRIGHT,
            "p": Back.MAGENTA
    }
    board = CamelUpBoard(camel_styles)
    p1 = CamelUpPlayer("p1")
    p2 = CamelUpPlayer("p2")
    board.print([p1, p2])
    die = ('b', 1)
    board.move_camel(die)
    #Roll 3 random dice
    rolled_die = board.shake_pyramid()
    board.move_camel(rolled_die)
    rolled_die = board.shake_pyramid()
    board.move_camel(rolled_die)
    rolled_die = board.shake_pyramid()
    board.move_camel(rolled_die)
    board.print([p1, p2])
    #Probabilites
    all_possible_dice_sequences= board.get_all_dice_roll_sequences()
    print(f"{len(all_possible_dice_sequences)} possible dice sequences for {len(board.pyramid)} dice in the pyramid:") 
    print("Enumerative Probabilities:", board.run_enumerative_leg_analysis())
    print("Experimental Probabilities:", board.run_experimental_leg_analysis(5000))