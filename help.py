def printHelp():
        print('\n----------------------------------------------------------------------------')
        print('Help still under construction.')                             # Insert help code here!
        print('----------------------------------------------------------------------------\n')

        from colorama import Fore                                               # Test of help text
        from colorama import Style
        import help

        #for _ in range(25): # Why??!
            #print('')
        print(f'{Fore.GREEN}DESCRIPTION{Style.RESET_ALL}')  # Does not work in powershell!
        print("\tThe prisoner's dilemma is a standard example of a game analyzed in")
        print("\tgame theory that shows why two completely rational individuals might")
        print("\tnot cooperate, even if it appears that it is in their best interests")
        print("\tto do so. (Source: Wikipedia)\n")

        print(f'{Fore.GREEN}GAME MODES{Style.RESET_ALL}') # Does not work in powershell!
        print('\tWhat does [Play Matchups] do?')
        print('\tWhat does [Simulate Evolution] do?\n')

        print(f'{Fore.GREEN}RULES{Style.RESET_ALL}')  # Does not work in powershell!
        print('\tWhat is the matrix of payouts?\n')

        print('\t+--------------------+---------------------------------------------+')
        print('\t|                    |                Column Player                |')
        print('\t|                    |----------------------+----------------------+')
        print('\t|                    |       Cooperate      |        Defect        |')
        print('\t|                    |                      |                      |')
        print('\t|                    |                      |                      |')
        print('\t+--------+-----------+----------------------+----------------------+')
        print('\t|        |           |       R=3, R=3       |       S=0, T=5       |')
        print('\t|        | Cooperate |                      |                      |')
        print('\t|        |           |      Reward for      | Sucker\'s payoff, and |')
        print('\t|  Row   |           |  mutual cooperation  | temptation to defect |')
        print('\t| Player +-----------+----------------------+----------------------+')
        print('\t|        |           |       T=5, S=0       |       P=1, P=1       |')
        print('\t|        |  Defect   |                      |                      |')
        print('\t|        |           | Temptation to defect |    Punishment for    |')
        print('\t|        |           | and sucker\'s payoff  |   mutual defection   |')
        print('\t+--------+-----------+----------------------+----------------------+')

        print('\n----------------------------------------------------------------------------\n')

        print(f'{Fore.GREEN}SOURCES{Style.RESET_ALL}')
        print('\tAxelrod, R. (1984), The Evolution of Cooperation, Basic Books, NY.')

        print('\n----------------------------------------------------------------------------\n')
