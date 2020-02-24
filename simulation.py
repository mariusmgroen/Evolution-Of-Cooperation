# Import relevant libraries
import random
import time
import os
from itertools import combinations

# Change Directory (so that header.py runs)
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)


# ------------------------------------------------------------------------------
# Define the Strategies, which can compete
#  Each strategy is a method which returns the strategies decision
#  (aka "ai_decision"), which is represented as a string of C or D.
def strat_C():
    # Always cooperate
    ai_decision = 'C'
    return ai_decision

def strat_D():
    # Always defect
    ai_decision = 'D'
    return ai_decision

def strat_RAND():
    # Choose randomly between cooperation and defection
    decisions = ['C', 'D']
    ai_decision = random.choice(decisions)
    return ai_decision

def strat_TFT(nr_round, decisions):
    # Play "tit for tat"; start with cooperation and then mirror
    #                     the opponent's last move
    if nr_round==0:
        ai_decision = 'C'
    else:
        opp_decision_before = decisions[nr_round-1]
        ai_decision = str(opp_decision_before)
    return ai_decision

def strat_RESENT(nr_round, decisions):
    # Always cooperate until the opponent defects the first time
    # from then on, always defects
    if nr_round==0:
        ai_decision = 'C'
    else:
        if 'D' in decisions:
            ai_decision = 'D'
        else:
            ai_decision = 'C'
    return ai_decision


# ------------------------------------------------------------------------------
# Define choosen strategies being the strategies defined above
def simulate_round(strategy_a, strategy_b, decisions_a, decisions_b, nr_round):
    if strategy_a=='A':
        decision_a = strat_C()
    elif strategy_a=='B':
        decision_a = strat_D()
    elif strategy_a=='C':
        decision_a = strat_RAND()
    elif strategy_a=='D':
        decision_a = strat_TFT(nr_round, decisions_b)
    elif strategy_a=='E':
        decision_a = strat_RESENT(nr_round, decisions_b)

    if strategy_b=='A':
        decision_b = strat_C()
    elif strategy_b=='B':
        decision_b = strat_D()
    elif strategy_b=='C':
        decision_b = strat_RAND()
    elif strategy_b=='D':
        decision_b = strat_TFT(nr_round, decisions_a)
    elif strategy_b=='E':
        decision_b = strat_RESENT(nr_round, decisions_a)

    return decision_a, decision_b


# ------------------------------------------------------------------------------
# Define the updating of the score after each round
# This are the payoffs of each combination
reward = 3
temptation = 5
sucker = 0
penalty = 1

def update_score(decision_a, decision_b, scores_a, scores_b, nr_round):
    if decision_a=='C' and decision_b=='C':
        scores_a.append(scores_a[nr_round] + reward)
        scores_b.append(scores_b[nr_round] + reward)
        situation = ('+' + str(reward), '+' + str(reward))

    elif decision_a=='C' and decision_b=='D':
        scores_a.append(scores_a[nr_round] + sucker)
        scores_b.append(scores_b[nr_round] + temptation)
        situation = ('  ', '+' + str(temptation))

    elif decision_a=='D' and decision_b=='C':
        scores_a.append(scores_a[nr_round] + temptation)
        scores_b.append(scores_b[nr_round] + sucker)
        situation = ('+' + str(temptation), '  ')

    elif decision_a=='D' and decision_b=='D':
        scores_a.append(scores_a[nr_round] + penalty)
        scores_b.append(scores_b[nr_round] + penalty)
        situation = ('+' + str(penalty), '+' + str(penalty))

    return scores_a, scores_b, situation


# ------------------------------------------------------------------------------
# Create a dictionary with all strategies
strategies = {'A': 'Always Cooperate',
              'B': 'Always Defect',
              'C': 'Play Random',
              'D': 'Tit for Tat',
              'E': 'Resentful'}
legit_strategies = []
for key in strategies.keys():
    legit_strategies.append(key)
    legit_strategies.append(key.lower())


