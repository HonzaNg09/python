import random
card = random.randint(1, 13)
card_value = ''
second_card = random.randint(1, 13)

if card == 1:
    card_value = 'Ace'
elif card == 2:
    card_value = '2'
elif card == 3:
    card_value = '3'
elif card == 4:
    card_value = '4'
elif card == 5:
    card_value = '5'
elif card == 6:
    card_value = '6'
elif card == 7:
    card_value = '7'
elif card == 8:
    card_value = '8'
elif card == 9:
    card_value = '9'
elif card == 10:
    card_value = '10'
elif card == 11:
    card_value = 'Jack'
elif card == 12:
    card_value = 'Queen'
elif card == 13:
    card_value = 'King'
    card_value = 'King'
print(card)
print(card_value)


user_guess = input('Guess if the next number will be higher or lower: ')
print('Deals')

if second_card == 1:
    print('The second card is Ace')
elif 1 < second_card < 11:
    print('The second card is '+ str(second_card))
elif second_card == 11:
    print('The second card is Jack')
elif second_card == 12:
    print('The second card is Queen')
elif second_card == 13:
    print('The second card is King')
if user_guess == 'higher':
    if second_card > card:
        print('Your guess is correct')
    elif second_card < card:
        print('Your guess is wrong')
elif user_guess == 'lower':
    if second_card < card:
        print('Your guess is correct')
    elif second_card > card:
        print('Your guess is wrong')
        
        


