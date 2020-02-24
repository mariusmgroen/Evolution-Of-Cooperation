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



class player:
    def __init__(self, strat, score, decisions_own, decisions_opponent):
        self.strat = strat
        self.score = score
        self.decisions_own = decisions_own
        self.decisions_opponent = decisions_opponent

    def update_score(self, payoff):
        self.score.append(payoff)

    def show_total_score(self):
        total_score = 0
        for scores in self.score:
            total_score = total_score + scores[-1]
        return total_score

    def update_decisions_own(self, decisions):
        self.decisions_own.append(decisions)

    def update_strat(self, new_strat):
        self.strat = new_strat

random.seed(420)
player_1 = player('A', [], [], [])
player_2 = player('A', [], [], [])
player_3 = player('B', [], [], [])
player_4 = player('C', [], [], [])
players = [player_1, player_2, player_3, player_4]
player_pairs = list(combinations(players, 2))

for player_a, player_b in player_pairs:
    print('\nR |', player_a.strat, '', player_b.strat, ' +  +')
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
        print(nr_round+1, '|', player_a_decisions[nr_round], '', player_b_decisions[nr_round],
              '', player_a_score[nr_round+1], player_b_score[nr_round+1])
    player_a.update_score(player_a_score)
    player_b.update_score(player_b_score)
    player_a.update_decisions_own(player_a_decisions)
    player_b.update_decisions_own(player_b_decisions)


print(player_1.score)
p1_total_score = 0
for sublist in player_1.score:
    p1_total_score = p1_total_score + sublist[-1]
print(p1_total_score)

print(player_2.score)
p2_total_score = 0
for sublist in player_2.score:
    p2_total_score = p2_total_score + sublist[-1]
print(p2_total_score)

print(player_3.score)
p3_total_score = 0
for sublist in player_3.score:
    p3_total_score = p3_total_score + sublist[-1]
print(p3_total_score)

print(player_4.score)
p4_total_score = 0
for sublist in player_4.score:
    p4_total_score = p4_total_score + sublist[-1]
print(p4_total_score)

print(player_1.show_total_score())
print(player_2.show_total_score())
print(player_3.show_total_score())
print(player_4.show_total_score())



# Let user choose which strategies/how many players per strategy
# participate in the simulation
print('How many players of each strategy shall take place',
      'in the tournament?')
strategies_to_simulate = dict()
for key, value in strategies.items():
    i = int(input(' [{0}] {1:20s}'.format(str(key),
                                          str(value))))
    strategies_to_simulate[value] = i
print(strategies_to_simulate)                                       # Delete Control !
print(sum(strategies_to_simulate.values()))                         # Delete Control !
simulated_players = []
for key, value in strategies_to_simulate.items():
    for _ in range(value):
        simulated_players.append(player(key, [], [], []))
for i in range(len(simulated_players)):
    print('Player ' + str(i+1) + ') ', simulated_players[i].strat)









































#