# ------------------------------------------------------------------------------
# Create a dictionary with all modes
modes = {'1': 'Play Matchups',
         '2': 'Simulate Evolution',
         '3': 'Help!',
         '4': 'Quit'}
legit_modes = list(modes.keys())


# ------------------------------------------------------------------------------
# Run Header/Manual before
choose_intro = True
while choose_intro:
    intro = input('Do you want to see the intro? (y/n) ')
    if intro=='y':
        choose_intro = False
        os.system('python3 header.py')
    elif intro=='n':
        print('Ok... :(')
        choose_intro = False
    else:
        print('Please enter (y) or (n).')


# ------------------------------------------------------------------------------
# Complete Loop
play_on = True
while play_on:

    # Start menu in which the player can
    # choose the mode of the game
    #  Create booleans for each mode
    play_manual = False
    play_simulation = False
    play_help = False

    #  activate boolean of chosen mode
    print('\n')
    print('The following modes are available for you:')
    for key, value in modes.items():
        print(' [' + key + ']', value)
    chosen_mode = input('Choose mode: ')
    if chosen_mode == '1':
        play_manual = True
    elif chosen_mode == '2':
        play_simulation = True
    elif chosen_mode == '3':
        play_help = True
    elif chosen_mode == '4':
        play_on = False
    else:
        print('You have to choose from:', legit_modes)


    # --------------------------------------------------------------------------
    # Manual simulation of single rounds of user-choosen strategies
    while play_manual:
        # Choose first strategy
        choose_strategy_a = True
        while choose_strategy_a:
            # Let user choose strategies
            print('\n')
            print('The following strategies are available for you:')
            for key, value in strategies.items():
                print(' [' + key + ']', value)
            strategy_a = input('Choose the first strategy: ')
            if strategy_a in legit_strategies:
                strategy_a = strategy_a.capitalize()
                choose_strategy_a = False
            else:
                print('You have to choose from:', list(strategies.keys()))


        # Choose second strategy
        choose_strategy_b = True
        while choose_strategy_b:
            # Let user choose strategies
            print('\n')
            for key, value in strategies.items():
                print(' [' + key + ']', value)
            strategy_b = input('Choose the second strategy: ')
            if strategy_b in legit_strategies:
                strategy_b = strategy_b.capitalize()
                choose_strategy_b = False
            else:
                print('You have to choose from:', list(strategies.keys()))


        # Define number of rounds
        choose_min_rounds = True
        while choose_min_rounds:
            min_nr_of_rounds = input('\nMinimum number of rounds: ')
            try:
                min_nr_of_rounds = int(min_nr_of_rounds)
                if min_nr_of_rounds > 0:
                    choose_min_rounds = False
                else:
                    print('Enter an integer greater zero!')
            except:
                print('Enter an integer greater zero!')

        choose_max_rounds = True
        while choose_max_rounds:
            max_nr_of_rounds = input('\nMaximum number of rounds: ')
            try:
                max_nr_of_rounds = int(max_nr_of_rounds)
                if max_nr_of_rounds >= min_nr_of_rounds:
                    choose_max_rounds = False
                else:
                    print('Maximum needs to be larger than the minimum!')
            except:
                print('Enter an integer!')

        nr_of_rounds = random.randint(min_nr_of_rounds, max_nr_of_rounds)


        # Show the simulated rounds
        decisions_a = []
        decisions_b = []
        scores_a = [0]
        scores_b = [0]
        if nr_of_rounds==1:
            print('\n | Simulating', nr_of_rounds, 'round...')
        else:
            print('\n | Simulating', nr_of_rounds, 'rounds...')
        print(' |  Player 1:', strategies.get(strategy_a))
        print(' |  Player 2:', strategies.get(strategy_b))
        print(' |')
        print(' |        P1   P2    .  Payoff')
        print(' | ------------------|--------')
        for nr_round in range(nr_of_rounds):
            decision_a, decision_b = simulate_round(strategy_a, strategy_b, decisions_a, decisions_b, nr_round)
            decisions_a.append(decision_a)
            decisions_b.append(decision_b)
            scores_a, scores_b, situation = update_score(decision_a,
                                                         decision_b,
                                                         scores_a,
                                                         scores_b,
                                                         nr_round)
            if nr_round < 9:
                print(' |  [' + str(nr_round+1) + ']   ', decision_a, '  ',
                                                          decision_b, '   | ',
                                                          situation[0], '',
                                                          situation[1])
            elif nr_round < 99:
                print(' |  [' + str(nr_round+1) + ']  ', decision_a, '  ',
                                                         decision_b, '   | ',
                                                         situation[0], '',
                                                         situation[1])
            else:
                print(' |  [' + str(nr_round+1) + '] ', decision_a, '  ',
                                                        decision_b, '   | ',
                                                        situation[0], '',
                                                        situation[1])
            time.sleep(0.5)
        print('')

        length_strategy_a = len(str(strategies.get(strategy_a)))
        length_strategy_b = len(str(strategies.get(strategy_b)))
        if length_strategy_a > length_strategy_b:
            difference = length_strategy_a - length_strategy_b
            print('Final Score P1 (' + str(strategies.get(strategy_a)) + '): ',
                  scores_a[-1])
            print('Final Score P2 (' + str(strategies.get(strategy_b)) + '):',
                  difference * ' ',
                  scores_b[-1])
        else:
            difference = length_strategy_b - length_strategy_a
            print('Final Score P1 (' + str(strategies.get(strategy_a)) + '):',
                  difference * ' ',
                  scores_a[-1])
            print('Final Score P2 (' + str(strategies.get(strategy_b)) + '): ',
                  scores_b[-1])
        print('')

        # Choose to play another game
        choose_play_on = True
        while choose_play_on:
            chosen_play_on = input('Do you want to play another round? (y/n) ')
            if chosen_play_on == 'y':
                choose_play_on = False
            elif chosen_play_on == 'n':
                print('You have chosen to end the game.\n')
                choose_play_on = False
                play_manual = False
            else:
                print('You have to choose between yes (y) and no (n)!\n')


    # --------------------------------------------------------------------------
    # Simulation
    while play_simulation:

        print('\nSimulation still under construction.\n')                       # Insert simulation code here!

        # Choose to play another game
        choose_play_on = True
        while choose_play_on:

            class player:
                def __init__(self, strat, score, decisions_own, decisions_opponent):
                    self.strat = strat
                    self.score = score
                    self.decisions_own = decisions_own
                    self.decisions_opponent = decisions_opponent

                def update_score(self, payoff):
                    self.score.append(payoff)

                def show_score(self):
                    return sum(self.score)

                def update_decisions_own(self, decisions):
                    self.decisions_own.append(decisions)

                def update_strat(self, new_strat):
                    self.strat = new_strat

            player_1 = player('A', [], [], [])
            player_2 = player('B', [], [], [])
            player_3 = player('C', [], [], [])
            player_4 = player('D', [], [], [])
            player_5 = player('E', [], [], [])
            players = [player_1, player_2, player_3, player_4, player_5]        # Create from useful input
            player_pairs = list(combinations(players, 2))

            for player_a, player_b in player_pairs:
                print('\nR', player_a.strat, player_b.strat, '+ +')
                player_a_decisions = []
                player_b_decisions = []
                player_a_score = [0]
                player_b_score = [0]
                for nr_round in range(10):
                    player_a_decision, player_b_decision = simulate_round(player_a.strat, player_b.strat,
                                                                          player_a_decisions, player_b_decisions,
                                                                          nr_round)
                    player_a_decisions.append(player_a_decision)
                    player_b_decisions.append(player_b_decision)
                    player_a_score, player_b_score, situation = update_score(player_a_decision,
                                                                  player_b_decision,
                                                                  player_a_score,
                                                                  player_b_score,
                                                                  nr_round)
                    print(nr_round+1, player_a_decisions[nr_round], player_b_decisions[nr_round],
                          player_a_score[nr_round+1], player_b_score[nr_round+1])
                player_a.update_score(player_a_score)
                player_b.update_score(player_b_score)
                player_a.update_decisions_own(player_a_decisions)
                player_b.update_decisions_own(player_b_decisions)

            # Let user choose which strategies/how many players per strategy
            # participate in the simulation
