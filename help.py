def print_help():

    from colorama import Fore
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

    print('\t+---------------------+---------------------------------------------+')
    print('\t|                     |                Column Player                |')
    print('\t|                     |----------------------+----------------------+')
    print('\t|                     |       Cooperate      |        Defect        |')
    print('\t|                     |                      |                      |')
    print('\t|                     |                      |                      |')
    print('\t+---------+-----------+----------------------+----------------------+')
    print('\t|         | Cooperate |       R=3, R=3       |       S=0, T=5       |')
    print('\t|         |           |                      |                      |')
    print('\t|         |           |      Reward for      | Sucker\'s payoff, and |')
    print('\t| Row     |           |  mutual cooperation  | temptation to defect |')
    print('\t| Player  +-----------+----------------------+----------------------+')
    print('\t|         | Defect    |       T=5, S=0       |       P=1, P=1       |')
    print('\t|         |           |                      |                      |')
    print('\t|         |           | Temptation to defect |    Punishment for    |')
    print('\t|         |           |  and sucker\'s payoff |   mutual defection   |')
    print('\t+---------+-----------+----------------------+----------------------+')

    print(f'{Fore.GREEN}SOURCES{Style.RESET_ALL}')
    print('\tAxelrod, R. (1984), The Evolution of Cooperation, Basic Books, NY.')
