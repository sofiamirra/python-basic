# Dinosaurs game

# Cards worth values: Red(5)= big , Green(3)=medium, Yellow(1)= small
dinosaurs = {"Red":5, "Green":3, "Yellow":1}

# Function to read file
def read_cards():
   with open("deck.txt", "r", encoding="utf-8") as f:
       deck = [line.strip("\n") for line in f]
       f.close()
   return deck

# Cards dealing: 15/30 per player (alternating)
def card_dealing(deck):
   counter = 0
   while counter < 30:
       counter += 1
       player1 = deck[0:len(deck):2]
       player2 = deck[1:len(deck):2]
   return player1, player2


# Function to simulate the game: at each hand, each player plays the first card of his deck
# If the played cards have different colors, the player that played the largest dinosaur wins, and takes all cards on the table.
# If the two cards have the same color, they are left on the table. At the end of the 15 hands the game is won by the player who collected cards with the largest total
# score.
def game_simulation(player1, player2):
   hand = 0
   score1 = 0
   score2 = 0
   while hand < 15:
       hand += 1
       print(f"\nHand {hand}")
       card1 = player1.pop(0)
       card2 = player2.pop(0)
       print(f"Player 1's card: {card1}")
       print(f"Player 2's card: {card2}")
       if dinosaurs[card1] > dinosaurs[card2]:
           score1 += dinosaurs[card1] + dinosaurs[card2]
           print("Result: Player 1 wins the hand")
       elif dinosaurs[card1] < dinosaurs[card2]:
           score2 += dinosaurs[card2] + dinosaurs[card1]
           print("Result: Player 2 wins the hand")
       elif dinosaurs[card1] == dinosaurs[card2]:
           print("Result: draw")
       print(f"Player 1's score: {score1}")
       print(f"Player 2's score: {score2}")
   if score1 > score2:
       print(f"Player 1 wins with {score1} points")
   if score2 > score1:
       print(f"Player 2 wins with {score2} points")

def main():
   print("Player 1's score: 0")
   print("Player 2's score: 0")
   deck = read_cards()
   player1, player2 = card_dealing(deck)
   game_simulation(player1, player2)
main()