#            print('How many players of each strategy shall take place',
#                  'in the tournament?')
#            strategies_to_simulate = dict()
#            for key, value in strategies.items():
#                i = int(input(' [{0}] {1:20s}'.format(str(key),
#                                                      str(value))))
#                strategies_to_simulate[value] = i
#
#            print(strategies_to_simulate)                                       # Delete Control !
#            print(sum(strategies_to_simulate.values()))                         # Delete Control !
#
#            simulated_players = []
#            for key, value in strategies_to_simulate.items():
#                for _ in range(value):
#                    simulated_players.append(SimulatedPlayer(key))
#            for i in range(len(simulated_players)):
#                print('Player ' + str(i+1) + ') ', simulated_players[i].sim_strategy)



            chosen_play_on = input('Do you want to simulate another round? (y/n) ')
            if chosen_play_on == 'y' or chosen_play_on == 'Y':
                choose_play_on = False
            elif chosen_play_on == 'n' or chosen_play_on == 'N':
                print('You have chosen to end the simulation.\n')
                choose_play_on = False
                play_simulation = False
            else:
                print('You have to choose between yes (y) and no (n)!\n')


    # --------------------------------------------------------------------------
    # Help / Information
    while play_help:
        print('\nHelp still under construction.\n')                             # Insert help code here!

        from colorama import Fore                                               # Test of help text
        from colorama import Style
        for _ in range(25):
            print('')
        print(f'{Fore.GREEN}DESCRIPTION{Style.RESET_ALL}')
        print('\tExplain what PD is.')
        print('')
        print(f'{Fore.GREEN}GAME MODES{Style.RESET_ALL}')
        print('\tWhat does [Play Matchups] do?')
        print('\tWhat does [Simulate Evolution] do?')
        print('')
        print(f'{Fore.GREEN}RULES{Style.RESET_ALL}')
        print('\tWhat is the matrix of payouts?')

        print('\t+--------------------+---------------------------------------------+')
        print('\t|                    |                Column Player                |')
        print('\t|                    |----------------------+----------------------+')
        print('\t|                    |       Cooperate      |        Defect        |')
        print('\t|                    |                      |                      |')
        print('\t|                    |                      |                      |')
        print('\t+--------+-----------+----------------------+----------------------+')
        print('\t|        | Cooperate |       R=3, R=3       |       S=0, T=5       |')
        print('\t|   Row  |           |                      |                      |')
        print('\t| Player |           |      Reward for      | Sucker\'s payoff, and |')
        print('\t|        |           |  mutual cooperation  | temptation to defect |')
        print('\t+--------+-----------+----------------------+----------------------+')
        print('\t|        | Defect    |       T=5, S=0       |       P=1, P=1       |')
        print('\t|        |           |                      |                      |')
        print('\t|        |           | Temptation to defect |    Punishment for    |')
        print('\t|        |           |  and sucker\'s payoff |   mutual defection   |')
        print('\t+--------+-----------+----------------------+----------------------+')

        print(f'{Fore.GREEN}SOURCES{Style.RESET_ALL}')
        print('\tAxelrod, R. (1984), The Evolution of Cooperation, Basic Books, NY.')

        input('\nPress Enter to return to the menu.\n')
        print('Returning to menu...')
        time.sleep(1)
        play_help = False







# ------------------------------------------------------------------------------
# To Do:
#
# - All vs all / Simulation (Menu: 2)
#   Implementation of "Let all strategies work against each other"
#
# - Help (Menu: 3)
#   Implementation of Help / Information
#
# - Emergent Phenomena
#   Evolution of Generations: less succesfull strategies need to be
#   replaced by the most succesfull ones.
#
