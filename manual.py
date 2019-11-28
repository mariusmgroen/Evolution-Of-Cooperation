# Import relevant libraries
import random


# Define each round's payoff
reward = 2
temptation = 3
sucker = 0
penalty = 1


# Define the AI's strategies
def simulate_round(player, chosen_cd):
    if player==1:
        # Always cooperate
        print(' You have chosen:  ', chosen_cd)
        ai_decision = 'c'
        return ai_decision

    elif player==2:
        # Always defect
        print(' You have chosen:  ', chosen_cd)
        ai_decision = 'd'
        return ai_decision

    elif player==3:
        # Choose random
        print(' You have chosen:  ', chosen_cd)
        ai_decision = random.choice(['c', 'd'])
        return ai_decision


# Define the updating of the score after each round
def update_score(decision_cd, ai_decision, score_user, score_ai):
    if decision_cd=='c' and ai_decision=='c':
        new_score_user = score_user + reward
        new_score_ai = score_ai + reward
        situation = 'CC / Reward!'

    elif decision_cd=='c' and ai_decision=='d':
        new_score_user = score_user + sucker
        new_score_ai = score_ai + temptation
        situation = "CD / Sucker's Payoff"

    elif decision_cd=='d' and ai_decision=='c':
        new_score_user = score_user + temptation
        new_score_ai = score_ai + sucker
        situation = 'DC / Temptation!'

    elif decision_cd=='d' and ai_decision=='d':
        new_score_user = score_user + penalty
        new_score_ai = score_ai + penalty
        situation = 'DD / Penalty'

    return new_score_user, new_score_ai, situation


# Show the payoff for each round
print('')
print('This is the payoff for each round:')
print(' CC: ' + str(reward) + ', ' + str(reward))
print(' CD: ' + str(sucker) + ', ' + str(temptation))
print(' DC: ' + str(temptation) + ', ' + str(sucker))
print(' DD: ' + str(penalty) + ', ' + str(penalty))


# Choose the opponent (and his strategy)
choose_opp = True
while choose_opp:
    decision_opp = input('\nChoose opponent (1/2/3): ')
    try:
        decision_opp = int(decision_opp)
        if decision_opp==1:
            print(' You have chosen Opp #1.')
            choose_opp = False
        elif decision_opp==2:
            print(' You have chosen Opp #2.')
            choose_opp = False
        elif decision_opp==3:
            print(' You have chosen Opp #3.')
            choose_opp = False
        else:
            print(' Choose between (1), (2), and (3)')
    except:
        print(' Choose between (1), (2), and (3)')


# Loop for the game
game = True

# Create scores
score_user = 0
score_ai = 0

while game:
    # Choose your own strategy
    choose_cd = True
    while choose_cd:
        decision_cd = input('\nChoose (c/d/q): ')
        if decision_cd=='c' or decision_cd=='d' or decision_cd=='q':
            choose_cd = False
        else:
            print(' Choose between cooperation (c) or defection (d).')
            print(' Press (q) to quit the simulation.')

    # User has chosen: Cooperation or Defection
    if decision_cd=='c' or decision_cd=='d':
        ai_decision = simulate_round(decision_opp, decision_cd)
        print(' The AI has chosen:', ai_decision, '\n')
        score_user, score_ai, situation = update_score(decision_cd,
                                                       ai_decision,
                                                       score_user,
                                                       score_ai)
        print(' ' + situation)
        print(' Your score:', score_user)
        print(" AI's score:", score_ai)

    # User has chosen: Quit
    elif decision_cd=='q':
        print(' You have chosen to quit the game.')
        print(' Your final score is:\n')
        print(' Bye.')
        break
