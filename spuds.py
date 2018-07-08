print('Hello! Do you want to boil some potatoes?')

answer = ''

while answer != 'y' and answer != 'n':
    print('Do you have potatoes? (y/n)')
    answer = input()
    if answer != 'y' and answer != 'n':
        print('Please answer with "y" or "n".')
        
    if answer == 'n':
        print('Do you have money? (y/n)')
        answer = input()
        if answer == 'n':
            print('You die...')
        elif answer == 'y':
            answer = ''
            while answer != 'y' and answer != 'n':
                print('Do you want to buy potatoes? (y/n)')
                answer = input()
                if answer == 'y':
                    print('You purchase spuds.')
                elif answer == 'n':
                    print('You die...')

    if answer == 'y':
        print('Cooking potatoes.')
