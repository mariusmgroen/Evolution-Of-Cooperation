# Import relevant libraries
import random
import time
import os


# ------------------------------------------------------------------------------
def strat_C():
    ai_decision = 'C'
    return ai_decision

def strat_D():
    ai_decision = 'D'
    return ai_decision

def strat_RAND():
    decisions = ['C', 'D']
    ai_decision = random.choice(decisions)
    return ai_decision

def strat_TFT(round, decisions):
    if round==0:
        ai_decision = 'C'
    else:
        opp_decision_before = decisions[round-1]
        ai_decision = str(opp_decision_before)
    return ai_decision
def strat_RESENT():
    ai_decision = 'C'                                                           # Update!
    return ai_decision
# ------------------------------------------------------------------------------
def simulate_round(strategy_a, strategy_b):
    if strategy_a=='A':
        decision_a = strat_C()
    elif strategy_a=='B':
        decision_a = strat_D()
    elif strategy_a=='C':
        decision_a = strat_RAND()
    elif strategy_a=='D':
        decision_a = strat_TFT(round, decisions_b)
    elif strategy_a=='E':
        decision_a = strat_RESENT()

    if strategy_b=='A':
        decision_b = strat_C()
    elif strategy_b=='B':
        decision_b = strat_D()
    elif strategy_b=='C':
        decision_b = strat_RAND()
    elif strategy_b=='D':
        decision_b = strat_TFT(round, decisions_a)
    elif strategy_b=='E':
        decision_b = strat_RESENT()

    return decision_a, decision_b
# ------------------------------------------------------------------------------
# Define the updating of the score after each round
reward = 3
temptation = 5
sucker = 0
penalty = 1

def update_score(decision_a, decision_b, scores_a, scores_b, round):
    if decision_a=='C' and decision_b=='C':
        scores_a.append(scores_a[round] + reward)
        scores_b.append(scores_b[round] + reward)
        situation = ('+' + str(reward), '+' + str(reward))

    elif decision_a=='C' and decision_b=='D':
        scores_a.append(scores_a[round] + sucker)
        scores_b.append(scores_b[round] + temptation)
        situation = ('  ', '+' + str(temptation))

    elif decision_a=='D' and decision_b=='C':
        scores_a.append(scores_a[round] + temptation)
        scores_b.append(scores_b[round] + sucker)
        situation = ('+' + str(temptation), '  ')

    elif decision_a=='D' and decision_b=='D':
        scores_a.append(scores_a[round] + penalty)
        scores_b.append(scores_b[round] + penalty)
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


# Choose first strategy
choose_strategy_a = True
while choose_strategy_a:
    # Let user choose strategies
    print('\n')
    for key, value in strategies.items():
        print(' [' + key + ']', value)
    strategy_a = input('Choose the first strategy: ')
    if strategy_a in legit_strategies:
        strategy_a = strategy_a.capitalize()
        choose_strategy_a = False
    else:
        print('You have to choose from A, B, C, or D!')                         # Use dict keys


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
        print('You have to choose from A, B, C, or D!')                         # Use dict keys


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

#min_nr_of_rounds = 1
#max_nr_of_rounds = 2

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
for round in range(nr_of_rounds):
    decision_a, decision_b = simulate_round(strategy_a, strategy_b)
    decisions_a.append(decision_a)
    decisions_b.append(decision_b)
    scores_a, scores_b, situation = update_score(decision_a,
                                                 decision_b,
                                                 scores_a,
                                                 scores_b,
                                                 round)
    if round < 9:
        print(' |  [' + str(round+1) + ']   ', decision_a, '  ',
                                               decision_b, '   | ',
                                               situation[0], '',
                                               situation[1])
    elif round < 99:
        print(' |  [' + str(round+1) + ']  ', decision_a, '  ',
                                              decision_b, '   | ',
                                              situation[0], '',
                                              situation[1])
    else:
        print(' |  [' + str(round+1) + '] ', decision_a, '  ',
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













# ------------------------------------------------------------------------------
# To Do:
#
# - "Keep Playing?"
#   Implementation of a while-loop in which the program does not
#   terminate after each run of a single round
#
# - Menu
#   Add a game menu in which the player can choose between playing
#   multiple sessions with choosen strategies OR let the arena/all vs all
#   start
#
# - All vs all
#   Implementation of "Let all strategies work against each other"
#
# - Emergent Phenomena
#   Evolution of Generations: less succesfull strategies need to be
#   replaced by the most succesfull ones.
#
