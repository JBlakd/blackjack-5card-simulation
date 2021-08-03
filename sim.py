print('Starting blackjack simulation')
import random

games_to_simulate = 100000
successful_games = 0
minimum_acceptable_sum = 18

for i in range(1, games_to_simulate + 1, 1):
  # draw 5 cards
  deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
  cards_dealt = []
  sum = 0
  for j in range(1, 5 + 1, 1):
    card_dealt = deck.pop(random.randint(0, len(deck)-1))
    cards_dealt.append(card_dealt)
    sum += card_dealt
    if len(cards_dealt) == 2 and sum == 11:
      # if you get an Ace and a 10-value card for your first two cards, you've hit blackjack and the game won't let 
      # you hit additional cards
      break
    if sum >= 21:
      # if you get a blackjack (sum == 21) before you've been dealt 5 cards, the game won't let you 
      # hit another card, even if you've been dealt an Ace which could be interpreted as a value 1 card instead of 11
      break
  if sum >= minimum_acceptable_sum and sum <= 21 and len(cards_dealt) == 5:
    # the last condition of the if statement deals with the edge case mentioned in the previous comment
    successful_games += 1
    print(f'Sum = {sum}. Cards dealt: {str(cards_dealt)}, {successful_games} success out of {i}. Percentage: {successful_games*100/i}%.')

print(f'{successful_games} successful games out of {i}. Success percentage: {successful_games*100/i}%.')
